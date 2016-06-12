print('Enter the 1st coordinate of castle\'s location')
a = input()
if a>8:
    print('TYPE LOWER THAN 9, MOTHERFUCKER')
    exit()
else:
    print('Enter the 2nd coordinate of castle\'s location')
    b = input()
    if b>8:
        print('TYPE LOWER THAN 9, MOTHERFUCKER')
        exit()
    else:
        print('Enter the 1st coordinate of arrival point')
        q = input()
        if q>8:
            print('TYPE LOWER THAN 9, MOTHERFUCKER')
            exit()
        else:
            print('Enter the 2nd coordinate of arrival point')
            w = input()
            if w>8:
                print('TYPE LOWER THAN 9, MOTHERFUCKER')
                exit()
            elif a==q or b==w:
                print('Ye$$')
            else:
                print('NO.')






