from random import randint
a = 0
while True:
    choice = input("Roll the dice? (y/n): ").lower()
  
    if(choice == "y"):
      num = int(input("How many time do you want to roll the dice? "))
      for i in range(num):
           print(f"({randint(1,6)} , {randint(1,6)})")
    elif( choice == "n"):
      print(f"Thanks for playing the game. You played the game for {a} times")
      break
    else:
      print("invalid choice")
    a += 1



