def minBisect(balance, annualInterestRate, pay):
    for month in range(12):
        balance = (balance-pay)+((annualInterestRate/12.0)*(balance-pay))
    if balance == 0:
        return round(balance, 2)
    elif balance > 0:
        lowerBound = pay       
    elif balance < 0:
        upperBound = pay
    return minBisect(balance, annualInterestRate, (upperBound+lowerBound)/2)
        

balance = 32000
annualInterestRate = 0.2
lowerBound = balance/12.0
upperBound = (balance * (1 + annualInterestRate/12.0)**12)/12.0

print("Lowest Payment: "+str(minBisect(balance, annualInterestRate, (upperBound+lowerBound)/2)))
