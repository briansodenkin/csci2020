while True:
    try:
        num = int(input("Please input a palindrome number: "))
    except:
        print("Your input is not a palindrome number!")
        continue
    tmp = num
    rev = 0
    while(num>0):
        digit = num % 10
        rev = rev*10 + digit
        num = num // 10 
    if (tmp == rev):
        print("{} is a palindrome number! Program ends.".format(tmp))
        break
    print("Your input is not a palindrome number!")
