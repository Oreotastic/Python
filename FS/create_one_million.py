fileName = 'pi_million_digits.txt'

with open(fileName, 'w') as file_object:
    for index in range(0,1000000):
        file_object.write(str(index)+ '\n')
