#!/usr/bin/env python3

'''
Long division.
'''

def format_number(digits, dividend, dividend_list):
    '''
    Formats a number for printing.
    '''

    out = str(digits[0])
    repeating_digits_count = len(dividend_list)-dividend_list.index(dividend)

    digits_after_dot = digits[1:]
    if digits_after_dot == []:
        digits_after_dot = [digits[0]]

    if digits_after_dot[-1] == 0:
        digits_after_dot = digits_after_dot[:-1]
        repeating_digits_count -= 1

    if digits_after_dot != []:

        non_repeating_digits_count = len(digits_after_dot)-repeating_digits_count
        not_repeating = ''.join(map(str, digits_after_dot[:non_repeating_digits_count]))
        out_postdot = not_repeating
        if repeating_digits_count > 0:
            repeating = ''.join(map(str, digits_after_dot[-repeating_digits_count:]))
            out_postdot += '|' + repeating + '|'

        if out_postdot != '':
            out += '.' + out_postdot

    return out

def divide_without_repetition(dividend, divisor):
    ''' a/b , divide avoiding repetition '''
    dividend_list = []
    digits = []
    while True:
        if dividend in dividend_list:
            break
        else:
            dividend_list += [dividend]
            digits += [dividend // divisor]
            dividend = dividend % divisor
            dividend = dividend * 10
    return format_number(digits, dividend, dividend_list)



def main():
    '''
    Main function with tests.
    '''

    dividend_divisor_pairs = [
        (8, 2),
        (7, 2),
        (1, 3),
        (10, 3),
        (50, 4),
        (500, 4),
    ]
    '''
    8/2 = 4
    7/2 = 3.5
    1/3 = 0.|3|
    10/3 = 3.|3|
    50/4 = 12.5
    500/4 = 125
    '''

    for (dividend, divisor) in dividend_divisor_pairs:
        print(str(dividend)+'/'+str(divisor)+' =', divide_without_repetition(dividend, divisor))

    while True:
        dividend = int(input('dividend? '))
        divisor = int(input('divisor? '))
        print('result:', divide_without_repetition(dividend, divisor))

if __name__ == '__main__':
    main()
