def genPrimes():
    prime1 = 2
    existing_primes = []
    while True:
        for item in existing_primes:
            if prime1%item == 0:
                prime1 += 1
                break
        else:
            existing_primes.append(prime1)
            yield prime1
        
        
        
