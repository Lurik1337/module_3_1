def count_calls():
    global calls
    calls += 1
    return calls


def string_info():
    count_calls()
    amount = len(string)
    cap_str = string.upper()
    low_str = string.lower()
    return amount, cap_str, low_str


def is_contains():
    count_calls()

    if string in list_to_search:
        return True

    else:
        return False


calls = 0
string = input()
list_to_search = [input()]
string_info()
is_contains()
print(calls)
