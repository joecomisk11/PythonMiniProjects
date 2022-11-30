roman = {
    'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,
   
}

def RomanToDec(romanNum):
    sum = 0
    for i in range(len(romanNum) - 1):
        left = romanNum[i]
        right = romanNum[i + 1]
        if roman[left] < roman[right]:
            sum -= roman[left]
        else:
            sum += roman[left]
    sum += roman[romanNum[-1]]
    print(sum)
    return sum



#LXXXIV should print 84
RomanToDec('LXXXIV')