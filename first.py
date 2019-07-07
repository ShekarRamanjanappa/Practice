balance = 2000
password = 1234
chance = 3
while chance >0:
    code = int(input('enter the password'))
    if code==password:
        print('press 1 for checking the balance')
        print('press 2 for withdrawing')
        print('press 3 for deposite ')

        option = int(input('enter the option'))
        if option == 1:
            print('Your current balcance is: ', balance)
            break
        if option == 2:
            withdraw=int(input('Enter the amount '))
            while withdraw<balance:
                balance -= withdraw
                print('Amount withdrawn ', withdraw)
                print('your current balance is ',balance)
                break
            else:
                print('sorr!, your balance is only',balance,'please withdraw below balance')
                print('if you want to continue press 1 if you want to exit press 4')
                option=int(input(' Enter your option here : '))
        else:
            chance-=1
            print('Account Blocked')
        if option == 3:
            deposite = int(input(' Enter the amount to deposite'))
            balance = balance + deposite
            print('your account balance after deposite is ', balance)
        if option ==4:
            break




















'''

'isinstance(balance, float)'
'raise AssertionError ('message') # Fails when the input password is less than 4 variable'

'''
