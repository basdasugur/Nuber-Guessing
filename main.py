
import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start! ")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))


num = random.randint(low, high)

ch = 7      # total allowed chaces
gc = 0      # Guess counter


print(f"Yu have 7 chances to guess the number between {low} and {high}. Let's start!")

while gc < ch:
    gc += 1
    guess = int(input("Enter you guess: "))
    
    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} attemps.")
        break
    
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. You guessed it in {gc} attempts.")
        break
    
    elif guess > num:
        print(f"Too high! Try a lower number.")
        
    elif guess < num:
        print(f"Too low! Try a higher number.")

