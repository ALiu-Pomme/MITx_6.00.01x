def minBisect(balance, annualInterestRate, upperBound, lowerBound):
    pay = (upperBound+lowerBound)/2
    for month in range(12):
        balance = (balance-pay)+((annualInterestRate/12.0)*(balance-pay))
    if round(balance, 2) == 0:
        return round(pay, 2)
    elif balance > 0:
        lowerBound = pay       
    elif balance < 0:
        upperBound = pay
    return minBisect(tempBalance, annualInterestRate, upperBound, lowerBound)
        

balance = int(input())
tempBalance = balance
annualInterestRate = int(input())
lowerBound = balance/12.0
upperBound = (balance * (1 + annualInterestRate/12.0)**12)/12.0

print("Lowest Payment: "+str(minBisect(balance, annualInterestRate, upperBound, lowerBound)))
