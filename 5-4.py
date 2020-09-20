replace = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four'}
new_file = []
with open('int.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(replace[i[0]] + '  ' + i[1])
    print(new_file)

with open('target.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)