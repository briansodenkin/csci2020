def load_data(file):
    import pickle
    try:
        fd = open(file, 'rb')
        answer = pickle.load(fd)
        fd.close()
        return answer
    except:
        print(f'{file} not exist')
        
