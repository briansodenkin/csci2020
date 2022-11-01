def non_unique(list):
    temp_dict = {}
    for i in list:
        if i not in temp_dict.keys():
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
    result = [[i for i in temp_dict.keys() if temp_dict[i] > 1],
              [temp_dict[i] for i in temp_dict.keys() if temp_dict[i] > 1]]
    return result
