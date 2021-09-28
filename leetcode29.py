'''
This was very easy, I guess there's a pretty big variability in difficulty for these medium problems.
'''

def division(dividend, divisor):
    sign = 1
    if (dividend >= 0) != (divisor > 0):
        sign = -1

    divisor = abs(divisor)
    dividend = abs(dividend)
    result = 0
    while dividend >= divisor:
        dividend -= divisor
        result += 1

    print(result * sign)

division(1, 1)
