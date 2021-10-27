def solution(A):
    len_A = len(A)

    # the interger within the range [1,...,(N+1)]
    # ex: lenght of array is 1
    #     the interger within the range [1-2]
    # the index 0 is useless
    # the integer 1 is stored into index 1
    len_key = len_A +2
    key = [0] * len_key
    
    # store the number into key array
    # if the number is exist --> the value is 1
    for i in A:
        key[i] = 1
    
    for i in range (1, len_key):
        # the current number is not exist
        if key[i] == 0:
            result = i
            print("the result is ", i)
            return result
            break


#A = [1]
#A = [2]
#A = []
A = [1, 2, 5, 4]
solution(A)
