empty='You do not have any items in your cart...'
item=''
items=[]
menu=int(1)
new_item=''
new_price=''
number=''
price=''
prices=[]
remove=''
total=float()

while menu>0 and menu<=6:
    print('Welcome to shopping cart, options are:')
    print('1. Add item.')
    print('2. View cart.')
    print('3. Remove item.')
    print('4. Compute total.')
    print('5. Change item')
    print('6. Quit.')
    print()
    menu=int(input('Please enter an action: '))
    print()
    if menu==1:
        item=input('What item would you like to add? ').lower()
        price=float(input(f'What is the price of {item}? $'))
        print(f"'{item}' has been added to the cart.\n")
        items.append(item)
        prices.append(price)
    elif menu==2:
        number_of_items=int(len(items))
        if number_of_items>0:
            print('The contents of the shopping cart are: ')
            for index in range(number_of_items):
                number=index+1
                item=items[index]
                price=prices[index]
                print(f'{number}. {item} - ${price:.2f}')
            print()
        else:
            print(empty)
            print()
    elif menu==3:
        number_of_items=int(len(items))
        if number_of_items>0:
            remove=int(input('Please select item to be removed: '))
            remove=remove-1
            if remove<number_of_items:
                items.pop(remove)
                prices.pop(remove)
                print('Item removed.')
                print()
            else:
                print('Sorry, that is not a valid item number.')
                print()
        else:
            print(empty)
            print()
    elif menu==4:
        for price in prices:
            total+=price
        print(f'The total price is: ${total:.2f}\n')
    elif menu==5:
        number_of_items=int(len(items))
        if number_of_items>0:
            number=int(input('Which item would you like to change? '))
            number=number-1
            new_item=input('What is the new item? ')
            new_price=input('What is the new price? $')
            items[number]=new_item
            prices[number]=new_price
            print('Item changed')
        else:
            print(empty)
            print()
    elif menu==6:
        menu=7
    else:
        print('Error, try again.')
print('Thank you. Goodbye.')