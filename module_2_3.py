my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []

i = 0

while i < len(my_list):

    if my_list[i] > 0:
        new_list.append(my_list[i])
        i += 1
    elif my_list[i] == 0:
        i += 1
    else:
        break

print(new_list)
