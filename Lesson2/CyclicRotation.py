import collections
import sys

def solution(A, K):
    ### A: input array
    ### K: times of right shift times
    num_zero_in_A = collections.Counter(A)[0]
    len_A = len(A)

    ### check the empty array
    if len_A == 0:
        #print("empty array")
        print(A)
        return A
        sys.exit(1)
    
    remainder = K % len_A

    ### the right-shifted times is 0
    ### don't rotate array A
    if K == 0:
        #print("the right-shifted times is 0")
        #print("rotate array A")
        print(A)
        return A
      
    ### there is only 0 in A
    ### don't rotate array A
    elif num_zero_in_A == len_A:
        print(A)
        return A
    
    ### don't rotate array A
    elif (K >= len_A) and (remainder == 0):
        #print("(K >= len_A) and (remainder == 0)")
        print(A)
        return A

    ### rotate array A K times
    elif K < len_A:
        #print("K < len_A")
        #print("rotate array A K times")
        result_array = [0] * len_A
        index = 0

        for item in A:
            if (index+K) >= len_A:
                pos = index + K - len_A
                result_array[pos] = item

                index += 1

            else:
                pos = index + K
                result_array[pos] = item
                index += 1
        
        print(result_array)      
        return result_array      
    
    ### K > len_A
    ### rotate array A remainder times
    else:
        #print("K > len_A")
        #print("rotate array A K times")
        #print("remainder ", remainder)
        result_array = [0] * len_A
        index = 0

        for item in A:
            if (index+remainder) >= len_A:
                pos = index + remainder - len_A
                result_array[pos] = item

                index += 1

            else:
                pos = index + remainder
                result_array[pos] = item
                index += 1
        
        print(result_array)      
        return result_array      


#A = [0] * 10
#A = []
A = [3, 8, 9, 7, 6]
solution(A, 1)
