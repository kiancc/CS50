# TODO
from cs50 import get_int


def main():

    # assigns return value of get_height to heigh variable
    height = get_height()
    i = 1
    j = height - 1

    # prints pyramid
    while height >= i:
        print(" " * j, end="")
        print("#" * i)
        i += 1
        j -= 1


def get_height():

    # prompts user for integer input (need to implement between 1 and 8)
    while True:
        n = get_int("Height: ")
        if n < 9 and n > 0:
            break
    return n


main()