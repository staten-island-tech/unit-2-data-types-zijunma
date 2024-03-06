import random

def guess_number():
    random_number = random.randint(1,10)
    guess_history = []
    global guess

    while True:
        guess = int(input("Guess a number between 1 and 10:"))
        guess_history.append(guess)
        
        if guess == random_number:
            print("Congrats! You guessed correctly")
            print("Guess history:", guess_history) 
            break  
        elif guess < random_number:
            print("Your guess was too low, try again")
        else:
            print("Your guess was too high, try again")
guess_number()