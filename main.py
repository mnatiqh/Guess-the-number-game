
from random import randint

print("Guess the number game!!!")

difficulty=input("Enter e for easy, m for medium and h for hard. ")

if difficulty == "e" :
    limit=100

elif difficulty == "m" :
    limit=1000

elif difficulty == "h" :
    limit=100000

else :
    print("Invalid input. You can't play this game if you can't enter input properly.")


x=randint(1,limit)
score=100

while True :
    guess=int(input(f"Guess the number 1 - {limit}: "))

    if guess == x :
        print("You have guessed the number correctly. Your score is" , score)
        break

    elif guess > x :
        print("Think of a smaller number.")

    else :
        print("Think of bigger number.")
    
    score=score-1



