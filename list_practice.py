item=''
items=[]
new=''
number=''

print('Please enter the items of the shopping list (type: quit to finish):')

while item!='Quit':
    item=input('Item: ').capitalize()
    if item!='Quit':
        items.append(item)

print()

print('The shopping list is: ')
for item in items:
    print(f'{item}')

print()

print('The shopping list with indexes is:')
for index in range(len(items)):
    item=items[index]
    print(f'{index}. {item}')

print()

number=int(input('Which item would you like to change? '))
new=input('What is the new item? ').capitalize()
items[number]=new

print()

print('The shopping list with indexes is:')
for index in range(len(items)):
    item=items[index]
    print(f'{index}. {item}')