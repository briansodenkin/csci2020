def check_sublist(list1, a, b ,c):
    # list a: smaller than min of a,b,c
    lista, listb, listc = [], [], []
    for i in range(len(list1)):
        if list1[i] < min(a,b,c):
            lista.append(list1[i])
            
    # list b: smaller than a+b-c
    result = a+b-c
    for i in range(len(list1)):
        if list1[i] < result:
            listb.append(list1[i])

    # list c: smaller than a or b or c
    for i in range(len(list1)):
        if list1[i] < a or list1[i] < b or list1[i] < c:
            listc.append(list1[i])
            
    return lista, listb, listc

print(check_sublist([22,25,321,123],23,20,1))