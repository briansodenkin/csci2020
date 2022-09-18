print("Please input a string:", end=" ")
line = input()
base = 0
line_list = list(line)

for i, a in enumerate(line_list):
    if a.isalpha():
        line_list[i] = chr(ord(a) + 1)
print("The encrypted string is:", end=" ")
print(''.join(line_list))
