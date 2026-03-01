from random import randint
n=randint(1,100)
choice=input("Enter Yes to play and No to terminate:").lower()

if (choice=="yes"):
    attempt=12
    for i in range(attempt):
        a = int(input("Guess the number:"))
        remaining = attempt-(i+1)
        print(f"You have {remaining} remaining attempts!")
        if (a>n):
            print("Wrong guess!\nHint: Enter lower number!")
        elif(a<n):
            print("Wrong guess!\nHint: Enter higher number!")
        else:
            print(f" Congratulations !!!!\nYou have guessed right number!\nAtempts = {i+1}")
            print(f"Computer choice was :{n}")
            break
    else:
        print(f"You lost! The number was :{n}\nTry again next time!")
        
        
elif(choice=="no"):
    print("Game terminated")
else:
    print("Invalid input")