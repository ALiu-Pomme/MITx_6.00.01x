def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    product = base
    if exp == 0:
        return 1
    else:
        for num in range (0, exp-1):
            product *= base
        return product



base = float(input("base: "))
exp = int(input("exp: "))

print(iterPower(base, exp))
