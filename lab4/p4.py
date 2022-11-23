def get_average_grades(filename = 'grades.csv'):
    with open(filename) as f:
        grades = [[float(x)  for x in line.split(',')] for line in f]
        new_list = [[n for n in col if n!= -1] for col in zip(*grades)]
        average_grade_list = [sum(grade)/len(grade) for grade in new_list]
    return average_grade_list

