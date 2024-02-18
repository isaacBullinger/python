child = float(input("What is the price of a child's meal? $"))
adult = float(input("What is the price of an adult's meal? $"))
children_number = int(input('How many children are there? '))
adult_number = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))
tip = float(input('What is the tip percentage? '))
print()

subtotal = (child*children_number)+(adult*adult_number)
print(f'Subtotal: ${subtotal:.2f}')
tax = subtotal * (tax/100)
print(f'Sales Tax: ${tax:.2f}')
total = subtotal + tax
tip = total * (tip/100)
print(f'Tip: ${tip:.2f}')
total = total + tip

print(f'Total: ${total:.2f}\n')
amount = float(input('What is the payment amount? '))
print(f'Change: ${(amount-total):.2f}')

