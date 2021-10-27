def solution(N):
    ### transfer to binary
    binary = "{0:b}".format(N)
             
    n = int(N)
    count_1 = 0
    index = 0
    
    pos_1 = []
    gap = 0
    longest_gap = 0

    ### check the num should be positive integer 
    if n <= 0:
        return 0

    else:
        ### count number of 1
        ### log the position of 1
        for i in binary:
            if i == '1':
                pos_1.append(index)
                count_1 =  count_1 + 1
            index = index + 1
        index = 0

        ### there is no binary gap
        if count_1 == 1:
            return 0    
       
        ### there is at least one binary gap
        else:
            for i in pos_1:
                ### index: 0, 1, ... ,(len(pos_1)-1)
                ### the next item is lastest item
                if (index+1) == (len(pos_1)-1):
                    gap = pos_1[index+1] - pos_1[index] - 1
                    index = index + 1

                    if gap > longest_gap:
                        longest_gap = gap

                    break
                else:
                    ### 592 to binary is 1000010001
                    ### the index is     0123456789
                    ### the first binary gap is (5-0-1) = 4
                    ### the second binary gap is (9-5-1) = 3
                    ### "the next position of 1"  - "the current position of 1" - 1
                    gap = pos_1[index+1] - pos_1[index] - 1
                    index = index + 1

                    if gap > longest_gap:
                        longest_gap = gap
            print(longest_gap)
            return longest_gap    
                

solution(1041)
