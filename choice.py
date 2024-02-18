error='That is not a choice! Please try again...'
end='THE END'
option=input('You are the commander of a space ship. You encounter an asteroid field, do you PROCEED or GO AROUND? ')
if option.lower()=='go around':
    option=input('You see a planet in the distance, do you APPROACH it SCAN or KEEP GOING? ')
    if option.lower ()=='approach':
        option=input('You see clouds and oceans on the planet! What a great discovery! Do you go DOWN or STAY? ')
        if option.lower()=='down':
            print('You go down to the surface and find signs of life, they invite you to dinner, you are on the menu. '+end)
        elif option.lower()=='stay':
            print('You are ambushed from behind by space pirates, they mock you for being dull and not going down to the planet, you become friends, you marry one of their daughters, you live happily ever space after! '+end)
        else:
            print(error)
    elif option.lower()=='scan':
        option=input('You begin the scan and the scanner breaks, do you LEAVE or REPAIR the scanner? ')
        if option.lower()=='leave':
            option=input('You leave and come across an escape pod drifting through space, do you TAKE it into your hangar or LEAVE IT? ')
            if option.lower()=='take':
                print('It has alien life forms inside, they are grateful for the rescue! In return they reveal the location of their home planet! '+end)
            elif option.lower()=='leave it':
                print('Your crew commit mutiny and jettison you in an escape pod headed towards the barren planet! '+end)
            else:
                print(error)
        elif option.lower()=='repair':
            print('You repair the scanner and continue the scan, you recieve a comunication: "klatu verata niktu". '+end)
        else:
            print(error)
    elif option.lower()=='keep going':
        option=input('You make it to the space station orbiting Alpha Centauri. Do you DOCK or FLY BY? ')
        if option.lower()=='dock':
            option=input('You are low on fuel, the space station is charging a steep price for fuel--you will not have much money left, do you REFUEL or RISK IT? ')
            if option.lower()=='refuel':
                print('Your ship is refueled, you travel to the mining fields to pick up cargo, the cargo was fuel, you feel dumb. '+end)
            elif option.lower()=='risk it':
                print('You slingshot your ship using the gravity of Alpha Centauri to fly towards a gas cloud so you can use your fuel condensers. '+end)
            else:
                print(error)
        elif option.lower()=='fly by':
                print('You run out of fuel, you send a message to the planet earth for help, they have been overrun by communist alien plant cocoon clones, better dead than red, you die, honorably. '+end)
        else:
            print(error)
    else:
        print(error)
elif option.lower()=='proceed':
    option=input('You feel a thud, do you STOP to investigate or CONTINUE? ')
    if option.lower()=='stop':
        option=input('Your crew notice a leak, you only have one patch, do you USE it or NOT? ')
        if option.lower()=='use':
            print('The leak is patched, You continue and make it back to earth! Good Job! '+end)
        elif option.lower()=='not':
            option=input('The room automatically seals, preventing further air loss. You continue on your journey and encounter a derelict ship. Do you LAUNCH a probe to investigate or CONTINUE ON? ')
            if option.lower()=='launch':
                print('The probe scans for life forms and valuable items and finds a stash of Xamuk crystals, you are rich now! '+end)
            elif option.lower()=='continue on':
                print('The ship suddenly comes to life and launches an attack destroying your ship! '+end)
            else:
                print(error)
        else:
            print(error)
    elif option.lower()=='continue':
        option=input('The hull is compromised! You and your crew launch an escape pod. A few days later you hear a signal from a ship, do you RESPOND or remain SILENT? ')
        if option.lower()=='respond':
            print('It is a planetery guard ship, you and your crew are saved! '+end)
        elif option.lower()=='silent':
            print('You run out of food in a month. '+end)
        else:
            print(error)
    else:
        print(error)
else:
    print(error)