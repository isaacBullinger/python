word='commitment'
word_letter=''
word_letters=len(word)
letter=input('What is your favorite letter? ')

for index in range(word_letters):
    word_letter=word[index]
    if word_letter==letter:
        print('_', end='')
    else:
        print(word_letter, end='')