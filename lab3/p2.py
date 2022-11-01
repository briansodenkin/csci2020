def quicksort(a):
    # if the len is zero
    if not a:
        return a
    # first element as the pivot
    pivot = a[0]
    # split to three parts
    less = [i for i in a if i < pivot]
    equal = [i for i in a if i == pivot]
    larger = [i for i in a if i > pivot]
    return quicksort(larger) + equal + quicksort(less)
