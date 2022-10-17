while True:
    print("Enter an integer:", end=" ")
    rows_num = int(input())
    if rows_num == 0 or rows_num < 0:
        break
    print("Enter a string:", end=" ")
    string = str(input())
    for i in range(1, rows_num+1):
        for j in range(rows_num, 0, -1):
            if j > i:
                # print number of space according to the string length
                for _ in range(len(string)):
                    print(" ", end='')
            else:
                print(str(string), end='')
        print("")
print("Program ends.")
