gpa = ''
cg = 0.0
prev_cred = 0

while True:
    gpa = input()
    if gpa == 'exit':
        print('Program ends')
        break
    gpa = gpa.split()
    current = float(gpa[0])
    cred = int(gpa[1])
    if current > 5.0 or current < 0.0 or cred < 0:
        print('Wrong input!')
        continue
    total_cred = cred + prev_cred
    cg = cg*prev_cred/total_cred + current*cred/total_cred
    prev_cred = total_cred
    print('Current GPA: {0:.2f}'.format(cg))
