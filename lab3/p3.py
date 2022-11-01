temp = {}
update_dict = {}

def load_data(file):
    import pickle
    try:
        fd = open(file, 'rb')
        answer = pickle.load(fd)
        fd.close()
        global temp
        temp = answer
        return answer
    except:
        print(f'{file} not exist')


def query(prof_name):
    result = []
    for i in temp.items():
        if prof_name in i[1]:
            result.append(i[0])
    return result


def update():
    import pickle
    remove_prof = []
    result_dict = {}
    for i in temp.items():
        if i[0] == 'Artificial Intelligence':
            remove_prof = i[1]
        else:
            result_dict[i[0]] = i[1]

    for i in result_dict.items():
        if i[0] == 'Computer Science':
            i[1].extend(remove_prof)

    result_dict['Metaverse'] = ['Mark', 'Neo', 'Trinity']
    global update_dict
    update_dict = result_dict
    pickle.dump(result_dict, open("dept-prof-updated.pydata", "wb"))

def get_depts_size():
    return {i: len(update_dict[i]) for i in update_dict}

# file = 'dept-prof.pydata'
# print(load_data(file))
# print(query('John'))
# update()
# print(update_dict)
# print(get_depts_size())
