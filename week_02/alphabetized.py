s = "bacd"
longstr = s[0]
for i in range(len(s)):
    """
    print("out")
    print("i: " + str(i))
    print("startlong: " + longstr)
    """
    tempstr = s[i]
#    print("starttemp: " + tempstr)
    for n in range(i, len(s)):
        """
        print("in")
        print("n: " + str(n))
        """
        if n == len(s)-1:
            break
        if s[n] <= s[n+1]:
            tempstr = tempstr + s[n+1]
#            print("temp: " + tempstr)
        else:
            break
    if len(tempstr) > len(longstr):
        longstr = tempstr
#        print("newlong: "+longstr)


print ("Longest substring in alphabetical order is: "+longstr)
