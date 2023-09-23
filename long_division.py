#!/usr/bin/env python3

'''
Long division.
'''

def format_number(digits, dividend, dividend_list):
    '''
    Formats a number for printing.
    
    result: 0.|076923| 076923 <- (current) wrong formatting for 10/13
    should be perhaps: |0.76923| <- correction is planned

    '''

    repeating=""

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

    return out, repeating

def divide_without_repetition(dividend, divisor):
    ''' a/b , divide avoiding repetition '''
    dividend_list = [0]
    digits = [0]
    while True:
        if dividend in dividend_list: break
        dividend_list += [dividend]
        digits += [dividend // divisor]
        dividend = dividend % divisor
        dividend = dividend * 10
    return format_number(digits, dividend, dividend_list)

def is_prime_by_field_checks(field_of):

    if field_of==0: return False
    if field_of==1: return False

    if field_of==2: return True
    if field_of==3: return True
    if field_of==5: return True

    repeating_is_same_lenght_checker=0
    for number_iterated in range(1,field_of):

        _,repeating = divide_without_repetition(number_iterated, field_of)

        # debugging
        ##print(repeating, number_iterated, field_of)

        if repeating_is_same_lenght_checker == 0 :
            repeating_is_same_lenght_checker = len(repeating)
        if len(repeating) != repeating_is_same_lenght_checker :
            ##print("different lenght")
            return False
        
        if (int(repeating) % 9) != 0 :
            ##print("not divisible by nine")
            return False
        
    return True

def prime_check(field_of):
    #field_of = 91 # 13 # int(input('field of? (integer number) '))
    is_prime = is_prime_by_field_checks(field_of)
    if is_prime : print("[[" + str(field_of) + "]] is a prime number!")
    else: print("not a prime number!")

def prime_listing():
    try:
        primes_found = []
        checked_number = 0
        #stop_at = 100 # wrongly behaving with this limit
        stop_at = 10 # decently behaving with this limit
        while len(primes_found) != stop_at:

            print(".",sep="",end="")

            if is_prime_by_field_checks(checked_number):
                primes_found += [checked_number]
                print(checked_number, len(primes_found))
            
            checked_number += 1

        print(primes_found)

    except KeyboardInterrupt:
        print("KeyboardInterrupt: now exiting.")

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
        try:
            dividend = int(input('dividend? '))
            divisor = int(input('divisor? '))
        except ValueError:
            print("ValueError: now exiting.")
            break
        result,repeating = divide_without_repetition(dividend, divisor)
        print('result:', result, repeating)

def main_for_cases_to_correct():
    # special case with errors, partially fixed see comment above
    result,repeating = divide_without_repetition(10, 13)
    print('result:', result, repeating)

    prime_check(91) # wrongly considered prime

    prime_listing() # not properly working, see above, plus it ceases to list, it stops finding primes

if __name__ == '__main__':
    main()
    main_for_cases_to_correct()

