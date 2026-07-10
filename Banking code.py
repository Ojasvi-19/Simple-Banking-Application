def check_balance():
    print(f"Your Current Balance is {balance}\n")

def deposit(amount):
    global balance                  #so that we can update the value of balance variable 
    if amount>0:
        balance+=amount
        print("Deposit was successful. \n")
    else:
        print("Cannot deposit a negative or zero amount.\n")

def withdraw(amount):
    global balance
    if amount<=0:
        print("Cannot withdraw a negative or zero amount.\n")
    elif amount>balance:
        print("Cannot withdraw! Insufficient balance!!\n")
    else:
        balance-=amount
        print("Withdrawal was successful.\n")

balance=0.0               #inital balance

print("Welcome to ABC Bank!!!\n")

while True:
    print("1. Check Your Balance")
    print("2. Deposit an Amount")
    print("3. Withdraw an Amount")
    print("4. Quit")

    choice=input("Enter your choice (1-4): ")

    if choice=='1':
        check_balance()
    elif choice=='2':
        amt=float(input("Enter the amount to deposit: "))
        deposit(amt)
    elif choice=='3':
        amt=float(input("Enter the amount to withdraw: "))
        withdraw(amt)
    elif choice=='4':
        print("Quitting")
        break
    else:
        print("Invalid input!! Enter a valid choice")

print("Thank you for banking with us.")