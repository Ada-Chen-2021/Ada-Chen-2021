### 使用一個 tmp array 來記錄出現過的數字
### 讀取 A array 的同時去檢查 tmp array
### 如果該數字已經存在 tmp array 就將該數字從 tmp array 中移除
### 直到最後 tmp array 會剩下一個數字

import sys

def solution(A):
    num = []
    len_A = len(A)

    if (len_A % 2) == 0:
        print("stop test")
        return 0            
        sys.exit(1)
        

    for item in A:
        len_num = len(num)
       
        ### empty number
        if len_num == 0:
            num.append(item)
            print("empty number")
            print("the num list :", num)
            print("===========================")
            
        
        else:
            index_num = 0 # stroe index nubmer
            find_num = 0 # check the number is duplicate
            for n in num:
                # if find the number: delete the number from "num" array
                if item == n:
                    del num[index_num] 
                    find_num = 1
                    print("else: find num is ", item)
                    print("num ", num)
                    print("*************************")
                    break
                
                index_num += 1

            if find_num == 0:
                num.append(item)
                print("else: append num ", item)
                print("num ", num)
                print("*************************")
    
    result = int(num[0])
    print("result : ", result)
    return result

### refrence: delete an element of array
### https://www.dotblogs.com.tw/YiruAtStudio/2021/01/13/200809


#A = [9, 3, 9, 3, 9, 7, 9]
#A = [1, 2, 3, 4, 5, 10, 2, 3, 4, 1, 5]
A = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 9, 5, 4, 9, 6]
solution(A)
