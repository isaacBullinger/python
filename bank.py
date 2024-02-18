avg=float()
balance=float()
balances=[]
change='yes'
count=int()
largest=float()
name=''
names=[]
total=float()

print('Enter the names and balances of bank accounts (type: quit when done)')

while name!='quit':
    name=input('What is the name of this account? ')
    if name!='quit':
        balance=float(input('What is the balance? $'))
        names.append(name)
        balances.append(balance)
count=len(names)

print()

print('Account information:')
for index in range(count):
    name=names[index]
    balance=balances[index]
    print(f'{index}. {name} - ${balance:.2f}')

print()

for balance in balances:
    total=float(total+balance)
print(f'Total: ${total:.2f}')

avg=total/count
print(f'Average: ${avg:.2f}')

for index in range(count):
    if balance>largest:
        largest=balance
        balances[index]=balance
        print()
        print('The account with the largest balance is:')
        print(f'{name} - ${balance:.2f}')
        print()

while change=='yes':
    change=input('Do you want to update an account (yes/no)? ').lower()
    if change=='yes':
        index=int(input('What account index do you want to update? '))
        new_balance=float(input('What is the new amount? '))
        balances[index]=new_balance
        print()
        print('Account information:')
        for index in range(count):
            name=names[index]
            balance=balances[index]
            print(f'{index}. {name} - ${balance:.2f}')
        print()
    else:
        print()
        print('Account information:')
        for index in range(count):
            name=names[index]
            balance=balances[index]
            print(f'{index}. {name} - ${balance:.2f}')
        print()