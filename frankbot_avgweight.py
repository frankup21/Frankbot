def getavg(input):
    l = eval(input)
    data = []
    index = 0
    for i in l:
        weight_added = False
        avg_added = False
        total_count = 0
        for j in i:
            if weight_added == False:
                data.append([j])
                weight_added = True
            if avg_added == False:
                data[index].append(0) #sum of grades
                data[index].append(0) #number of grades
                avg_added = True
            else:
                data[index][1] += j
                total_count += 1
        data[index][2] += total_count
        index += 1

    final_avg = 0
    for i in range(0, len(data)):
        final_avg += (data[i][1] / data[i][2]) * (data[i][0] / 100)
    return final_avg
