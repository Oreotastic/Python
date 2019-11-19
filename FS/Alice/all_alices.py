file_name = 'Alice.txt'

with open(file_name, 'r') as file_object:
    list = file_object.readlines()
    text = ''
    count = 0
    text = text.join(list)
    list = text.split('\n')
    text = text.join(list)
    list = text.split(' ')

    for word in list:
        if 'Alice' in word:
            count+=1

    print(f"alice is mentioned {count} times")
