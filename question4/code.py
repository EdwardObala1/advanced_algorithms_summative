def get_superdigit(string_digit, concatanation_multiple):
    # to multiply the string digit byhow many times it should appear
    # e.g 89 * 3 = 989898
    string_digit = string_digit * concatanation_multiple
    print(string_digit)
    # digit total
    digit_total = 0
    # put in a counter
    for i in range(0, len(string_digit)):
        digit_total += int(string_digit[i])
    if digit_total >= 10:
        return get_superdigit(str(digit_total), 1)
    else:
        return str(digit_total)

    
print(get_superdigit('191', 3))
