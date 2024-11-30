def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    amount = len(string)
    cap_str = string.upper()
    low_str = string.lower()
    return amount, cap_str, low_str


def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string.lower() in list_to_search:
        return True

    else:
        return False


calls = 0
print(calls)
