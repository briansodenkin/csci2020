from curses.ascii import isalpha, isdigit
import getpass
secret_input = getpass.getpass('Please input your password: ')

flag_d = False # flag for digit
flag_a = False # flag for alphabet
flag_l = False # flag for length
chance_count = 0

while flag_a == False or flag_d == False or flag_l == False:
    # check if the password contain at least 8 characters
    if len(secret_input) >= 8:
        flag_l = True

    for i in range(len(secret_input)):
        # check if the password contain at least one digit
        if secret_input[i].isdigit():
            flag_d = True
        # check if the password contain at least one alphabet
        if secret_input[i].isalpha():
            flag_a = True

    # if valid
    if flag_a == True and flag_d == True and flag_l == True:
        confirm_pw = getpass.getpass('Please input again to confirm your password: ')
        while True:
            if secret_input == confirm_pw:
                print('Successfully set your password!')
                break
            elif chance_count == 2:
                print('Those passwords did not match. Please set your password next time. Program ends.')
                break
            else:
                print('Those passwords did not match.')
                confirm_pw = getpass.getpass('Please try again: ')
                chance_count += 1
    
    else:
        print('Invalid input.')
        secret_input = getpass.getpass('Please try again: ')



    