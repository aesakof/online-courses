import random

def match(code, guess):
    '''
    If any digit in the user's guess is in the same position as the code,
    return True
    '''
    for i in range(3):
        if guess[i] == code[i]:
            return True
    return False

def close(code, guess):
    '''
    If any digit in the user's guess is anywhere in the code, return True
    '''
    for x in guess:
        if x in code:
            return True
    return False


def run():
    digits = list(range(10))
    random.shuffle(digits)
    code = digits[:3]
    print(code)

    game_won = False
    while not game_won:
        guess = input("What is your guess? ")
        guess = [int(x) for x in str(guess)]
        print(guess)

        if code == guess:
            print("You win!")
            game_won = True
        elif match(code, guess):
            print("Match")
        elif close(code, guess):
            print("Close")
        else:
            print("Nope")


run()
