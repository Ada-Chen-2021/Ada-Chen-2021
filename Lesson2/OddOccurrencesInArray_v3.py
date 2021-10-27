### 使用 counting sort
### 讀取 array A 的第一個數字，開始計算該數字
### 算完後將該數字存進 array key，次數存進 array count
### 再將該數字從 array A 移除

def solution(A):
    key = []
    count = []
    
    while len(A) > 0:
        tmp_key = A[0]
        tmp_count = 0
        
        for i in range (0, len(A)):
            if tmp_key == A[i]:
                tmp_count += 1

        
        print("key is ", tmp_key, "/count is ", tmp_count)
        key.append(A[0])
        count.append(tmp_count)

        # delete the tmp_key from array A
        for i in range (0, tmp_count):
            A.remove(tmp_key)
        print(A)
        print("=====================")
    
    print(key)
    print(count)

    for i in range(0, len(count)):
        if count[i] % 2 == 1:
            result = int(key[i])
            print("the result is ", result)
            return result
            break
            

#A = [1, 1, 1, 2, 2, 3, 3]
#A = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 9, 5, 4, 9, 6]
A = [9, 3, 9, 3, 9, 7, 9]
solution(A)
