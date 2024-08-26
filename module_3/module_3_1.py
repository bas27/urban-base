
calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string: str):
    count_calls()
    len_string = len(string)
    return tuple([len_string, string.upper(), string.lower()])

def is_contains(string: str, list_to_search: list):
    count_calls()
    is_contains = False
    for element in list_to_search:
        if element.lower() == string.lower():
            is_contains = True
    return is_contains


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
