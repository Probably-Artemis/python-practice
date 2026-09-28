"""
Objective: the user has five tries to guess the secret number. After each wrong guess, tell them whether the secret number is higher or lower. If they guess it, congratulate them and end the game right away. If they run out of tries, tell them what the number was.
Restriction: you may not edit preexisting code.
"""

secret = 37

guessed = False

for attempt in range(5):
    guess = int(input("Guess: "))

    if guess == secret:
        print("You got it!")
        guessed = True
        break # break immediately exits the current loop.
    elif guess < secret:
        print("Higher.")
    else:
        print("Lower.")

if not guessed:
    print("Out of tries. The number was", secret)

# python also has a for/else, where the else runs only if the loop finished without a break. look it up if you're curious.