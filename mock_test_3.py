import random

def solution(board, nums):
    for i in range(len(board)):
        for j in range(len(board)):
            for k in range(len(nums)):
                if(board[i][j] == nums[k]):
                    board[i][j] = "a"

    bingo = 0
    cross_cnt1 = 0
    cross_cnt2 = 0
    for i in range(len(board)):
        cal_cnt=0
        row_cnt=0
        for j in range(len(board)):
            if(board[i][j] == "a"):
                row_cnt += 1
            if(board[i][j] == "a"):
                cal_cnt += 1
            if(i == j and board[i][j] == "a"):
                cross_cnt1 += 1
            if((i+j==len(board)-1) and board[i][j] == "a"):
                cross_cnt2 += 1
        if(row_cnt == len(board)):
            bingo += 1
        if(cal_cnt == len(board)):
            bingo += 1
    if(cross_cnt1 == len(board)):
        bingo += 1
    if(cross_cnt2 == len(board)):
        bingo += 1
    
    return bingo


print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [13,1,2,14,16,4,5,11,15]))
print(solution([[6,15,17,14,23], [5,12,16,13,25], [21,4,2,1,22] ,[10,20,3,18,8], [11,9,19,24,7]], [15,5,12,16,13,25,4,2,10,20,18,9,7]))