def makeGuestList(name, dir):
    lst = []
    with open(dir, 'a+') as file_object:
        file_object.write(name + '\n')
    for line in file_object:
        lst.append(line)
    return lst

name = input('What is your name? ')
dir = input('Where are we storing this list? ')

print(makeGuestList(name, dir))
