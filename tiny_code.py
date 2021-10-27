'''
A = [1, 2, 3, 4, 5]

len = len(A)

for i in range(0, len, 2):
    print(i)

for i in range(0, 4):
    print(i)

'''

def outer(A):
    t = A
    print("A ", A)
    def inner():
        B = 1
        R = t + B
        print("R", R)
        return R
    inner()

tmp = outer(10)
print(tmp)

