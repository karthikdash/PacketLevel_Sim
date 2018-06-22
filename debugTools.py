import numpy as np

def checkSystemResources(wt_matx, wt_matx_real, wt_matx_real1, path_final, orig_total_matx, orig_total_real1):

    total_matx = np.sum(1 / wt_matx)
    total_real = np.sum(1 / wt_matx_real)
    total_real1 = np.sum(1 / wt_matx_real1)
    k = 0
    weight_diff = 0
    realweight_diff = 0
    while path_final[k][0] != 0:
        j = 15
        while path_final[k][j] != 0 and j != 26:
            weight_diff = weight_diff + path_final[k][4]
            if path_final[k][1] == 0:
                realweight_diff = realweight_diff + path_final[k][4]
            j += 1
        weight_diff = weight_diff - path_final[k][4]
        if path_final[k][1] == 0:
            realweight_diff = realweight_diff - path_final[k][4]
        k += 1
    if (orig_total_matx - total_matx - weight_diff) > 2 or (orig_total_matx - total_matx - weight_diff) < -2:
        print "--------------- Weight matices not updated properly-----------------"
    if (orig_total_real1 - total_real1 - realweight_diff) > 2:
        print "--------------- Weight matices not updated properly-----------------"

def displayStats(blockedvoice_alog1, totalvoice, blockedvideo_algo1,
                 totalvideo, blocekednonrealtime_algo1, totalnonrealtime,
                 sum_soujorn, number_soujorn, Video_e2e, Video_e2e_Count,
                 Voice_e2e, Voice_e2e_Count, File_e2e, File_e2e_Count, scale, lamb):
    fracvoice_algo1 = float(blockedvoice_alog1 * 1.0 / totalvoice)
    fracvideo_algo1 = float(blockedvideo_algo1 * 1.0 / totalvideo)
    fracnonreal_algo1 = float(blocekednonrealtime_algo1 * 1.0 / totalnonrealtime)
    sj_time = sum_soujorn / number_soujorn * 1.0
    video_endtoend = (Video_e2e / (scale)) / Video_e2e_Count
    voice_endtoend = (Voice_e2e / (scale)) / Voice_e2e_Count
    file_endtoend = (File_e2e / (scale)) / File_e2e_Count
    print lamb, fracvoice_algo1, fracvideo_algo1, fracnonreal_algo1, voice_endtoend, video_endtoend, file_endtoend, sj_time

def makeCSV(blockedvoice_alog1, totalvoice, blockedvideo_algo1,
                 totalvideo, blocekednonrealtime_algo1, totalnonrealtime,
                 sum_soujorn, number_soujorn, Video_e2e, Video_e2e_Count,
                 Voice_e2e, Voice_e2e_Count, File_e2e, File_e2e_Count, scale, lamb):
    fracvoice_algo1 = float(blockedvoice_alog1 * 1.0 / totalvoice)
    fracvideo_algo1 = float(blockedvideo_algo1 * 1.0 / totalvideo)
    fracnonreal_algo1 = float(blocekednonrealtime_algo1 * 1.0 / totalnonrealtime)
    sj_time = sum_soujorn / number_soujorn * 1.0
    video_endtoend = (Video_e2e / (scale)) / Video_e2e_Count
    voice_endtoend = (Voice_e2e / (scale)) / Voice_e2e_Count
    file_endtoend = (File_e2e / (scale)) / File_e2e_Count
    np.savetxt("resultsHetero" + str(lamb) + ".csv", np.array([[lamb, fracvoice_algo1,
                                                                fracvideo_algo1, fracnonreal_algo1, sj_time,
                                                                voice_endtoend, video_endtoend, file_endtoend
                                                                ]]), delimiter=",")
    print "Success"
