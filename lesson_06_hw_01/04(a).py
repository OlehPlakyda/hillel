from random import randint


def random_12digit_number():
    return randint(100000000000, 999999999999)


def get_max_digit(number):  # returns int
    number = str(number)
    for i in range(9, 0, -1):
        if f'{i}' in number:
            return i


def main():
    number = random_12digit_number()
    print('A randomly generated 12-digit number: ', number)
    print('The largest digit of this number: ', get_max_digit(number))


main()
