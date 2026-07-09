
import random
import time
Playing=True
while Playing:
    t=1
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    choice = int(input("Enter your choice: "))
    if choice not in [1, 2, 3]:
        print("Invalid choice")
        exit()
    elif choice == 1:
        print("Great! You have selected the Easy difficulty level.\nLet's start the game!")
        chances = 10
    elif choice == 2:
        print("Great! You have selected the Medium difficulty level.\nLet's start the game!")
        chances = 5
    elif choice == 3:
        print("Great! You have selected the Hard difficulty level.\nLet's start the game!")
        chances = 3

    num = random.randint(1, 100)
    #print(num)  # Remove this line when you finish testing
    start=time.time()
    for i in range(chances):
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if guess == num:
            print(f"Congratulations! You guessed the correct number in {t} attempts")
            break
        elif guess < num:
            print(f"Incorrect! The number is greater than {guess}.")
            t += 1
        elif guess > num:
            print(f"Incorrect! The number is less than {guess}.")
            t += 1
        if choice==1 and i==1:
          if num%2==0:
             print("Hint: The number is even.")
          else:
             print("Hint: The number is odd.")
        if choice==2 and i==0:
          if num%2==0:
            print("Hint: The number is even.")
          else:
            print("Hint: The number is odd.") 
    else:
      print(f"Game Over! The correct number was {num}.")        
    end=time.time()
    print("time taken:",end-start)
    #cont = int(input("Would you like to play again?\n1. Yes\n2. No\n"))

    while True:
      cont = int(input("Would you like to play again?\n1. Yes\n2. No\n"))

      if cont == 1:
        break
      elif cont == 2:
         print("Thank you for playing the Number Guessing Game!")
         Playing=False
         break
      else:
        print("Invalid choice. Please enter 1 or 2")
        #cont = int(input("Would you like to play again?\n1. Yes\n2. No\n"))



