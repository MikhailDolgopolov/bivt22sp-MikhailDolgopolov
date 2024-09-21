def greeting():
    while not (name := input("Welcome to the Brain Games! May I have your name? ")):
        pass

    print(f"Hello, {name}!")
    return name
