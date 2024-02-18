msg1 = 'Please enter the following information: \n'
msg2 = '\nThe ID Card is:'
s1 = 'Please type your '
s2 = ': '
print (msg1)
fname = input ('First name: ')
lname = input ('Last name: ')
email = input ('Email address: ')
phone = input ('Phone number: ')
job = input ('Job title: ')
id = input ('ID Number: ')
hair = input ('Hair color: ')
eye = input ('Eye color: ')
month = input ('Month started: ')
training = input ('Have you received training? ')
line = '----------------------------------------'
print (msg2)
print (line)
print (lname.upper()+', '+fname.capitalize())
print (job.title())
print ('ID: '+id)
print ()
print (email.lower())
print (phone)
print(f"{'Hair: ' + hair.capitalize():<25} Eyes: {eye.capitalize()}")
print(f"{'Month: ' + month.capitalize():<25} Training: {training.capitalize()}")
print (line)