import random
import os
from test2 import logo

print(logo)

print("Vítejte ve hře Guess secret number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")

computer_number = random.randint(1, 100)            # random secret number between 1 to 100
lets_continue = "yes"
win = ""

while lets_continue == "yes":
    difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard':  ").lower()
    difficulty_list = {
        "easy": 10,
        "hard": 5
    }
    while difficulty not in difficulty_list:
        print("Nerozumím zadání, prosím napište 'easy' nebo 'hard'.")
        difficulty = input().lower()
    
    lives = difficulty_list[difficulty]
    print(f"Váš počet zbývajících pokusů je {lives}.")

    while lives != 0:
        while True:
            guess_number = input("Tipněte si číslo:  ")
            try:
                guess_number1 = int(guess_number)
                break
            except ValueError:
                print("Zadaná hodnota musí být celé kladné číslo!")
        if guess_number1 < computer_number:
            result = "Příliš nízké"
        elif guess_number1 > computer_number:
            result =  "Příliš vysoké"
        elif guess_number1 == computer_number:
            result = f"Výborně, porazili jste počítač a uhodli jste tajné číslo {computer_number}."
            win = "yes"
        print(result)
        lives -= 1
        if lives == 0 or win == "yes":
            if lives == 0: 
                print("Počítač vyhrál. Prohráli jste.")
            lets_continue = input("Napište 'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit.  ").lower()
            while lets_continue not in ["yes", "no"]:
                print("Nerozumím zadání, prosím napište 'yes' nebo 'no'.")
                lets_continue = input().lower()
            os.system('cls')
            break
        print(f"Váš počet zbývajících pokusů je {lives}.")
    
