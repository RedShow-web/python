ls3 = [2, 7, 5, 6, 9, 15]
new_list = []
for i in ls3:
    if i % 2 == 0:
        new_list.append(i / 4)
    else:
        new_list.append(i * 2)
print(new_list)
