my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
elem = my_list[i]
while i < len(my_list):
    elem = my_list[i]
    i += 1
    if elem < 0:
        break
    elif elem == 0:
        continue
    print(elem)