from linkedlist import LinkedList

def add_two(linked1, linked2):
    number1 = 0
    for i, digit in enumerate(linked1):
        number1 += digit * pow(10, i)
    number2 = 0
    for i, digit in enumerate(linked2):
        number1 += digit * pow(10, i)

    return number1 + number2