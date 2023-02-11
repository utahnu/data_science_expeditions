import argparse
import numpy as np
import os
import math

def main(number: int) -> int:
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    array = np.linspace(1, number, number, dtype=int)
    array_cubed = np.power(array, 3)

    sum = 0
    def is_fd_even(n):
        while n >= 10:
            n = n//10
        if n == 0:
            return False
        if n % 2 == 0:
            return True
        return False

    for i in array_cubed:
        if is_fd_even(i):
            sum += i

    print(f"cube({number}) = {int(sum)}")

    # array = np.array(list(range(0, number+1, 2)))
    # cubed = np.power(array, 3)
    # print(sum(cubed))

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)