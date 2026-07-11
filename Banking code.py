'''
Simple Banking System using functions with the following options:
1.Check Balance
2.Deposit Money in Account
3.Withdraw Money from Account
4.Check KYC Documents
5.Add KYC Documents
'''

balance=0.0               #inital balance
kyc_documents={}

def check_balance():
    print(f"Your Current Balance is {balance}\n")

def deposit(amount):
    global balance                  #so that we can update the value of balance variable which is a global variable
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

def check_kyc():                      #Check Know Your Customer Documents
    if len(kyc_documents)==0:
        print("KYC not done!\n")
    else:
        for doc in kyc_documents:
            print(f"{doc}:{kyc_documents[doc]}")
        print("\n")

def update_kyc(docs):                #Update and add KYC Documents
   global kyc_documents
   kyc_documents.update(docs)


if __name__=="__main__":
    print("Welcome to ABC Bank!!!\n")

    while True:
        print("1. Check Your Balance")
        print("2. Deposit an Amount")
        print("3. Withdraw an Amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")

        choice=input("Enter your choice (1-6): ")

        if choice=='1':
            check_balance()
        elif choice=='2':
            amt=float(input("Enter the amount to deposit: "))
            deposit(amt)
        elif choice=='3':
            amt=float(input("Enter the amount to withdraw: "))
            withdraw(amt)
        elif choice=='4':
            check_kyc()
        elif choice=='5':
            kyc_docs={}
            n_documents=int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key=input("Enter the document type: ")
                value=input("Enter the document number: ")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
            print("KYC Updated!!\n")
        elif choice=='6':
            print("*** Quitting ***\n")
            break
        else:
            print("Invalid input!! Enter a valid choice.\n")

    print("Thank you for banking with us.\n")