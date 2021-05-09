import numpy as np
def solution(places):
    answer = []
    for q in range(5):
        answers = []
        test = places[q]
        plist = []

        for x in range(5):
            for y in range(5):
                if test[x][y] == "P":
                    plist.append(np.array([x,y]))
                else:
                    continue

        for i in range(len(plist)): 
            for j in range(len(plist)):
                if np.abs(plist[i]-plist[j])[0]+np.abs(plist[i]-plist[j])[1] == 1:
                    answers.append("0")
                elif np.abs(plist[i]-plist[j])[0]+np.abs(plist[i]-plist[j])[1] == 2:
                    x_dif = np.abs(plist[i]-plist[j])[0]
                    y_dif = np.abs(plist[i]-plist[j])[1]
                    if x_dif == 2:
                        mid_x = int((plist[i][0]+plist[j][0])/2)
                        mid_y = plist[i][1]
                        if test[mid_x][mid_y]=="X":
                            answers.append("1")
                        else:
                            answers.append("0")
                    elif y_dif == 2:
                        mid_x = plist[i][0]
                        mid_y = int((plist[i][1]+plist[j][1])/2)
                        if test[mid_x][mid_y]=="X":
                            answers.append("1")
                        else:
                            answers.append("0")
                    else:
                        mid_1_x = plist[i][0]
                        mid_1_y = plist[j][1]
                        mid_2_x = plist[j][0]
                        mid_2_y = plist[i][1]
                        if test[mid_1_x][mid_1_y]=="X" and test[mid_2_x][mid_2_y]=="X":
                            answers.append('1')
                        else:
                            answers.append('0')

                else:
                    answers.append("1")
        if answers.count("0") != 0 :
            answer.append(0)
        else:
            answer.append(1)
        
    return answer