def solution(A):
    len_A = len(A)

    # empty array
    if len_A == 0:
        print("there is no item in A")
        return 0
    else:
        num = []
        
        for i in range (0, len(A)):
            # the first number
            if i == 0:
                num.append(A[i])
            else:
                find_flag = 0
                for j in range(0, len(num)):
                    if A[i] == num[j]:
                        find_flag = 1
                        break
                if find_flag == 0:
                    num.append(A[i])

        print("the result is ", len(num))
        return len(num)
            





A = [2, 1, 1, 2, 3, 1]
A = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
solution(A)