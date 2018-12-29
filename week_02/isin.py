#import time
#start_time = time.time()

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        if char == aStr[0]:
            return True
        else:
            return False
        
    elif char == aStr[int((len(aStr)-1)/2)]:
        return True
    else:
        if char < aStr[int((len(aStr)-1)/2)]:
            return isIn(char, aStr[0:int((len(aStr)-1)/2)+1])
        else:
            return isIn(char, aStr[int((len(aStr)-1)/2)+1:int(len(aStr))])


#char = input("char: ")
#aStr = input("aStr: ")
char = "a"
aStr = "abcdsfghi"
print (isIn(char, aStr))
#print("--- %s seconds ---" % (time.time() - start_time))
