def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance+money))
    return balance + money

balance = 0
balance = deposit(balance,1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다 잔액은 {0}원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance

balance=0
balance=deposit(balance, 1000)
print(balance)
balance=withdraw(balance,500)
print(balance)

def withdraw_night(balance, money):
    commission=100
    return commission, balance-money-commission

commission, balance = withdraw_night(balance,500)
print("수수료 {0}원 이며 잔액은 {1}원입니다.".format(commission,balance))