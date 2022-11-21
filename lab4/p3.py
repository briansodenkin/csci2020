from functools import reduce
def word_count(x, str, n):
    filteredList = list(filter(lambda x: len(x)>n, x))
    count = list(x.count(str) for x in filteredList)
    return reduce(lambda x, y : x + y, count)