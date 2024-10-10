import random
from functools import reduce
from math import gcd

def greeting():
    while not (name := input("Welcome to the Brain Games! May I have your name? ")):
        pass

    print(f"Hello, {name}!")
    return name

# Function to calculate LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def game_scm():
    print("Find the smallest common multiple of the given numbers.")
    numbers = random.sample(range(1, 50), 3)
    while lcm_multiple(numbers)>1000:
        numbers = random.sample(range(1, 50), 3)
    yield f"{' '.join(map(str, numbers))}"
    guess = int(input("Your answer:  "))
    answer = lcm_multiple(numbers)
    yield answer
    yield guess

def game_progression():
    l = random.randint(8, 12)
    r = random.randint(3,5)
    start = random.randint(1, r)
    arr = [start * (r**i) for i in range(l)]
    hidden_in = random.randint(0, len(arr)-1)
    answer = arr[hidden_in]
    arr[hidden_in] = ".."
    yield f"{' '.join(map(str, arr))}"
    guess = int(input("Your answer:  "))
    yield answer
    yield guess

def game(logic):
    name = greeting()
    for i in range(3):
        generator = logic()
        print(f"Question: {next(generator)}")
        answer = next(generator)
        guess = next(generator)
        if guess == answer:
            print("Correct!")
        else:
            print(f"'{guess}' is a wrong answer ;(."
                  f" Correct answer was '{answer}'. Let's try again, {name}!")