blank=' _ '
count=int(0)
guess=''
guess_letters=len(guess)
guess_msg='What is your guess? '
word='mosiah'
word_letters=len(word)

#while guess != word:
    #print('Your hint is:'+blank+blank+blank)
    #if guess_letters==word_letters:

    #print('Congratulations! You guessed it!')
    #count=count+1

while guess != word:
    guess=input(guess_msg)
    guess_letters=len(guess)
    if guess_letters!=word_letters:
        print('Sorry, the guess must have the same number of letters as the secret word.')
    count=count+1
count=str(count)
print('Congratulations! You guessed it!')
print(f'It took you {count} guesses.')
