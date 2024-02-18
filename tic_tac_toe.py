import random

choice = ''
computer_choice = ''
display = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
draw = False
user_points = []
computer_points = []
number = int()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
guide = '_|_|_    1|2|3\n_|_|_    4|5|6\n | |     7|8|9'
user_point = int()
computer_point = int()
winner = ''

def print_board(display):
    print(display[0]+'|'+display[1]+'|'+display[2]+'    1|2|3')
    print('-----    -----')
    print(display[3]+'|'+display[4]+'|'+display[5]+'    4|5|6')
    print('-----    -----')
    print(display[6]+'|'+display[7]+'|'+display[8]+'    7|8|9')

def check_all(display):
    global winner
    if display[0] == display[1] == display[2] and display[0] != ' ':
        winner = display[0]
    elif display[3] == display[4] == display[5] and display[3] != ' ':
        winner = display[3]
    elif display[6] == display[7] == display[8] and display[6] != ' ':
        winner = display[6]
    elif display[0] == display[3] == display[6] and display[0] != ' ':
        winner = display[0]
    elif display[1] == display[4] == display[7] and display[1] != ' ':
        winner = display[1]
    elif display[2] == display[5] == display[8] and display[2] != ' ':
        winner = display[2]
    elif display[0] == display[4] == display[8] and display[0] != ' ':
        winner = display[0]
    elif display[2] == display[4] == display[6] and display[0] != ' ':
        winner = display[2]

print('Welcome to tic-tac-toe!')
print(guide)

while user_point != 'quit' and len(computer_points) < 5 and winner == '' and draw == False:

    while choice == '' or (choice != 'x' and choice != 'o'):
        choice = input('Choose x or o: ')
        if choice == 'x':
            computer_choice = 'o'
        else:
            computer_choice = 'x'

    user_point = int(input('Please select where (1-9): '))
    while user_point == computer_point or user_point in computer_points or computer_point in user_points:
        user_point = int(input('Please select where (1-9): '))

    user_points.append(user_point)

    for number in numbers:
        if user_point == number:
            display[number - 1] = choice

    if len(user_points) >= 5:
        draw = True
        winner = 'draw'
        print_board(display)
        check_all(display)

    if draw == False:
        if len(computer_points) < 5:
            computer_point = random.randint(1, 9)

        if len(computer_points) < 5:
            while user_point == computer_point or computer_point in computer_points or computer_point in user_points:
                computer_point = random.randint(1, 9)

        if len(computer_points) < 5:
            computer_points.append(computer_point)

        for number in numbers:
            if computer_point == number:
                display[number - 1] = computer_choice
    print()
    print_board(display)
    check_all(display)

if (choice == 'x' and winner == 'x') or (choice == 'o' and winner == 'o'):
    who_won = 'user'
    who_chose = choice
elif (computer_choice == 'x' and winner == 'x') or (computer_choice == 'o' and winner == 'o'):
    who_won = 'computer'
    who_chose = computer_choice
else:
    who_won = 'draw'
    who_chose = 'no one'
if winner != 'draw':
    print(f'\nThe winner is {who_won} who chose {who_chose}!')
else:
    print(f'{who_chose.capitalize()} won, it is a {who_won}...')