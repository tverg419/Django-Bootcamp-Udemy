import random
# Get the Player code
def get_guess():
    return list(input("What is your guess?: "))

# Generate Coptuer code
def generate():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

# Three Clues
def get_clues(code,user_guess):

    clues = [];

    if user_guess == code:
        return "You've cracked the code!"

    for i, num in enumerate(user_guess):
        if num == code[i]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["None"]
    else:
        return clues

# Running Game

print("Welcome to Code Breaker!")

secret_code = generate();
clue_report = [];
active = True;

while active:

    guess = get_guess()

    clue_report = get_clues(secret_code,guess);
    for clue in clue_report:
        print(clue);
    if secret_code == guess:
        active = False
