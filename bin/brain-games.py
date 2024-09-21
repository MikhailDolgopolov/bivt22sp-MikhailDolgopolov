import random
from functools import reduce
from math import gcd

from src.cli import greeting

# Function to calculate LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def game_scm(name):

    print("Find the smallest common multiple of the given numbers.")
    numbers = random.sample(range(1, 50), 3)
    while lcm_multiple(numbers)>1000:
        numbers = random.sample(range(1, 50), 3)
    yield f"{' '.join(map(str, numbers))}"
    guess = int(input("Your answer:  "))
    answer = lcm_multiple(numbers)
    yield answer
    yield guess

def game(logic):
    name = greeting()
    for i in range(3):
        generator = logic(name)
        print(f"Question: {next(generator)}")
        answer = next(generator)
        guess = next(generator)
        if guess == answer:
            print("Correct!")
        else:
            print(f"'{guess}' is a wrong answer ;(."
                  f" Correct answer was '{answer}'. Let's try again, {name}!")

game(game_scm)