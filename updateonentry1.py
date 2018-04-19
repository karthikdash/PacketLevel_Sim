import numpy as np
from call1 import call1
from call2 import call2
from dijkstra import dijkstra


def findRoute(p, s, d, flow_type, min_rate, flownumber, userpriority, s_new, d_new,
             flow_type_new, min_rate_new, flownumber_new, userpriority_new, path_final, wt_matx,
             wt_matx_real, wt_matx_real1, blockstate, flow_duration, flowarrival_time, connection_type,
             packet_size, packet_datarate, header_size):
    scale = 100.0
    blockstate_new = 0
    [s1, s2] = np.shape(path_final)
    if flow_type_new == 0:
        if connection_type == 0:  # Two way Voice Calls
            # Calls call1.py
            # Source to destination calculation
            wt_matx, wt_matx_real, wt_matx_real1, path1 = \
                call1(p, s_new, d_new, flow_type_new, min_rate_new, wt_matx,
                     wt_matx_real, wt_matx_real1)
            v = path1 == np.zeros((p))
            if v.all():
                blockstate_new = 0  # Represents blockstate
            else:
                # Destination to source calculation
                wt_matx, wt_matx_real, wt_matx_real1, path2 = \
                    call1(p, d_new, s_new, flow_type_new, min_rate_new, wt_matx,
                          wt_matx_real, wt_matx_real1)
                v = path2 == np.zeros((p))
                if v.all():
                    blockstate_new = 0
                    # Call2
                    # If blocked by destination to source, we invoke Call2
                    cd1 = call2(p, path1, flow_type_new, min_rate_new, wt_matx,
                                wt_matx_real, wt_matx_real1)
                    cd1.execute()
                    wt_matx = cd1.wt_matx
                    wt_matx_real = cd1.wt_matx_real
                    wt_matx_real1 = cd1.wt_matx_real1
                else:
                    blockstate_new = 1
                    # Packets level Variables
                    fwdpath = path1
                    bkwdpath = path2
                    noofpaths = 1
                    for loop in range(0, s1-1, 1):
                        # Not sure about this loop[0] or loop[1]
                        if path_final[loop][0] == 0:
                            no_of_packets = int(flow_duration*((packet_datarate / scale) / (packet_size - header_size)))

                            v = [flownumber_new, flow_type_new,
                                 no_of_packets, connection_type,
                                 min_rate_new, flowarrival_time, flowarrival_time, flow_duration, packet_datarate / scale, 0, no_of_packets, 0, 0, 0, 0]
                            pp = np.concatenate((v, path1))
                            path_final[loop, :] = np.concatenate((pp, [0]))

                            v1 = [flownumber_new, flow_type_new,
                                 no_of_packets, connection_type,
                                 min_rate_new, flowarrival_time, flowarrival_time, flow_duration, packet_datarate / scale, 0, no_of_packets, 0, 0, 0, 0]
                            pp1 = np.concatenate((v1, path2))
                            path_final[loop + 1, :] = np.concatenate((pp1, [0]))
                            # np.savetxt("pathfinal1.csv", path_final, delimiter=",")
                            break
        else:  # One Way Video Calls
            # Source to destination calculation
            wt_matx, wt_matx_real, wt_matx_real1, path1 = \
                call1(p, s_new, d_new, flow_type_new, min_rate_new, wt_matx,
                      wt_matx_real, wt_matx_real1)
            v = path1 == np.zeros((p))
            if v.all():
                blockstate_new = 0  # Represents blockstate
            else:
                blockstate_new = 1
                # Packets level Variables
                fwdpath = path1
                bkwdpath = None  # None is python equivalent for nil
                noofpaths = 1
                for loop in range(0, s1-1, 1):
                    # Not sure about this loop[0] or loop[1]
                    if path_final[loop][0] == 0:
                        no_of_packets = int(flow_duration * ((packet_datarate / scale) / (packet_size - header_size)))

                        v = [flownumber_new, flow_type_new,
                            no_of_packets, connection_type,
                            min_rate_new, flowarrival_time, flowarrival_time, flow_duration, packet_datarate/scale, 0, no_of_packets, 0, 0, 0, 0]
                        pp = np.concatenate((v, path1))
                        path_final[loop, :] = np.concatenate((pp, [0]))
                        break
    elif flow_type_new == 2:
        wt_matx, wt_matx_real, wt_matx_real1, path1 = \
            call1(p, s_new, d_new, flow_type_new, min_rate_new, wt_matx,
                  wt_matx_real, wt_matx_real1)
        v = path1 == np.zeros((p))
        if v.all():
            blockstate_new = 0
        else:
            blockstate_new = 1
            fwdpath = path1
            bkwdpath = None  # None is python equivalent for nil
            noofpaths = 1
            for loop in range(0, s1, 1):
                # print loop
                # Not sure about this loop[0] or loop[1]
                if path_final[loop][0] == 0:
                    file_limit = int(1.0*flow_duration/(packet_size - header_size)/scale)
                    if s_new == 3 and d_new == 13:
                        satellite_link = 1
                    else:
                        satellite_link = 0

                    v = [flownumber_new, flow_type_new,
                         file_limit, connection_type,
                         min_rate_new, flowarrival_time, flowarrival_time, flow_duration, packet_datarate/scale, file_limit, 0, 0, satellite_link, 0, 0]
                    pp = np.concatenate((v, path1))
                    path_final[loop, :] = np.concatenate((pp, [0]))
                    break
    if blockstate_new == 1:
        s = np.append(s, s_new)
        d = np.append(d, d_new)
        flow_type = np.append(flow_type, flow_type_new)
        min_rate = np.append(min_rate, min_rate_new)
        flownumber = np.append(flownumber, flownumber_new)
        userpriority = np.append(userpriority, userpriority_new)
        blockstate = np.append(blockstate, blockstate_new)
    return s, d, flow_type, min_rate, flownumber, userpriority, blockstate, blockstate_new, wt_matx, wt_matx_real, wt_matx_real1, path_final