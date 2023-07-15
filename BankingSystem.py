import csv


def login():
    customerfile = open('BankCustomerDetails.csv', 'r')
    reader = csv.DictReader(customerfile)
    print("WELCOME TO ABC BANKING SYSTEM!!")
    print("-----Login----")
    username = input("Enter the Username:")
    password = input("Enter the Password:")

    for row in reader:
        if row['username'] == username and row['password'] == password:
            print("Login Successful")
            bankmain(row)

    else:
        print("Username or Password Invalid\n---------------")
        login()

    customerfile.close()


def bankmain(row):
    while True:
        print("--------------")
        print("1.Check Bank Balance\n2.Amount Deposit\n3.Amount Withdrawal\n4.Logout")
        option = int(input("Choose an Option:"))
        if option == 1:
            print("Current Balance:", row['balance'])
        elif option == 2:
            deposit(row)
        elif option == 3:
            withdrawal(row)
        elif option == 4:
            print("---------------")
            login()

        else:
            print("Invalid option")


def deposit(row):
    balance = int(row['balance'])
    deposit_amount = int(input("Enter the amount to deposit:"))
    row['balance'] = balance + deposit_amount
    print(f"{deposit_amount} amount deposited successfully.\n Current Balance:{row['balance']}")


def withdrawal(row):
    balance = int(row['balance'])
    withdraw_amount = int(input("Enter the amount to withdraw:"))
    if withdraw_amount > balance:
        print("Insufficient Balance")
    else:
        row['balance'] = balance - withdraw_amount
        print(f"{withdraw_amount} amount withdrawn successfully.\n Current Balance:{row['balance']}")


login()
