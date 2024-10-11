def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [43, 'good', False]

values_dict = {'a': 10, 'b': 'новая строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)
