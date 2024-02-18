number=''
numbers=[]
sum=float()
avg=float()
largest=0
smallest=9999999999

print('Enter a list of numbers, type 0 when finished.')

while number!=0:
    number=float(input('Enter number: '))
    if number!=0:
        numbers.append(number)

# Sum

for number in numbers:
    sum+=number
print(f'The sum is: {sum:.0f}')

# Average

count=len(numbers)
avg=sum/count
print(f'The average is:  {avg}')

# Largest number

for number in numbers:
    if number>largest:
        largest=number
print(f'The largest number is: {largest:.0f}')

# Smallest positive number

for number in numbers:
    if number>0 and number<smallest:
        smallest=number
print(f'The smallest positive number is: {smallest:.0f}')

# Sorted list

numbers.sort()
print('The sorted list is:')
for index in range(len(numbers)):
    number=numbers[index]
    print(f'{number:.0f}')
