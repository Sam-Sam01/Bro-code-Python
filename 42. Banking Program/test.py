# Python banking test softwere

# things are need todo this:
# 1. show total amount
# 2. deposit an amount
# 3. taking an amount 
# 4. exit

def show_balance(balance):

    print(f"Your balance is ${balance:.2f}")

def deposit():

    amount = float(input("How much would you like to deposit?"))
    if amount < 0:
        print("This is not a valid amount.")
        return 0
    else:
        print(f"You have deposited ${amount:.2f}.")
        return amount

def withdraw(balance):

    print(f"Your balance is ${balance:.2f}")
    amount = float(input("How much would you like to withdraw?"))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        balance -= amount
        print(f"You have withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}.")
        return balance

def main():

    balance = 0
    is_running = True

    while is_running:
        print("Banking Program Test")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance = withdraw(balance)
            case "4":
                is_running = False
            case "_":
                print("Invalid choice. Please try again.")

    print("Thank you for using our banking program.")

if __name__ == '__main__':
    main()