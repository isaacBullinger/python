msg1='Please type a positive number: '
msg2='May I have a piece of candy? '
number=input(msg1)
candy='no'

while number < '0':
    print('Sorry, that is a negative number. Please try again.')
    number=input(msg1)
print('The number is: '+number)

while candy=='no':
    candy=input(msg2)
print('Thank you.')