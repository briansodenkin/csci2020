def count_alphabet(test_string):
    count = 0
    for i in test_string:
        if i.isalpha():
            count +=1
    return count

def hksar_capitalization(test_string):
    test_string = test_string.replace('h', 'H')
    test_string = test_string.replace('k', 'K')
    test_string = test_string.replace('s', 'S')
    test_string = test_string.replace('a', 'A')
    test_string = test_string.replace('r', 'R')
    return test_string

def concat(test_string, new_string):
    return test_string + new_string

def search(test_string, sub):
    return test_string.rfind(sub)