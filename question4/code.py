def get_superdigit(string_digit, concatanation_multiple):
    # to multiply the string digit byhow many times it should appear
    # e.g 89 * 3 = 989898
    string_digit = string_digit * concatanation_multiple
    # digit total
    digit_total = 0
    # put in a counter
    for i in range(0, len(string_digit)):
        digit_total += int(string_digit[i])
    if digit_total >= 10:
        return get_superdigit(str(digit_total), 1)
    else:
        return str(digit_total)

    
print(get_superdigit('191', 3), "for 191 to give 6")
print(get_superdigit('9875', 4), " for 9875 to give 8")
print(get_superdigit('9875', 1), " for 9875 to give 2")
