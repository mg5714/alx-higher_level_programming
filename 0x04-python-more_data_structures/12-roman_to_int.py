#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    dig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    for i in range(len(roman_string) - 1, -1, -1):
        if i < len(roman_string) - 1 and dig[roman_string[i]] < dig[roman_string[i + 1]]:
            result -= dig[roman_string[i]]
        else:
            result += dig[roman_string[i]]

    return result
