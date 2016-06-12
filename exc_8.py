from math import sqrt
print('Enter 1st side of triangle')
a = input()
if a>1000:
    print('Enter another side lower than 1000!')
    a = input()
if a>1000:
    print('RESTART THE PROGRAM AND WRITE THE CORRECT SIDE, BITCH!')
    exit()
else: print('Enter 2nd side of triangle')
b = input()
if b>1000:
        print('Enter another side lower than 1000!')
        b = input()
if b > 1000:
        print('RESTART THE PROGRAM AND WRITE THE CORRECT SIDE, BITCH!')
        exit()
c = sqrt(a**2+b**2)
print('3rd side of triangle is '+str(c))