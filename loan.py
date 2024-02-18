print('Rate these questions 1-10: \n')
size=int(input('How large is the loan? '))
history=int(input('How good is your credit history? '))
income=int(input('How high is your income? '))
down_payment=int(input('How large is your down payment? '))
yes='YES!'
no='NO!'
loan = False
decision='The decision is: '
if size>=5:
    if history>=7 and income>=7:
        loan = True
    elif history>=7 or income>=7:
        if down_payment>=5:
            loan = True
        else:
            loan = False
    else:
        loan = False
elif size<5:
    if history<4:
        loan = False
    elif income>=7 or down_payment>=7:
        loan = True
    elif income>=4 and down_payment>=4:
        loan = True
    else:
        loan = False
else:
    loan = False
if loan == True:
    print(decision+yes)
else:
    print(decision+no)