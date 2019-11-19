def makeGuestList(name, dir):
    with open(dir, 'a+') as file_object:
        file_object.write(name + '\n')

name = input('What is your name? ')
dir = input('Where are we storing this list? ')

print(makeGuestList(name, dir))
