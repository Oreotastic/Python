numList = []

with open('num_list.txt') as file_object:
    for line in file_object:
        if line[0] == '1':
            numList.append(int(line))

print(numList)
