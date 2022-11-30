'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
'''
def toHex(num: int) -> str:
        if num < 0: 
            num = num + 2**32
        ret = ''
        d = '0123456789abcdef'
        while num >= 16:
            a = num % 16
            ret += str(d[a])
            num //= 16
        ret += d[num]
        return ret[::-1]

#should print "1a"
print(toHex(26))

#should print "ffffffff"
print(toHex(-1))
