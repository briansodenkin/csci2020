while True:
    print("Enter an integer:", end=" ")
    rows = int(input())
    if rows == 0 or rows < 0:
        break
    print("Enter a string:", end=" ")
    out = str(input())

    for i in range(1, rows + 1):
        for j in range(rows, 0, -1):
            if j > i:
                for _ in range(len(out)):
                    print(" ", end='')
            else:
                print(str(out), end='')
        print("")
print("Program ends.")
