#This is a sample budget app

myDatabase = {}


class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdrawal(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount
        return db


def init():
    print('==== **** You are welcome to the Budget App Interface **** ====\n')
    menu()


def menu():
    try:
        user = int(input('''***What you you like to do? ***:  \nPress (1) to create a new budget
    Press (2) to deposit into your account
    Press (3) to withdraw from your account
    Press (4) to check your balance
    Press (5) to transfer from one budget account to another
    Press (6) to quit\n'''))
    except:
        print('Invalid input')
        menu()

    if user == 1:
        newBudget()
    elif user == 2:
        credit()
    elif user == 3:
        debit()
    elif user == 4:
        balance()
    elif user == 5:
        transfer()
    elif user == 6:
        out()
    else:
        print('Invalid option selected, please try again')
        menu()


def newBudget():
    print('Creating a New Budget')

    budgetName = input('Enter budget name: ')
    try:
        budgetAmount = int(input('Enter the amount: '))
    except:
        print('\nInvalid input')
        newBudget()
    budget = Budget(budgetName, budgetAmount)
    myDatabase[budgetName] = budgetAmount
    print(' ')
    print(f'Budget {budgetName} has been setup with #{budgetAmount}')
    menu()


def debit():
    print('''*** Withdrawing from an exiting Budget Account
    Here is the list of availabel Budget Accounts''')

    for key, value in myDatabase.items():
        print(f'- {key}')

    try:
        wRequest = int(input(
            'Press (1) to continue with your debit transaction and (2) to stop debit transaction\n'))
    except:
        print('\nInvalid option')
        wRequest = int(input(
            'Press (1) to continue with your debit transaction and (2) to stop debit transaction\n'))
    if wRequest == 1:
        userRequest = input(
            'Please select the budget account you would like to withdraw from, from the list given above \n')
        if userRequest in myDatabase:
            print('''NB: Before you proceed to make withdrawals, note that you can't withraw the total balance in your budget account
            There must be a minimun balance of #10 in the account''')
            wAmount = int(
                input('Enter the amount you would like to withdraw: \n'))
            if wAmount < myDatabase[userRequest]:
                balance = int(myDatabase[userRequest])
                newBalance = Budget.withdrawal(userRequest, wAmount, balance)
                myDatabase[userRequest] = newBalance
                print(
                    f'#{wAmount} has been debited from budget {userRequest}\n Budget balance is {newBalance}')
                menu()
            else:
                wAmount = int(input(
                    f'\nBudget {userRequest} is insufficient of the #{wAmount} required.\nThe actual balance is {myDatabase[userRequest]}\nTo make a deposit into the budget {user}, press (1) and (2) to cancel the transaction'))
                if wAmount == 1:
                    dAmount = int(
                        input('Enter the amount you would like ti deposit: \n#'))
                    balance = int(myDatabase[userRequest])
                    newBalance = Budget.deposit(dAmount, balance)
                    myDatabase[userRequest] = newBalance
                    print(' ')
                    print(
                        f'Budget {userRequest} has been credited with #{dAmount}\n')
                    debit()
                elif wAmount == 2:
                    debit()
                else:
                    print('Invalid option selected')
                    debit()
        else:
            userRequest = int(input(
                f' *** Budget {userRequest} does not exit!***\nPress (1) to create a new budget\nPress (2) to choose another budget account\nPress (3) to perform another transaction\n'))
            if userRequest == 1:
                newBudget()
            elif userRequest == 2:
                debit()
            elif userRequest == 3:
                menu()
            else:
                print('Invalid option selected')
                debit()
    elif wRequest == 2:
        print('\nYou have terminated the withdrawal transaction')
    else:
        print('Invalid option selected, please try again')
        debit()


def credit():
    print('''*** Deposit into a Budget Account***
    The Available Budgest are''')
    for key, value in myDatabase.items():
        print(f' - {key}')

    try:
        dOption = int(input(
            '\nPress (1) to contine with your deposit trannsaction\nPress (2) to stop deposit transaction\n'))
    except:
        print('\nInvalid option')
        credit()
    if dOption == 1:
        userOption = input('Select a budget: \n')
        if userOption in myDatabase:
            dAmount = int(input('Enter the amount you wished to deposit: \n'))
            balance = int(myDatabase[userOption])
            newBalance = Budget.deposit(dAmount, balance)
            myDatabase[userOption] = newBalance
            print(
                f'\nBudget {userOption} has been credited with #{dAmount}\nTotal Budget balance is now #{newBalance}')
            print(' ')
            menu()
        else:
            print(' ')
            userOption = int(input(
                f'Budget {userOption} does not exist!\nPress (1) to create a new budget\nPress (2) to choose the right budget\nPress (3) to perform another transaction'))
            if userOption == 1:
                newBudget
            elif userOption == 2:
                credit()
            elif userOption == 3:
                menu()
            else:
                print('Invalid option selected')
                credit()
    elif dOption == 2:
        print('\nYou have terminated the deposit teansaction')
        menu()
    else:
        print('You have selected an invalid option')
        credit()


def balance():
    print('*** Getting your Budget Balance ***\n')
    checkBal = Budget.balance(myDatabase)
    if checkBal == None:
        print('')
        menu()
    else:
        print(f'#{checkBal}')
        menu()


def transfer():
    print('*** Available and Valid Budgets')
    for key, value in myDatabase.items():
        print(key)
        print(' ')
    print('''*** Transfer Options ***
    Please note that you must maintain a minimum balance of #10 in your budget accont''')
    fundingBudget = input('Enter the budget you are transfering from: \n')
    if fundingBudget in myDatabase:
        try:
            fundingAmt = int(
                input('Enter the amount you want to transfer: \n'))
        except:
            print('\nInvalid input')  # Just corrected this place
            fundingAmt = int(
                input('Enter the amount you want to transfer: \n'))
        if fundingAmt < myDatabase[fundingBudget]:
            receivingBudget = input(
                'Enter the budget you want to transfer to:\n')
            if receivingBudget in myDatabase:
                db = Budget.transfer(
                    myDatabase, fundingBudget, fundingAmt, receivingBudget)
                print('')
                print(
                    f'You have successfully transferred #{fundingAmt} from {fundingBudget} to {receivingBudget}')
                for key, value in db.items():
                    print(f'{key}, {value}')
                menu()
            else:
                print(
                    f'\n {receivingBudget} does not exist, please choose from the valid budget list')
                transfer()
        else:
            print(
                f'You do not have such amount #{fundingAmt} in {fundingBudget}')
            transfer()
    else:
        print(f'Budget {fundingBudget} do not exist\n')
        transfer()


def out():
    userChoice = int(input(
        'Are you sure you want to quit?: \nPress (1) to quit\nPress (2) to continue with other transactions'))
    if userChoice == 1:
        print('We hope you have had an amazing budgetting experience\nWe hope to see you again')
        quit()

    elif userChoice == 2:
        menu()
    else:
        print('You have selected an invalid option')
        out()


init()
