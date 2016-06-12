print('Enter the 1st coordinate of horse\'s location')
a = input()
if a>8:
    print('DAMN! LOWER THAN 9, BASTARD!!')
    exit()
else:
    print('Enter the 2nd coordinate of horse\'s location')
    b = input()
    if b > 8:
        print('DAMN! LOWER THAN 9, BASTARD!!')
        exit()
    else:
        print('Enter the 1st coordinate of arrival point')
        q = input()
        if q > 8:
            print('DAMN! LOWER THAN 9, BASTARD!!')
            exit()
        else:
            print('Enter the 2nd coordinate of arrival point')
            w = input()
            if w > 8:
                print('DAMN! LOWER THAN 9, BASTARD!!')
                exit()
            elif a+1==q and b+2==w:
                print('Yes')
            elif a+2==2 and b+1==w:
                print('Yes')
            else:
                print('No')

