def solution(X, A):
    len_A = len(A)
    
    # the index 0 is useless
    # the index means position
    # the index 1 is postion 1
    # the N is integer within the range [1..100,000]
    # a non-empty array A consisting of N integers
    time = [1000000] * (X+1)
    
    for i in range(0, len_A):
        current_time = i
        pos = A[i]
        
        # the leaf hasn't fallen in the river
        if time[pos] == 1000000:
            time[pos] = current_time

        elif time[pos] != 0 and current_time <= time[pos]:
            time[pos] = current_time
    
    print("the position and time")

    result = 0

    # debug
    '''
    for i in range (1, len(time)):
        print("pos: ", i, "; time ", time[i])
        print("---------------------")
    '''

    for i in range (1, len(time)):     
        if time[i] == 1000000:
            print("the frog is never able to jump to the other side of the river")
            print("the result is -1")
            return -1
            break
        
        elif result <= time[i]:
            result = time[i]
    print("the result is ", result)
    return result


#A = [1, 3, 1, 4, 2, 3, 5, 4]
#A = [1, 6, 7, 3, 1, 2, 5, 6, 4]
A = [1]
solution(5, A)


