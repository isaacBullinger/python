grade=float(input('Please put your grade in percent: '))
print()
message='Your letter grade is: '
if grade>=90:
    letter='A'
elif grade>=80:
    letter='B'
elif grade>=70:
    letter='C'
elif grade>=60:
    letter='D'
elif grade<60:
    letter='F'
digit=grade%10
if digit>=7:
    sign='+'
elif digit<3:
   sign='-'
else:
    sign=''
if grade>=93:
    sign=''
if letter=='F':
    sign=''
print(message+letter+sign)
if grade>=70:
    print('Congratulations! You passed the course!')
else:
    print('You did not pass, you will get it next time...')