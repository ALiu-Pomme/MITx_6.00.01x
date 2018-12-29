def upBalance(balance, annualInterestRate, monthlyPaymentRate):
    for month in range(0, 12):
        balance = (balance-(monthlyPaymentRate*balance))+(annualInterestRate/12.0)*(balance-monthlyPaymentRate*balance)
        #print (balance)
    return round(balance, 2)
'''
balance = float(input("balance: "))
annualInterestRate = float(input("annualInterestRate: "))
monthlyPaymentRate = float(input("monthlyPaymentRate: "))
'''
print("Remaining balance: "+str(upBalance(balance, annualInterestRate, monthlyPaymentRate)))
