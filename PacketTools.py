import numpy as np
import bisect
from Packets import Packets
from updateonexit import releaseResources
from debugTools import checkSystemResources
# Function to check if a particular node has packets

def nodesHavePackets(noOfNodes, node_links, nodes_real, nodes_nonreal):
    for no in range(1, noOfNodes + 1, 1):
        for nextnode in range(0, len(node_links[no]), 1):
            if len(nodes_real[(no, node_links[no][nextnode])]) != 0:
                return True
            for ii in range(0, len(nodes_nonreal[(no, node_links[no][nextnode])])):
                if len(nodes_nonreal[(no, node_links[no][nextnode])][ii]) != 0:
                    return True
    return False

# Function to check if a particular node has realtime packets

def realnodesHavePackets(noOfNodes, node_links, nodes_real):
    for no in range(1, noOfNodes + 1, 1):
        for nextnode in range(0, len(node_links[no]), 1):
            if len(nodes_real[(no, node_links[no][nextnode])]) != 0:
                return True
    return False

# Function to check if a particular node has nonrealtme packets
def nonrealnodesHavePackets(noOfNodes, node_links, nodes_nonreal):
    for no in range(1, noOfNodes + 1, 1):
        for nextnode in range(0, len(node_links[no]), 1):
            for ii in range(0, len(nodes_nonreal[(no, node_links[no][nextnode])])):
                if len(nodes_nonreal[(no, node_links[no][nextnode])][ii]) != 0:
                    return True
    return False

def dataPacketsAvailable(source, dest, nodes_nonreal):
    for ii in range(1, len(nodes_nonreal[(source, dest)])):
        if len(nodes_nonreal[(source, dest)][ii]) != 0:
            return True
    return False

def currentNonrealQueue(source, dest, nodes_nonreal):
    no_of_active = 0
    active_indices = []
    inde = 0
    for ii in range(1, len(nodes_nonreal[(source, dest)])):
        if len(nodes_nonreal[(source, dest)][ii]) != 0:
            no_of_active += 1
            active_indices.append(ii)
    return np.random.choice(active_indices)


