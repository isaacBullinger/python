msg1 = 'The other day, I was really in trouble. It all started when I saw a very '
msg2 = 'down the hallway. "'
msg3 = '!" I yelled. But all I could think to do was to '
msg4 = ' over and over. Miraculously, that caused it to stop, but not before it tried to '
msg5 = ' right in front of my family.\n'
msg6 = 'I went out the door and saw my '
msg7 = ' holding a '
msg8 = '. This caused me to think about when I lived in '
msg9 = '. The weather was '
msg10 = ' was '
msg11 = '. It was a '
msg12 = ' day!'
space = ' '
enter = 'Please enter the following: \n'
story = '\nYour story is: \n'
print(enter)
adj0= input('adjective: ')
animal = input('animal: ')
verb0 = input('verb: ')
ex= input('exclamation: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
person = input('person: ')
noun0 = input('noun: ')
state = input('US state: ')
adj1 = input('adjective: ')
adj2 = input('adjective: ')

print(story)
print(msg1+adj0+space+animal+space+verb0+space+msg2+ex.capitalize()+msg3+verb1+msg4+verb2+msg5+msg6+person+msg7+noun0+msg8+state.capitalize()+msg9+adj1+msg11+adj2+msg12)