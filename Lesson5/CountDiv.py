# 將頭尾的數字變成 K 可以整除的數字後再去計算 i 的數量
# 如果 A < K，first_number 則直接為 K
# 如果 A > K，並且 A 不能被 K 整除，first_number 會加上 (K-remainder) 變成 K 可以整除的數字


import math

def solution(A, B, K):
    
    if A == B:
        if A % K == 0:
            print("A == B; the result is 1")
            return 1
        else:
            print("A == B; the result is 0")
            return 0

    elif K == 1:
            result = B - A + 1
            print("K == 1; the result is", result)
            return result
    
    else:
        remainder_A = A % K
        remainder_B = B % K
        
        if remainder_A != 0:
            # ex: A = 11, K = 17
            if A < K:
                fisrt_number = K
            else:
                fisrt_number = A + (K - remainder_A)
            print(A, " A ", remainder_A, "   ", fisrt_number)
        else:
            fisrt_number = A

        if remainder_B != 0:
            last_number = B - remainder_B
            print(B, " B ", remainder_B, "   ", last_number)
        else:
            last_number = B
        
        quotient = (last_number - fisrt_number)/K
        result = math.floor(quotient) + 1
        print("A != B; the result is", result)
        return result

#solution(6, 11, 2)
#solution(6, 12, 2)
#solution(11, 345, 17)
#solution(0, 2000000000, 1)
solution(5, 20, 3)
