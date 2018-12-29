def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        gcd = a
    else:
        gcd = b
    while a%gcd != 0 or b%gcd != 0:
            """
            print ("current gcd: " +str(gcd))
            print ("a%gcd: "+str(a%gcd))
            print ("b%gcd: "+str(b%gcd))
            """
            gcd -= 1
           
            #print("new gcd: "+str(gcd))           
    return gcd


a = int(input("a: "))
b = int(input("b: "))


print (gcdIter(a,b))
print (gcdIter(a, b)+1)
