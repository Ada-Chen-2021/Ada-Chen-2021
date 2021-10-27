import sys
import math

def solution(X, Y, D):
    
    if (X < 1) or (Y < 1) or (D < 1):
        return  0
        sys.exit(1)
    
    if X > Y:
        return  0
        sys.exit(1)

    # the frog doesn't need to jump
    if X == Y:
        print("the result is 0")
        return 0

    # the frog jumps
    else:
        distance = Y - X
        quotient = distance / D
        remainder = distance % D
        print("distance ", distance, "; quotient ", quotient, "; remainder ", remainder)
        
        if remainder > 0:
            result = math.ceil(quotient)
        else:
            result = int(quotient)
        
        print("the result is :", result)
        return result


    
### math fuction
### https://dotblogs.azurewebsites.net/YiruAtStudio/2021/03/13/153157

solution(10, 85, 10)