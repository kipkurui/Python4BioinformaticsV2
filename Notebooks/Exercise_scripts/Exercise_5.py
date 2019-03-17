#!/home/user/miniconda3/bin/python

## Program to manage bank withdrawals, balance requests and deposits at the ATM

accountbal = 500000
choice = input("Please enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
while choice != 'q':
    if choice.lower() in ('w','d','b'):
        if choice.lower() == 'd':
            print("Please enter the amount to deposit")
            deposit=(int(input("amount:")))
            accountbal=accountbal+deposit
            print("New account balance is", accountbal)
            print("Anything else?")
            choice = input("Enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
            print(choice.lower())
        elif choice == ('w'):
                withdraw=int(input("Please enter the amount you'd like to withdraw:"))
                if accountbal<withdraw:
                    print("Error, insufficent funds")
                    print("please try again")
                else:
                        accountbal = accountbal - withdraw
                        print("New account balance is",accountbal)
                        choice = input("Enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
                        print(choice.lower())
        elif choice == ('b'):
            print("Your account balance is", accountbal)
            print("Would you like to do another transaction?")
            choice = input("Please enter 'b' to check balance, 'd' to deposit, 'w' to withdraw or 'q' to quit: ")
            print(choice.lower())
        else:
            if choice.lower =="q":
                print("Please pick your card. Thank you for using our services")                           