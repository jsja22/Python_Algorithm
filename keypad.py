def solution(numbers, hand):
    left =[10]
    right =[11]
    answer = ''
    for i in numbers:
        if i ==1 or i==4 or i==7:
           answer +='L'
           left.append(i)
        if i ==3 or i==6 or i==9:
           answer +='R'
           right.append(i)
        


        if i ==2 :
            if left[-1] == 1 :
                l_distance = 1
            elif left[-1] == 4:
                l_distance = 2
            elif left[-1] == 7:
                l_distance = 3
            elif left[-1] == 10:
                l_distance = 4
            elif left[-1] == 2:
                l_distance = 0
            elif left[-1] == 5:
                l_distance = 1
            elif left[-1] == 8:
                l_distance = 2
            elif left[-1] == 0:
                l_distance = 3
                
            if right[-1] == 3:
                r_distance = 1
            elif right[-1] == 6:
                r_distance = 2
            elif right[-1] == 9:
                r_distance = 3
            elif right[-1] == 11:
                r_distance = 4
            elif right[-1] == 2:
                r_distance = 0
            elif right[-1] == 5:
                r_distance = 1
            elif right[-1] == 8:
                r_distance = 2
            elif right[-1] == 0:
                r_distance = 3
                
            if l_distance>r_distance:
                answer +='R'
                right.append(i)
            elif r_distance>l_distance:
                answer +='L'
                left.append(i)
            elif l_distance ==r_distance:
                if hand =="right" :
        
                    answer +='R'
                    right.append(i)

                elif hand =="left":
                    answer +='L'
                    left.append(i)

            
        if i ==5 :
            if left[-1] == 1:
                l_distance = 2
            elif left[-1] == 4:
                l_distance = 1
            elif left[-1] == 7:
                l_distance = 2
            elif left[-1] == 10:
                l_distance = 3
            elif left[-1] == 2:
                l_distance = 1
            elif left[-1] == 5:
                l_distance = 0
            elif left[-1] == 8:
                l_distance = 1
            elif left[-1] == 0:
                l_distance = 2
                
            if right[-1] == 3:
                r_distance = 2
            elif right[-1] == 6:
                r_distance = 1
            elif right[-1] == 9:
                r_distance = 2
            elif right[-1] == 11:
                r_distance = 3
            elif right[-1] == 2:
                r_distance = 1
            elif right[-1] == 5:
                r_distance = 0
            elif right[-1] == 8:
                r_distance = 1
            elif right[-1] == 0:
                r_distance = 2
                
            if l_distance>r_distance:
                answer +='R'
                right.append(i)
            elif r_distance>l_distance:
                answer +='L'
                left.append(i)
            elif l_distance ==r_distance:
                if hand =="right" :
                    answer +='R'
                    right.append(i)

                elif hand =="left":
                    answer +='L'
                    left.append(i)


        if i ==8 :
            if left[-1] == 1:
                l_distance = 3
            elif left[-1] == 4:
                l_distance = 2
            elif left[-1] == 7:
                l_distance = 1
            elif left[-1] == 10:
                l_distance = 2
            elif left[-1] == 2:
                l_distance = 2
            elif left[-1] == 5:
                l_distance = 1
            elif left[-1] == 8:
                l_distance = 0
            elif left[-1] == 0:
                l_distance = 1
                
            if right[-1] == 3:
                r_distance = 3
            elif right[-1] == 6:
                r_distance = 2
            elif right[-1] == 9:
                r_distance = 1
            elif right[-1] == 11:
                r_distance = 2
            elif right[-1] == 2:
                r_distance = 2
            elif right[-1] == 5:
                r_distance = 1
            elif right[-1] == 8:
                r_distance = 0
            elif right[-1] == 0:
                r_distance = 1
                
            if l_distance>r_distance:
                answer +='R'
                right.append(i)

            elif r_distance>l_distance:
                answer +='L'
                left.append(i)

            elif l_distance ==r_distance:
                if hand =="right" :
                    answer +='R'
                    right.append(i)

                elif hand =="left":
                    answer +='L'
                    left.append(i)

        if i ==0 :
            if left[-1] == 1:
                l_distance = 4
            elif left[-1] == 4:
                l_distance = 3
            elif left[-1] == 7:
                l_distance = 2
            elif left[-1] == 10:
                l_distance = 1
            elif left[-1] == 2:
                l_distance = 3
            elif left[-1] == 5:
                l_distance = 2
            elif left[-1] == 8:
                l_distance = 1
            elif left[-1] == 0:
                l_distance = 0
                
            if right[-1] == 3:
                r_distance = 4
            elif right[-1] == 6:
                r_distance = 3
            elif right[-1] == 9:
                r_distance = 2
            elif right[-1] == 11:
                r_distance = 1
            elif right[-1] == 2:
                r_distance = 3
            elif right[-1] == 5:
                r_distance = 2
            elif right[-1] == 8:
                r_distance = 1
            elif right[-1] == 0:
                r_distance = 0
                
            if l_distance>r_distance:
                answer +='R'
                right.append(i)

            elif r_distance>l_distance:
                answer +='L'
                left.append(i)

            elif l_distance ==r_distance:
                if hand =="right" :
                    answer +='R'
                    right.append(i)

                elif hand =="left":
                    answer +='L'
                    left.append(i)
    print(left)               
    print(right)
    return answer




numbers =[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers,hand))