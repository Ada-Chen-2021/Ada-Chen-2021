def solution(A, B):
    index = 0
    #for i in range (0, 5):
    while(1):
        N = len(A) # the number of fish is [0 ~ N-1]
        print("N:", N)
    
        #print("i:", i ,"; index:", index)
        print("index :", index)

        if B[index] == 0:
            # 檢查這條魚是不是最後一條
            if index != (N-1):
                index += 1
                print("----------------------------------")
                continue

        
        if B[index] == 1:
            # 檢查這條魚是不是最後一條，但下一條魚是往上游
            if index != (N-1) and B[index+1] == 0:
                # 「目前要往下的魚」比「下一條往上魚」大
                # 下一條魚被吃掉，因此將他從 array A 與 array B 中移除
                if A[index] > A[index+1]:
                    del A[index+1]
                    del B[index+1]
                    print("del next: ", A)
                    print("----------------------------------")
                
                # 「目前要往下的魚」比「下一條往上魚」小
                # 目前這條魚要被吃掉，因此將他從 array A 與 array B 中移除
                elif A[index] < A[index+1]:
                    del A[index]
                    del B[index]
                    index -= 1
                    print("del current: ", A)
                    print("----------------------------------")
            
            # 檢查這條魚是不是最後一條，且下一條魚是往上游
            elif index != (N-1) and B[index+1] == 1:
                index += 1
        print("----------------------------------")
        


        if index >= (N-1):
            print("the result of A ", A)
            print("the result of B ", B)
            result = N
            print("the result is ", N)
            return result
            break

        


#A = [4, 3, 2, 1, 5] # example
#B = [0, 1, 0, 0, 0]
A = [4, 3, 2, 1, 5, 6, 7, 9]
B = [0, 1, 0, 0, 0, 1, 1, 0]
solution(A, B)
