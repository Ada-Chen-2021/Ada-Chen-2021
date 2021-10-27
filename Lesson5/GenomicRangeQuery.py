# 基因組合是 A C G T，分別的 factor 為 1-4
# S 為 string，代表一串基因序列。長度為 N 個 ex: S = "CAGCCTA"
# P array 指的是開頭第 X 個基因，總共 M 個數字  ex: P = [2, 5, 0]
# Q array 指的是結尾第 X 個基因，總共 M 個數字  ex: Q = [4, 5, 6]
# 位置上來說 P[K] <= Q[K]
# 計算每一對 (P, Q) 中最小的 factor
# ex: (P[0], Q[0]) --> (2, 4) index 2~4 的字串為 GCC，那最小 factor 為 2
# ex: (P[1], Q[1]) --> (5, 5) index 5 的字串為 T，那最小 factor 為 4
# ex: (P[2], Q[2]) --> (0, 6) index 0~6 的字串為整串 S，那最小 factor 為 1
# result 要回傳一個 array 格式：[2, 4, 1]

import sys

def solution(S, P, Q):
   
    len_result = len(P)
    len_S = len(S)
    S_factor = []
    result = [0] * len_result

    # factor
    # A --> 1; C --> 2; G --> 3; T --> 4; 
    for i in S:
        if i == 'A':
            S_factor.append(1)
        elif i == 'C':
            S_factor.append(2)         
        elif i == 'G':
            S_factor.append(3)
        elif i == 'T': # T
            S_factor.append(4)
        else:
            sys.exit(1)


    print("S is ", S_factor)
    # the answer is S itself
    if len_S == 1:
        print("the answer is S")
        print(S_factor)
        return S_factor
        exit(0)

    else:
        # read (P, Q) pair
        for i in range (0, len_result):

            # the factor is [1-4]
            min_factor = 5
            index_start = P[i]
            index_end = Q[i]

            print("i:", i, "; index_start:", index_start, "; index_end:", index_end)
            print("===============")
            
            # find the minmum factor
            if index_start == index_end:
                result[i] = S_factor[index_start]
                print("don't need to compare")
                print("the ", i, " of result is ", int(S_factor[index_start]))
                print("result ", result)
                print("----------------------------------")
            else:
                for n in range(index_start, (index_end+1)):
                    # factor 1 是最小的，因此找到 1 後不需要繼續往下找，並且離開 for-loop
                    if S_factor[n] == 1:
                        result[i] = min_factor
                        min_factor = S_factor[n]
                        print("find the minmun and break for-loop")
                        print("the ", i, " of result is ", min_factor)
                        print("----------------------------------")
                        break
                    elif S_factor[n] < min_factor:
                        min_factor = S_factor[n]
                print("min_factor:", min_factor)
                result[i] = min_factor
                print("result ", result)

        print("end of search")
        print("the result is ", result)
        return result


S = "CAGCCTA"
P = [2, 5, 0, 3]
Q = [4, 5, 6, 5]

'''
S = "T"
P = [0]
Q = [0]
'''
solution(S, P, Q)