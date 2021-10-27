# 使用 stack 的特性 first in, last out 的概念
# 因為要左括與右括成一對才行，中間不能插入落單的一個左括或落單的一個右括
# if 1. 如果找到是左括號，先存入 stack_list 的 array 中
# elif 2. 如果找到的是右括號
#         |--> 如果 stack_list 的 array 中沒有任何左括號 --> 此為非法的輸出，直接跳出 for loop 並回傳 0
#         |--> 如果 stack_list 的 array 中有左括號，取出最後一個 item，檢查是否與右括號成對
#              |--> 成對，將該 itme 從 stack_list 中移除
#              |--> 不成對，此為非法的輸出，直接跳出 for loop 並回傳 0
# for loop 結束後
#          |--> 如果 stack_list 為空表示為合法 (因為成對的都會被移除)
#          |--> 如果 stack_list 不為空表示不合法

def solution(S):
    N = len(S)
    stack_list = []

    # 如果是空字串也視為 nested 
    if S == "[]":
        print("the result is 1")
        return 1
        exit()

    for index in range (0, N):
        # 如果是左側的括號就先放進 stack_list 裡
        if S[index] == "{" or S[index] == "[" or S[index] == "(":
            stack_list.append(S[index])
            index += 1
        
        # 以下邏輯都一樣
        # 如果找到的是右括號
        # 如果 stack_list 的 array 中沒有任何左括號 --> 此為非法的輸出，直接跳出 for loop 並回傳 0 (else statement)
        # 如果 stack_list 的 array 中有左括號，取出最後一個 item，檢查是否與右括號成對
        #      |--> 成對，將該 itme 從 stack_list 中移除 (if statement)
        #      |--> 不成對，此為非法的輸出，直接跳出 for loop 並回傳 0 (else statement)
        elif S[index] == "}":
            if len(stack_list) > 0 and stack_list[len(stack_list)-1] == "{":
                del stack_list[len(stack_list)-1]
            else:
                print("the result is 0")
                return 0
                break;
        
        elif S[index] == "]":
            if len(stack_list) > 0 and stack_list[len(stack_list)-1] == "[":
                del stack_list[len(stack_list)-1]
            else:
                print("the result is 0")
                return 0
                break;

        elif S[index] == ")":
            if len(stack_list) > 0 and stack_list[len(stack_list)-1] == "(":
                del stack_list[len(stack_list)-1]
            else: 
                print("the result is 0")
                return 0
                break;
                
    # 如果 stack_list 為空表示為合法 (因為成對的都會被移除)
    if len(stack_list) == 0:
        print("the result is 1")
        return 1
    # 如果 stack_list 不為空表示不合法
    else:
        print("the result is 0")
        return 0

#S = "{[()()]}"
#S = "{[)()]"
#S = []
S = ")("
#S = "{{{{"
solution(S)