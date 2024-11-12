calls = 0


def count_call(func):
    global calls
    calls += 1


def string_info(string):
    count_call(string)
    length = len(string)

    upper_case = string.upper()
    lower_case = string.lower()

    return length, upper_case, lower_case


def is_contains(string, list_to_search):
    count_call(is_contains)
    return string.lower() in [item.lower() for item in list_to_search]


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)