import time
start_time = time.time()
def minMonth(balance, annualInterestRate, pay):
    for month in range(12):
        balance = (balance-pay)+((annualInterestRate/12.0)*(balance-pay))
    if balance <= 0:
        return pay
    else:
        return minMonth(tempbalance, annualInterestRate, pay+10)
'''
balance = float(input("balance: "))
annualInterestRate = float(input("annualInterestRate: "))
'''
tempbalance = balance
print("Lowest Payment: "+str(minMonth(balance, annualInterestRate, 10)))
print("--- %s seconds ---" % (time.time() - start_time))
