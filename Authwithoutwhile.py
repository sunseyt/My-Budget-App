#Rigister

#Login
# - account number and password
#Bank Operation

import random
import string
database = {} #A database for our users

accountBalance = 35000
def initialize():

    print('Welcome to GTB')

    haveAccount = int(input('Do you have an account with GTB?: 1 (yes) 2(no):\n'))
    if haveAccount == 1:
        login()
    elif haveAccount ==2:
        register()
    else:
        print('You have selected an invalid option, please try again')
        initialize()

def login():
    print('''Welcome to the login portal
    Please provide your account number and password to gain access.''')

    accountNumberFromUser = int(input('Please enter your account number: \n'))
    password = input('Please enter your password: \n')

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)
            else:
                print ('Invalid account number or password')
                login()

def register():
    print('Welcome to the registration portal. \n Please provide the following information for registartion')
    firstName = input('What is your first name?: \n')
    lastName = input('What is your last name?: \n')
    emailAdd = input('What is your email address?: \n')
    users_password()

    password = (firstName[0:2] + lastName[-2:] + users_password())
    print('Your system generated password is: ', password)

    isValidOpt = False

    while isValidOpt == False:
        passwordChoice = input('''Do you like your system generated password?
        Enter 'yes' to save password
        Enter 'no' to create a custom password: ''').lower()
        if passwordChoice == 'yes':
            isValidOpt = True
            print('Your user password is: ', password)
        elif passwordChoice == 'no':
            isValidOpt= True

            isValidPass = False
            while isValidPass == False:
                customPassword = input('''Please input your preferred password.
                 Your password must possess the following:
                 Must not be less than 7 characters
                 Password must be in lower case
                 Must not contain a number or special character: \n''')

                if len(customPassword) >= 7:
                    isValidPass = True
                    password = customPassword
                    print('Your new password is: ', password)
                else:
                    print('Password cannot be taken. \nPlease read the password specifications and input your preferred password again: \n')
        else:
            print ('You have selected an invalid option, Please try again: \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, emailAdd, password, accountNumber]

    print('Welcome to GT Bank. \nYour account has been created, you can now proceed to login')
    print(' ****** ***** ******* ******')
    print('Your account number is: %d' %accountNumber)
    print('Your password is: %s' %password)
    print('Ensure you keep these information safe')
    print(' ****** ***** ******* ******')

    login()



def users_password(stringLength=5):
    letters = string.ascii_letters
    return ''.join(random.sample(letters, 5))


def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    userOption = int(input('What would like to do?: \n(1) deposit \n(2) withdrawal \n(3) balance enquiry \n(4) complaints \n(5) logout \n(6) exit: \n'))

    if(userOption ==1):
        depositOperation()
    elif(userOption == 2):
        withdrawalOperation()
    elif(userOption == 3):
        balanceOperation()
    elif(userOption == 4):
        complaintOperations()
    elif(userOption == 5):
        logout()
    elif(userOption == 6):
        exit()
    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    withdrawal = int(input('How much would you like to withdraw?: \n'))
    if withdrawal > accountBalance:
        print('Insufficient balance in your account')
        withdrawalOperation()
    else:
        print('You can now take your cash', withdrawal)
        performAnotherTransaction()



def depositOperation():
    amountDeposited = int(input('How much would you like to deposit? Please enter: \n'))
    print('You have deposited ', amountDeposited)
    print('Your new account balance is ', amountDeposited + accountBalance)
    performAnotherTransaction()


def balanceOperation():
    print ('Your Account Balance is: ', accountBalance)
    performAnotherTransaction()


def complaintOperations():
    print (input('''Thank you for choosing to air out your complaint
    Please tell us what your complaint is and one of our agents would talk to you: \n'''))
    print('Thank you for your submission')
    performAnotherTransaction()

def logout():
    login()

def performAnotherTransaction():
    for userDetails in database.items():
        choiceByUser = int(input('Would you like to perform another transaction?: (1) yes (2) no \n'))
        if choiceByUser == 1:
            bankOperation(userDetails)
        elif choiceByUser == 2:
            exit()
        else:
            print('You have selected an invalid option')
            performAnotherTransaction()



def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)



#### ACTUAL BANKING SYSTEM #####


initialize()
