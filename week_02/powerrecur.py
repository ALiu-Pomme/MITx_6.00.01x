def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    print ("current base: "+str(base))
    print ("current exp: "+str(exp))
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

base = float(input("base: "))
exp = int(input("exp: "))

print (recurPower(base, exp))
