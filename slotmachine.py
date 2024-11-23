import random
symbols = ["🍍","🍒","🍋","🍎"]
results = []
def spinrow():
    return  [random.choice(symbols) for _ in range(3)]
def showbalance():
 pass
def printrow(row):
    print(" | ".join(row))

def payout(row,bet):
 if row[0] == row[1] == row [2]:
    if row[0] == '🍍':
     return bet * 3 
    elif row[0] == '🍋 ':
       return bet * 5
    elif row[0] == '🍒 ':
       return bet * 8
    elif row[0] == ' 🍎':
       return bet * 20
 return 0



balance = 100
print("---------------------------")
print("  Welcome to slot machine! ")
print("   🍍   🍒   🍋    🍎    ")
print("---------------------------")


while balance > 0:
    print(f"Current Balance: {balance}")
    bet = input("Enter the amount of your bet: ")

    if not bet.isdigit():
        print("Please enter a valid input")
        continue


    bet = int(bet)
    if balance == 0:
      print(f"You have no bets left: {balance} ")
      continue

    if bet > balance:
      print(f"Not enough balance: {balance} ")
      continue
    bet = int(bet)
    balance -= bet
    row = spinrow()
    printrow(row)

    