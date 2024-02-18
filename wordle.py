import random

congrats='Congratulations! You guessed it!'
count=int(0)
guess=''
guess_letters=len(guess)
guess_msg='What is your guess? '
hint=[]
hint_msg='Your hint is: '
words=['slate', 'keeps', 'zebra', 'quite', 'cater']
word_letter=''
guess_letter=''
word=random.choice(words)
word_letters=len(word)
capital=''
lower=''
    
while guess!=word:
    count=count+1

    # Beginning

    if count==1:
        print('Welcome to the word guessing game!\n')
        hint.append(hint_msg)
        for index in range(word_letters):
            word_letter=word[index]
            hint.append('_ ')
        print(''.join(hint))

    # Guess:

    guess=input(guess_msg).lower()
    guess_letters=len(guess)

    if guess_letters==word_letters and guess!=word:
        hint1=[]
        hint1.append(hint_msg)
        
        # Hint:

        for index in range(word_letters):
            word_letter=word[index]
            guess_letter=guess[index]
            if word_letter==guess_letter:
                hint1.append(word_letter.upper()+' ')
            elif guess_letter in word and word_letter!=guess_letter:
                hint1.append(guess_letter.lower()+' ')
            else:
                hint1.append('_ ')
        print(''.join(hint1))

    # Letter count:

    elif guess_letters!=word_letters:
        print('Sorry, the guess must have the same number of letters as the secret word.\n')
        
count=str(count)
print()
if count>'1':
    print(congrats)
    print(f'It took you {count} guesses.')
else:
    print(congrats)
    print(f'It took you {count} guess.')