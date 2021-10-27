### 每次從 A array 中抓取兩個數字去比對
### 如果兩個數字不一樣，並且數字並沒有在 tmp array 中找到就放進 tmp array
### 一樣的話就不放進 tep array
### 目前有 bug 尚未修正

import sys

def solution(A):
    num = []
    len_A = len(A)

    if (len_A % 2) == 0:
        print("stop test")
        return 0            
        sys.exit(1)
        


    for i in range(0, len_A, 2):
        len_num = len(num)
        print("the for loop is ", i)
        print("---")
        ### the last number 
        if i == (len_A-1):
            print("the last number")
            if A[i] == num[0]:
                del num[0]
            else:
                del num[1]
            
            break
        
        else:
            ### empty number
            if len_num == 0:
                ### the (i)th number is equal to (i+1)th number
                if A[i] == A[i+1]:
                    continue
                else:
                    num.append(A[i])
                    num.append(A[i+1])
                    print("empty number")
                    print("the num list :", num)
                    print("===========================")
            else:
                index_num = 0
                find_num_1 = 0 
                find_num_2 = 0
                ### the (i)th number is equal to (i+1)th number
                if A[i] == A[i+1]:
                    break
                else:
                    for n in num:
                        # if find the number: delete the number from "num" array
                        if A[i] == n:
                            del num[index_num] 
                            find_num_1 = 1
                            print("find the num1 is ", A[i])
                            print("num ", num)
                            print("num[index_num] ", num[index_num])
                            print("*************************")
                            
                            if (find_num_2 == 0) and (A[i+1] == (num[index_num])):
                                del num[index_num] 
                                find_num_2 = 1
                                print("find the num2 is ", A[i+1])
                                print("num ", num)
                                print("*************************")
                                break

                        elif A[i+1] == n:
                            del num[index_num] 
                            find_num_2 = 1
                            print("find the num2 is ", A[i+1])
                            print("num ", num)
                            print("*************************")

                            if (find_num_1 == 0) and (A[i] == (num[index_num])):
                                del num[index_num] 
                                find_num_1 = 1
                                print("find the num1 is ", A[i])
                                print("num ", num)
                                print("*************************")
                                break
                        
                        elif (find_num_1 == 1) and (find_num_2 == 1):
                            break
                        index_num += 1
                    
                    if find_num_1 == 0:
                        num.append(A[i])
                        print("append the num1 ", A[i])
                        print("num ", num)
                        print("*************************")
                    
                    if find_num_2 == 0:
                        num.append(A[i+1])
                        print("append the num1 ", A[i+1])
                        print("num ", num)
                        print("*************************")

    result = int(num[0])
    print("result : ", result)
    return result
'''
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
'''
### refrence: delete an element of array
### https://www.dotblogs.com.tw/YiruAtStudio/2021/01/13/200809


#A = [9, 3, 9, 3, 9, 7, 9]
#### 0  1  2  3  4  5   6  7  8  9  10
#A = [1, 2, 3, 4, 5, 10, 2, 3, 4, 1, 5]
A = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 9, 5, 4, 9, 6]
solution(A)
