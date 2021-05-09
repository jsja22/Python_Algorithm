import re
def solution(s):
    answer =0
    text = s
    number_s = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    number_i = ["0","1","2","3","4","5","6","7","8","9"]

    for i in range(10):
        a = text.replace(number_s[i],number_i[i])
        text = a
        answer = text
    answer = int(answer)

    return answer