def oddTuples(aTup):
    newTup = ()
    for num in range(0, len(aTup), 2):
         newTup = newTup+(aTup[num], )
    return newTup
