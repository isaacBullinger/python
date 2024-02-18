import random

number= random.randint(1,100) #int(input('What is the magic number? '))
my_number=-1
again=True
count=0

while again==True:
    count=count+1
    my_number=int(input('What is your guess (1-100)? '))
    if number>my_number:
        print('Higher')
    elif number<my_number:
        print('Lower')
    elif my_number>100 or my_number<0:
        print('Number needs to between 1 and 100! Try again...')
    else:
        print(f'You guessed it in {count} tries!\n')
        x=input('Do you want to play again? ')
        if x=='yes':
            again=True
            count=0
            number= random.randint(1,100) #int(input('What is the magic number? '))
        elif x=='no':
            again=False
        else:
            print('Invalid input...')
            again=False