import math

def solution(i, v):
    v_max = 0
    v = sorted(v)
    for j in range(1,len(v)):
        if(v[j] - v[j-1] > v_max):
            v_max = v[j] - v[j-1]
    answer = v_max / 2
    return math.ceil(answer)

print(solution(15, [15,5,3,7,9,14,0]))
print(solution(5, [2,5]))

