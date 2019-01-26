def solution(arrA, arrB):
    answer = True
    for i in arrA:
        if(i not in arrB):
            answer = False
    
    for i in range(len(arrA)):
        temp = arrA[len(arrA)-1]
        for i in range(1,len(arrA)):
                arrA[i] = arrA[i-1]
        arrA[0] = temp
        if(arrA == arrB):
            answer = True

    return answer