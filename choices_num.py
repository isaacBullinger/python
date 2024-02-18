error='Invalid input!'
x=input('Type 1 or 2: ')
if x=='1':
    x=input('Type 1, 2, or 3: ')
    if x=='1':
        print('Result 1_1')
    elif x=='2':
        print('Result 1_2')
    elif x=='3':
        print('Result 1_3')
    else:
        print(error)
elif x=='2':
    x=input('Type 1 or 2: ')
    if x=='1':
        x=input('Type 1 or 2: ')
        if x=='1':
            print('Result 2_1_1')
        elif x=='2':
            print('Result 2_1_2')
        else:
            print(error)
    elif x=='2':
        print('Result 2_2')
    else:
        print(error)

error='Invalid input!'
x=input('Type A or B: ')
print(x)
if x.lower()=='a':
    x=input('Type A, B, or C: ')
    if x.lower ()=='a':
        print('Result A_A')
    elif x.lower()=='b':
        print('Result A_B')
    elif x.lower()=='c':
        print('Result A_C')
    else:
        print(error)
elif x.lower()=='b':
    x=input('Type A or B: ')
    if x.lower()=='a':
        x=input('Type A or B: ')
        if x.lower()=='a':
            print('Result B_A_A')
        elif x.lower()=='b':
            print('Result B_A_B')
        else:
            print(error)
    elif x.lower()=='b':
        print('Result B_B')
    else:
        print(error)