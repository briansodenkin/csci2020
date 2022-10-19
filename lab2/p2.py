def roman_to_decimal(str1, str2):
	# value mapping provided
    roman_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int1, int2 = 0, 0
    for i in range(len(str1)):
        # if not the leading character, and current number
        if i > 0 and roman_int_map[str1[i]] > roman_int_map[str1[i - 1]]:
            # minus the value again
            # e.g. CM, 1100 - 100 * 2
            int1 = int1 + roman_int_map[str1[i]] - 2 * roman_int_map[str1[i - 1]]
        else:
            int1 = int1 + roman_int_map[str1[i]]

    for i in range(len(str2)):
        if i > 0 and roman_int_map[str2[i]] > roman_int_map[str2[i - 1]]:
            int2 = int2 + roman_int_map[str2[i]] - 2 * roman_int_map[str2[i - 1]]
        else:
            int2 = int2 + roman_int_map[str2[i]]
    n = min(int1, int2)
    return n
