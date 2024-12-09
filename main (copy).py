import random
from colorama import Fore, Style, init

init(autoreset=True)

def spin_roulettle():
  return random.randint(0,36)
  
balance = 100

def roulette_game():
  print(Fore.GREEN + "Welcome to the Roulette Game!")
  print(f"Your starting balance is ${balance}")

roulette_game()

red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 31, 33, 35,}
black = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 30, 32, 34,}
green = {0, 36}
number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21 ,22 ,23 ,24 ,25 ,26 ,27,28 ,29 ,30 ,31 ,32 ,33 ,34 ,35 ,36 }

print("Would you like to bet on Black, Red, or Green, or a number?")
Decision = input()

if Decision == "red":
  print("How much would you like to bet")
  bet = int(input())
  if bet > balance:
    print("You don't have enough money to make that bet broke ass bitch")
  else: 
    bet <= balance
    print("Spinning the wheel...")
    spin_roulettle()
    if spin_roulettle() in red:
      print("you win! You get double your money back!")
      balance += bet * 2
    else:
      print("your a fucking loser")
      balance -= bet
    if balance <= 0:
      print(Fore.RED + "You have run out of money! Game over.") 
      print(balance)
      

if Decision == "black":
  print("How much would you like to bet")
  bet = int(input())
  if bet > balance:
    print("You don't have enough money to make that bet broke ass bitch")
  else: 
    bet <= balance
    print("Spinning the wheel...")
    spin_roulettle()
    if spin_roulettle() in black:
      print("you win! You get double your money back!")
      balance += bet * 2
    else:
      print("your a fucking loser")
      balance -= bet
    if balance <= 0:
      print(Fore.RED + "You have run out of money! Game over.") 
      print(balance)
      

if Decision == "green":
  print("How much would you like to bet")
  bet = int(input())
  if bet > balance:
    print("You don't have enough money to make that bet broke ass bitch ")
  else: 
    bet <= balance
    print("Spinning the wheel...")
    spin_roulettle()
    if spin_roulettle() in green:
      print("you win! You get double your money back!")
      balance += bet * 2
    else:
      print("your a fucking loser")
      balance -= bet
    if balance <= 0:
      print(Fore.RED + "You have run out of money! Game over.") 
      print(balance)
      

if Decision == "number":
  print("How much would you like to bet")
  bet = int(input())
  if bet > balance:
    print("You don't have enough money to make that bet broke ass bitch ")
  else: 
    bet <= balance
    print("what number would you like to bet on?")
    number = int(input())
    print("Spinning the wheel...")
    spin_roulettle()
    if spin_roulettle() == number :
      print("you win! You get 35 times your bet!")
      balance += bet * 35
    else:
      print("your a fucking loser")
      balance -= bet
    if balance <= 0:
      print(Fore.RED + "You have run out of money! Game over.") 
      print(balance)
      print("is how much money you got left")
      
option = input("Do you want to play again? (yes/no): ").strip().lower()
if balance <= 0:
  print(Fore.RED + "You have run out of money! Game over.") 
elif option == "no":
  print("Good Bye! Thanks for playing!")
else:
  print("starting another game")
  






