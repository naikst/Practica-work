my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
elem = my_list[index]
while index < len(my_list):
    elem = my_list[index]
    index += 1
    if elem < 0:
        break
    elif elem == 0:
        continue
    print(elem)