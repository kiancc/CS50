# TODO
from cs50 import get_float


def main():

    cents = get_cents()
    # counts coins
    quarters = int(calculate_quarters(cents))
    cents = cents - quarters * 25

    dimes = int(calculate_dimes(cents))
    cents = cents - dimes * 10

    nickels = int(calculate_nickels(cents))
    cents = cents - nickels * 5

    pennies = int(calculate_pennies(cents))
    cents = cents - pennies * 1
    # sums coins
    coins = quarters + dimes + nickels + pennies

    print(coins)


def get_cents():

    # prompts user for input
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            break

    return n * 100

# calculates quarters


def calculate_quarters(cents):
    return cents / 25

# calculates dimes


def calculate_dimes(cents):
    return cents / 10

# calculates nickels


def calculate_nickels(cents):
    return cents / 5

# calculates pennies


def calculate_pennies(cents):
    return cents


main()