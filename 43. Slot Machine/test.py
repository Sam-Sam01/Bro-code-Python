#This is me trying to create a slot machine game.

import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("***********************")
    print(" | ".join(row))
    print("***********************")


def get_payment(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 3
        elif row[0] == '🔔':
            return bet *2
        elif row[0] == '⭐':
            return bet * 100
    else:
        return 0


def main():
    balance = 100

    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")
        bet = int(input("Place your bet amount: "))

        if bet < 0 or bet > balance:
            print("Invalid bet amount.")
            continue

        balance -= bet
        row = spin_row()

        print("Spinning...\n")
        print_row(row)

        payout = get_payment(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else: 
            print("You lost this round.")
        
        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("***********************")
    print(f"Game over! Your final balance is ${balance:.2f}")
    print("***********************")

if __name__ == '__main__':
    main()