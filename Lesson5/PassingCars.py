# 從後面計算數字 1 的數量
# ex:
# [0, 1, 0, 1, 1]
#    |-----------| 第一個 0 會配到 3 個 1
#           |----| 第二個 0 會配到 2 個 1
# 總排序是 3 + 2 = 5

def solution(A):
    len_A = len(A)
    counter_one = []
    current_count = 0

    # 從 array 的尾巴往前計算 1 的數量
    for i in range ((len_A-1), -1, -1):
        if A[i] == 1:
            current_count += 1
        # 目前 0 的位置右邊的 1 總數量存進 counter_one array 中
        # 例如：第二個 0 會算出有 2 個 1
        else:
            counter_one.append(current_count)
    print(counter_one)

    result = 0
    for i in counter_one:
        result += i

    # The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000
    if result > 1000000000:
        return -1
    else:
        print("the result is ", result)
        return result


A = [0, 1, 0, 1, 1]
#A = [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1]
solution(A)
