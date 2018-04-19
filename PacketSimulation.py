from PacketTools import *

def packetSimulation(min_arrivaltime, noOfNodes, B, C, packet_size, path_final, nodes_real, node_links , time_service, Voice_e2e, Voice_e2e_Count,
                     Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                     wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, scale, nodes_nonreal,
                     sum_soujorn, number_soujorn, allLinks):
    if True:
        for node_no in range(1, noOfNodes + 1, 1):
            for next_nodeno in range(0, len(node_links[node_no]), 1):
                # if len(nodes_real[(node_no, node_links[node_no][next_nodeno])]) > 0 and len(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])]) > 0:
                #     nodes_slot_unused[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1
                #     nodes_slot_total[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1
                if len(nodes_real[(node_no, node_links[node_no][next_nodeno])]) > 0:
                    # nodes_slot_used[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1
                    # nodes_slot_total[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1

                    s_link = int(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[0])
                    d_link = int(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[1])
                    # if nodes_real[(node_no, node_links[node_no][next_nodeno])][0].arrival_time <= time_service and B[s_link - 1][d_link - 1] == 8:
                    if B[s_link - 1][d_link - 1] == 8 or allLinks:
                        if len(nodes_real[(node_no, node_links[node_no][next_nodeno])]) == 0:
                            continue  # Continue checking other nodes for servicable packets
                        s_link = int(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[0])
                        d_link = int(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[1])
                        link_retransmit_prob = np.random.choice(np.arange(0, 2), p=[1 - C[s_link - 1][d_link - 1], C[s_link - 1][d_link - 1]])
                        # link_retransmit_prob = 1
                        for packetno in range(0, len(nodes_real[(node_no, node_links[node_no][next_nodeno])]), 1):
                            nodes_real[(node_no, node_links[node_no][next_nodeno])][packetno].addSlotDelay(packet_size / 80000)

                        # nodes_slot_queue_real_len[node_no - 1][node_links[node_no][next_nodeno] - 1] += len(nodes_real[(node_no, node_links[node_no][next_nodeno])])
                        nodes_real[(node_no, node_links[node_no][next_nodeno])][0].service(
                            max(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].arrival_time, time_service),
                            B[s_link - 1][d_link - 1], False, link_retransmit_prob,
                            packet_size / 80000)

                        if link_retransmit_prob == 1:
                            # Appending to the next node receiving Queue
                            if nodes_real[(node_no, node_links[node_no][next_nodeno])][0].d_new == 99:
                                cur_connection_type = nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_tag
                                if nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_tag == 0:
                                    ################### Decrementing the packet count from path_final ############
                                    if nodes_real[(node_no, node_links[node_no][next_nodeno])][0].direction == True:
                                        # path_final[nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flownumber ][2] -= 1
                                        path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type = \
                                            removeFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
                                                       Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                                                       wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, cur_connection_type)
                                    else:
                                        path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type = \
                                            removeReverseFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
                                                              Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                                                              wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, cur_connection_type)
                                else:
                                    ################### Decrementing the packet count from path_final ############
                                    if nodes_real[(node_no, node_links[node_no][next_nodeno])][0].direction == True:
                                        path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type = \
                                            removeFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
                                                       Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                                                       wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, cur_connection_type)
                                    else:
                                        path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count, Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, connection_type = \
                                            removeReverseFlow(path_final, nodes_real, node_no, node_links, next_nodeno, time_service, Voice_e2e, Voice_e2e_Count,
                                                              Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,
                                                              wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, cur_connection_type)

                            else:
                                # nodes_real[str(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].d_new)].append(nodes_real[(node_no, node_links[node_no][next_nodeno])][0])
                                # nodes_real[str(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].d_new)].append(Packets(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].initial_arrival_time, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].service_end_time, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_duration, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_tag, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flownumber))
                                # nodes_total_real_packets[nodes_real[(node_no, node_links[node_no][next_nodeno])][0].d_new-1][nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[1]-1] += 1
                                bisect.insort_left(nodes_real[(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].d_new, nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path[1])],
                                                   Packets(nodes_real[(node_no, node_links[node_no][next_nodeno])][0].initial_arrival_time,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].service_end_time,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_duration,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flow_tag,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].path,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].flownumber,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].noofpackets,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].direction,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].node_service_rate,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].total_slot_time,
                                                           nodes_real[(node_no, node_links[node_no][next_nodeno])][0].total_slots,
                                                           False))
                            nodes_real[(node_no, node_links[node_no][next_nodeno])].pop(0)
                else:
                    # for i in range(0, int(node_service_rate/packet_size) - 1, 1):
                    if dataPacketsAvailable(node_no, node_links[node_no][next_nodeno], nodes_nonreal):
                        current_nr_index = 0
                        current_nr_index = currentNonrealQueue(node_no, node_links[node_no][next_nodeno], nodes_nonreal)
                        # nodes_slot_used[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1
                        # nodes_slot_total[node_no - 1][node_links[node_no][next_nodeno] - 1] += 1

                        # if nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][0].arrival_time <= time_service and B[s_link - 1][d_link - 1] == 8:
                        s_link = int(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].path[0])
                        d_link = int(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].path[1])
                        if B[s_link - 1][d_link - 1] == 8 or allLinks:
                            if nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].flow_tag == 2:

                                # Servicing for each individual node
                                if len(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])]) == 0:
                                    continue  # Continue for other servicable nodes

                                s_link = int(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].path[0])
                                d_link = int(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].path[1])
                                link_retransmit_prob = np.random.choice(np.arange(0, 2), p=[1 - C[s_link - 1][d_link - 1], C[s_link - 1][d_link - 1]])

                                if node_no == 8 and node_links[node_no][next_nodeno] == 13:
                                    if nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].arrival_time > time_service:
                                        link_retransmit_prob = 0
                                if B[s_link - 1][d_link - 1] == 0:
                                    print "Inf"

                                nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].service(
                                    max(nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].arrival_time, time_service), B[s_link - 1][d_link - 1],
                                    False, link_retransmit_prob, packet_size / (8000000 / scale))
                                # Appending to the next node receiving Queue
                                if link_retransmit_prob == 1:
                                    if nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][
                                        0].d_new == 99:  # If packet reached destination we add to the end-to-end final tracker
                                        ################### Decrementing the packet count from path_final ############
                                        k = 0
                                        if nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index][0].direction == True:
                                            path_final, nodes_nonreal, node_no, node_links, next_nodeno, time_service, File_e2e, sum_soujorn, number_soujorn, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, current_nr_index, wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1 = \
                                                removeFileFlow(path_final, nodes_nonreal, node_no, node_links, next_nodeno, time_service, File_e2e, sum_soujorn, number_soujorn,
                                                               File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority, current_nr_index,
                                                               wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1)
                                    else:
                                        nodes_nonreal = appendNonRealQueue(node_no, node_links[node_no][next_nodeno], current_nr_index, current_nr_index, nodes_nonreal, time_service)
                                    nodes_nonreal[(node_no, node_links[node_no][next_nodeno])][current_nr_index].pop(0)
    time_service = time_service + packet_size / 80000
    return min_arrivaltime, noOfNodes, B, C, packet_size, path_final, nodes_real, node_links, time_service, Voice_e2e, Voice_e2e_Count,\
           Video_e2e, Video_e2e_Count, File_e2e, File_e2e_Count, p, s, d, flow_type, min_rate, flownumber, userpriority,\
           wt_matx, wt_matx_real, wt_matx_real1, blockstate, orig_total_matx, orig_total_real1, scale, nodes_nonreal, sum_soujorn, number_soujorn