def appendNonRealQueue(source, dest, inde, current_nr_index, nodes_nonreal, time_service):
    flag = 1
    for jj in range(1, len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])])):
        if len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj]) != 0:
            if nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj][0].flownumber == \
                    nodes_nonreal[(source, dest)][current_nr_index][0].flownumber:
                if nodes_nonreal[(source, dest)][current_nr_index][0].d_new == 8 and nodes_nonreal[(source, dest)][inde][0].path[1] == 13:
                    init_arrival_time_add = 25  # adding 250 ms (250 ms * 100 because of scale factor) propogation delay for satellite
                else:
                    init_arrival_time_add = 0
                if nodes_nonreal[(source, dest)][inde][0].addedAtSource:
                    timeToBeAdded = time_service
                else:
                    timeToBeAdded = nodes_nonreal[(source, dest)][inde][0].noofpackets
                bisect.insort_left(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj],
                                   Packets(nodes_nonreal[(source, dest)][inde][0].initial_arrival_time,
                                           nodes_nonreal[(source, dest)][inde][0].service_end_time + init_arrival_time_add,
                                           nodes_nonreal[(source, dest)][inde][0].flow_duration,
                                           nodes_nonreal[(source, dest)][inde][0].flow_tag,
                                           nodes_nonreal[(source, dest)][inde][0].path,
                                           nodes_nonreal[(source, dest)][inde][0].flownumber,
                                           timeToBeAdded,
                                           nodes_nonreal[(source, dest)][inde][0].direction,
                                           nodes_nonreal[(source, dest)][inde][0].node_service_rate,
                                           nodes_nonreal[(source, dest)][inde][0].total_slot_time,
                                           nodes_nonreal[(source, dest)][inde][0].total_slots,
                                           False))
                return nodes_nonreal
            # else:
            #     if len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj + 1]) == 0:
            #         bisect.insort_left(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj+1],
            #                            Packets(nodes_nonreal[(source, dest)][inde][0].initial_arrival_time,
            #                                    nodes_nonreal[(source, dest)][inde][0].service_end_time,
            #                                    nodes_nonreal[(source, dest)][inde][0].flow_duration,
            #                                    nodes_nonreal[(source, dest)][inde][0].flow_tag,
            #                                    nodes_nonreal[(source, dest)][inde][0].path,
            #                                    nodes_nonreal[(source, dest)][inde][0].flownumber,
            #                                    nodes_nonreal[(source, dest)][inde][0].noofpackets,
            #                                    nodes_nonreal[(source, dest)][inde][0].direction,
            #                                    nodes_nonreal[(source, dest)][inde][0].node_service_rate,
            #                                    nodes_nonreal[(source, dest)][inde][0].total_slot_time,
            #                                    nodes_nonreal[(source, dest)][inde][0].total_slots))
            #        break
            flag = 0
    if flag == 1:
        for jj in range(1, len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])])):
            if len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj]) == 0:
                if nodes_nonreal[(source, dest)][current_nr_index][0].d_new == 8 and nodes_nonreal[(source, dest)][inde][0].path[1] == 13:
                    init_arrival_time_add = 25  # adding 250 ms (250 ms * 100 because of scale factor) propogation delay for satellite
                else:
                    init_arrival_time_add = 0
                if nodes_nonreal[(source, dest)][inde][0].addedAtSource:
                    timeToBeAdded = time_service
                else:
                    timeToBeAdded = nodes_nonreal[(source, dest)][inde][0].noofpackets
                bisect.insort_left(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj],
                                   Packets(nodes_nonreal[(source, dest)][inde][0].initial_arrival_time,
                                           nodes_nonreal[(source, dest)][inde][0].service_end_time + init_arrival_time_add,
                                           nodes_nonreal[(source, dest)][inde][0].flow_duration,
                                           nodes_nonreal[(source, dest)][inde][0].flow_tag,
                                           nodes_nonreal[(source, dest)][inde][0].path,
                                           nodes_nonreal[(source, dest)][inde][0].flownumber,
                                           timeToBeAdded,
                                           nodes_nonreal[(source, dest)][inde][0].direction,
                                           nodes_nonreal[(source, dest)][inde][0].node_service_rate,
                                           nodes_nonreal[(source, dest)][inde][0].total_slot_time,
                                           nodes_nonreal[(source, dest)][inde][0].total_slots,
                                           False))
                return nodes_nonreal
    # print "nononon"
    for jj in range(1, len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])])):
        if len(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj]) == 0:
            if nodes_nonreal[(source, dest)][current_nr_index][0].d_new == 8 and nodes_nonreal[(source, dest)][inde][0].path[1] == 13:
                init_arrival_time_add = 25  # adding 250 ms (250 ms * 100 because of scale factor) propogation delay for satellite
            else:
                init_arrival_time_add = 0
            if nodes_nonreal[(source, dest)][inde][0].addedAtSource:
                timeToBeAdded = time_service
            else:
                timeToBeAdded = nodes_nonreal[(source, dest)][inde][0].noofpackets
            bisect.insort_left(nodes_nonreal[(nodes_nonreal[(source, dest)][current_nr_index][0].d_new, nodes_nonreal[(source, dest)][inde][0].path[1])][jj],
                               Packets(nodes_nonreal[(source, dest)][inde][0].initial_arrival_time,
                                       nodes_nonreal[(source, dest)][inde][0].service_end_time + init_arrival_time_add,
                                       nodes_nonreal[(source, dest)][inde][0].flow_duration,
                                       nodes_nonreal[(source, dest)][inde][0].flow_tag,
                                       nodes_nonreal[(source, dest)][inde][0].path,
                                       nodes_nonreal[(source, dest)][inde][0].flownumber,
                                       timeToBeAdded,
                                       nodes_nonreal[(source, dest)][inde][0].direction,
                                       nodes_nonreal[(source, dest)][inde][0].node_service_rate,
                                       nodes_nonreal[(source, dest)][inde][0].total_slot_time,
                                       nodes_nonreal[(source, dest)][inde][0].total_slots,
                                       False))
            return nodes_nonreal

def removeFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
               Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
               wt_matx, wt_matx_real,
               wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type):
    k = 0

    while path_final[k][0] != 0:
        if path_final[k][0] == nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flownumber:
            path_final[k][2] -= 1
            # path_final[k][9] = (path_final[k][9] + nodes_real[(node_no, node_links[node_no][next_nodeno])][0].total_slot_time) / 2.0
            path_final[k][13] += time_service - nodes_real[(node_no, node_links[node_no][next_nodeno])][0].initial_arrival_time
            path_final[k][14] += 1

            if path_final[k][2] < 1:
                if connection_type == 0:
                    Voice_e2e += path_final[k][13]/path_final[k][14]
                    Voice_e2e_Count += 1
                elif connection_type == 1:
                    Video_e2e += path_final[k][13]/path_final[k][14]
                    Video_e2e_Count += 1
                if True:
                    s, d, min_rate, flow_type, flownumber,\
                    userpriority, blockstate, path_final,\
                    wt_matx, wt_matx_real, wt_matx_real1 = releaseResources(p, s, d, flow_type, min_rate, flownumber,
                                                                            userpriority, path_final[k][0], path_final,
                                                                            wt_matx, wt_matx_real, wt_matx_real1, blockstate)
                    # Debugging
                    checkSystemResources(wt_matx, wt_matx_real, wt_matx_real1, path_final, orig_total_matx, orig_total_real1)
                    return path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type
        k += 1
    return path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type


def removeReverseFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
                      Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                      wt_matx, wt_matx_real,
                      wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type):
    k = 0
    while path_final[k][0] != 0:
        if path_final[k][0] == nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flownumber:
            path_final[k + 1][2] -= 1
            # path_final[k + 1][9] = (path_final[k + 1][9] + nodes_real[(node_no, node_links[node_no][next_nodeno])][0].total_slot_time) / 2.0
            path_final[k+1][13] += time_service - nodes_real[(node_no, node_links[node_no][next_nodeno])][0].initial_arrival_time
            path_final[k+1][14] += 1
            if path_final[k + 1][2] < 1:
                if connection_type == 0:
                    Voice_e2e += path_final[k+1][13]/path_final[k+1][14]
                    Voice_e2e_Count += 1
                elif connection_type == 1:
                    Video_e2e += path_final[k+1][13]/path_final[k+1][14]
                    Video_e2e_Count += 1
                if True:
                    s, d, min_rate, flow_type, flownumber, \
                    userpriority, blockstate, path_final, \
                    wt_matx, wt_matx_real, wt_matx_real1 = releaseResources(p, s, d, flow_type, min_rate, flownumber,
                                                                            userpriority, path_final[k][0], path_final,
                                                                            wt_matx, wt_matx_real, wt_matx_real1, blockstate)

                    # Debugging
                    checkSystemResources(wt_matx, wt_matx_real, wt_matx_real1, path_final, orig_total_matx, orig_total_real1)
                    return path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type
        k += 1
    return path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type

def removeFileFlow(path_final, nodes_nonreal, node_no, node_links, next_nodeno, time_service, File_e2e, sum_soujorn, number_soujorn,
                   File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, current_nr_index,
                   wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1):
    k = 0
    while path_final[k][0] != 0:
        if path_final[k][0] == nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].flownumber:
            path_final[k][2] -= 1
            path_final[k][13] += time_service - nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].noofpackets
            path_final[k][14] += 1

            if path_final[k][2] < 1:
                sum_soujorn += path_final[k][13]/path_final[k][14]
                number_soujorn += 1

                File_e2e += time_service - nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].noofpackets
                File_e2e_Count += 1

                s, d, min_rate, flow_type, flownumber, \
                userpriority, blockstate, path_final, \
                wt_matx, wt_matx_real, wt_matx_real1 = releaseResources(p, s, d, flow_type, min_rate, flownumber,
                                                                        userpriority, path_final[k][0], path_final,
                                                                        wt_matx, wt_matx_real, wt_matx_real1, blockstate)

                # Debugging
                checkSystemResources(wt_matx, wt_matx_real, wt_matx_real1, path_final, orig_total_matx, orig_total_real1)
                return path_final, nodes_nonreal, node_no, node_links, next_nodeno, time_service, File_e2e, sum_soujorn, number_soujorn, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, current_nr_index, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1
        k += 1
    return path_final, nodes_nonreal, node_no, node_links, next_nodeno, time_service, File_e2e, sum_soujorn, number_soujorn, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, current_nr_index, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1