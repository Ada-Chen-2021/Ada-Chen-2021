def solution(N, A):
    current_max = 0
    counter = [0] * N

    for i in A:
        # all counters are set to the maximum value
        if i == (N+1):
            print("the max counter!!")
            counter = [current_max] * N
            print(counter)
        else:
            counter[i-1] += 1
            if counter[i-1] > current_max:
                current_max = counter[i-1]
                print("the currenct counter is changed. ", current_max)
    
    print("the result is ", counter)
    return counter


#A = [3, 4, 4, 6, 1, 4, 4]
A = [2, 1]
solution(1, A)