paragraph='In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
paragraph_letter=''
paragraph_letters=len(paragraph)
again='yes'

while again=='yes':
    number=int(input('Please enter a number: '))
    
    for i, paragraph_letter in enumerate(paragraph):
        
        if i%number==0:
            print(paragraph_letter.upper(), end='')
        elif i%number!=0:
            print(paragraph_letter, end='')

    x=input('Would you like to enter another number? ')

