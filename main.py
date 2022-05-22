"""
The code checks the Collatz Conjecture for n - a number given by the user and shows the path taken to obtain 1.

No error handling since the numbers in possible range are proven to fulfill the Collatz Conjecture.

Collatz Conjecture
The Collatz conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive
integer into one. It concerns sequences of integers in which each term is obtained from the previous term as follows:
if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term
is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive
integer is chosen to start the sequence.
"""
print('Welcome to the Collatz Conjecture project.')
number = int(input('What number would you like to check? '))


def check(n):
    if n % 2 == 0:
        return n // 2;
    else:
        return 3 * n + 1;


path = [number]
index = 1
if number > 2 ** 20:
    print("The number is too big, try again.")
else:
    while number > 1:
        number = check(number)
        path += [number]
    print('The number fulfills the Collatz Conjecture')
    print(f'The path taken to obtain the end of procedure is : {path}')
