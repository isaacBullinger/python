age1=int(input('What is the age of the first rider? '))
height1=int(input('What is the height of the first rider? '))
riders=input('Is there a second rider (yes/no)? ').lower()
ride_yes='Welcome to the ride. Please be safe and have fun!'
ride_no='Sorry, you may not ride.'
if riders=='yes':
    age2=int(input('What is the age of the second rider? '))
    height2=int(input('What is the height of the second rider? '))
    # Condition 1
    if height1<36 or height2<36:
        print(ride_no)
    # Stretch 2
    elif (age1>=12 and age1<=17) or (age2>=12 and age2<=17):
        passport=input('Do you have a golden passport (yes/no)? ').lower()
    # Condition 3
        if age1>=18 or age2>=18 or passport=='yes':
            print(ride_yes)
        elif (age1>=14 and age1<=16) and (age2>=14 and age2<=16):
            print(ride_yes)
        # Stretch 1
        elif age1>=12 and age2>=12 and height1>=52 and height2>=52:
            print(ride_yes)
            # Stretch 3
        else:
            print(ride_no)
elif riders=='no':
    # Condition 2
    if height1<36:
        print(ride_no)
    # Stretch 2
    elif age1>=12 and age1<=17:
        passport=input('Do you have a golden passport (yes/no)? ').lower()
        if (age1>=18 or passport=='yes') and height1>=62:
            print(ride_yes)
        elif passport=='no':
            print(ride_no)
        else:
            print(ride_no)
    elif age1>=18 and height1>=62:
        print(ride_yes)
    else:
        print(ride_no)
else:
    print('Input wrong--try again!')