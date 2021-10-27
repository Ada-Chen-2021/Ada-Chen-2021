def solution(S):
    N = len(S)
    stack_list = []
    flag_nested = -1

    if S == "[]":
        print("the result is 1")
        return 1
        exit()

    for index in range (0, N):
        if S[index] == "{" or S[index] == "[" or S[index] == "(":
            stack_list.append(S[index])
            index += 1
        
        elif S[index] == "}":
            if stack_list[len(stack_list)-1] == "{":
                #print("if } :", stack_list[len(stack_list)-1])
                #print("----------------------")
                del stack_list[len(stack_list)-1]
            else:
                flag_nested = 0
                #print("if } :", stack_list[len(stack_list)-1])
                print("the result is 0")
                return 0
                break;
        
        elif S[index] == "]":
            if stack_list[len(stack_list)-1] == "[":
                #print("if ] :", stack_list[len(stack_list)-1])
                #print("----------------------")
                del stack_list[len(stack_list)-1]
            else:
                flag_nested = 0
                #print("if ] :", stack_list[len(stack_list)-1])
                print("the result is 0")
                return 0
                break;

        elif S[index] == ")":
            if stack_list[len(stack_list)-1] == "(":
                #print("if ) :", stack_list[len(stack_list)-1])
                #print("----------------------")
                del stack_list[len(stack_list)-1]
            else: 
                flag_nested = 0
                #print("if ) :", stack_list[len(stack_list)-1])
                print("the result is 0")
                return 0
                break;
                

    if flag_nested == -1:
        print("the result is 1")
        return 1

#S = "{[()()]}"
#S = "{[)()]"
#S = []
S = ")("
solution(S)