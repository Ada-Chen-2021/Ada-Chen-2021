def solution(A):
    len_A = len(A)

    # 當 array 裡只有 3 個數字時
    # result 所有數字乘在一起
    if len_A == 3:
        result = A[0] * A[1] * A[2]
        print("the result is ", result)
        return result
        exit(0)
    
    # ---------------------------------------
    # 以下的計算方式都是 array 裡的數字超過 3 個
    positive = [0] * 1001 # store  0 ~  1000
    short_positive = []
    negative = [0] * 1001 # store -1 ~ -1000
    short_negative = []


    max = 0
    min = 0
    index = 0
    for i in A:
        if i < 0:
            negative[-i] += 1
            if  i < min:
                min = i
        elif i >= 0:
            positive[i] += 1
            if i > max:
                max = i
        index += 1


    # 將正數依小至大存進 short_positvie
    for i in range (0, (max+1)):
        if positive[i] != 0:
            if positive[i] > 1:
                for count_p in range (1, (positive[i]+1)):
                    short_positive.append(i)
            else:
                short_positive.append(i)
    
    
    # 將負數依小至大存進 short_negatvie
    for i in range (0, (-min+1)):
        if negative[i] != 0:
            if negative[i] > 1:
                for count_n in range(1, (negative[i]+1)):
                    short_negative.append(-i)
            else:
                short_negative.append(-i)
     

    # 檢查正負數是否有兩個以上
    flag_positive = 0    
    flag_nagative = 0
    result = 0
    len_short_positvie = len(short_positive)
    len_short_nagative = len(short_negative)
    
    # 檢查正數是否為兩個以上
    if  len_short_positvie >= 2:
        flag_positive = 1

    # 檢查負數是否為兩個以上
    if len_short_nagative  >= 2:
        flag_nagative = 1


    
    # 正負數都有超過 2 個的時候
    if flag_nagative == 1 and flag_positive == 1:
        # +++
        # 最大的正 * 倒數第二大的正 * 倒數第三大的正
        if len(short_positive) >= 3:
            result = short_positive[(len_short_positvie)-1] * short_positive[(len_short_positvie)-2] * short_positive[(len_short_positvie)-3]
        
        # --+
        # 最小的負 * 倒數第二小的負 * 最大的正
        tmp = short_negative[(len_short_nagative)-1] * short_negative[(len_short_nagative)-2] * short_positive[(len_short_positvie)-1]
        if tmp > result:
            result = tmp
        
        print("part 1: the result is ", result)
        return result
    
    # 負數只有 1 個或 0 個的情況下
    # 假設 array 有 4 個數字，那必定會取 3 個正數
    elif flag_positive == 1:
        if flag_nagative == 0:
            # the combine of numbers is +++
            # 最大的正 * 倒數第二大的正 * 倒數第三大的正
            #if len(short_positive) >= 3: 
            result = short_positive[(len_short_positvie)-1] * short_positive[(len_short_positvie)-2] * short_positive[(len_short_positvie)-3]
            print("part 2: the result is (+++)" , result)
            return result
            
    
    # 正數只有 1 個或 0 個的情況下
    # 假設 array 有 4 個數字
    elif flag_nagative == 1:
        if flag_positive == 0:
            # the combine of numbers is --+
            # 最小的負 * 倒數第二小的負 * 最大的正
            if len(short_positive) > 0:
                result = short_negative[(len_short_nagative)-1] * short_negative[(len_short_nagative)-2] * short_positive[(len_short_positvie)-1]
                print("part 3: the result is (--+)" , result)
                return result
            
            # 都沒有正整數的情況
            # the combine of numbers is ---
            # 最大的負 * 第二大的負 * 第三大的負 
            elif len(short_positive) == 0:
                result = short_negative[0] * short_negative[1] * short_negative[2]
                print("part 3: the result is (---)" , result)
                return result


#A = [-3, -2, 4, 5, 6]


#A = [-1, 2, 4, 5]   # part 1 +++ (40)
#A = [-10, -1, 4, 5]# part 1-1 --+ (50)
#A = [-10, -2, 4, 5] # part 1 --+ (100)
#A = [4, 7, 3, 2, 1, -3, -5] # part 1 --+ (105)

#A = [-100, 4, 2, 4]# part 2 +++

#A = [-100, -10, -1, 4] # part 3 --+ (4000)
#A = [-100, -10, -5, -2] # part 3 --- (-100)
#A = [-1000, 1, 2, 1000] (2000)
A = [-3, -2, -1, 0]
A = [-2, -2, -2, -2]


solution(A)