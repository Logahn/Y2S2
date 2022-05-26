#!/usr/bin/env python3
# dec_val= int(input("Введите десятичное число: "))
# bin_val = int(input("Введите двоичное число: "))

# def DecimalToBinary(num):
# 	if num >= 1:
# 		DecimalToBinary(num // 2)
    
# 	print(num % 2, end = '')


# def binaryToDecimal(bin_val):
	
# 	binary1 = bin_val
# 	decimal, i, n = 0, 0, 0
# 	while(bin_val != 0):
# 		dec = bin_val % 10
# 		decimal = decimal + dec * pow(2, i)
# 		bin_val = bin_val//10
# 		i += 1
# 	print(decimal)

# print("\n")
# print(dec_val,"а двоичную систему: ", end = '')
# DecimalToBinary(dec_val)
# print("")
# print(bin_val,"на десятичную систему ", end ='')
# binaryToDecimal(bin_val) 

import collections

def toBASEint(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = abs(num)
    b = alpha[n % base] 
    while n >= base :
        n = n // base
        b += alpha[n % base] 
    return ('' if num >= 0 else '-') + b[::-1] 
    
def toBaseFrac(frac, base, n = 16) :
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = ''
    while n :
        frac *= base
        frac = round(frac,n)
        b += str(alpha[int(frac)])
        frac -= int(frac)
        n -= 1
    return b
recurr = []
	
Number = input("Number: ")
Basein = int(input("Initial base: "))
Baseout = int(input("Final base: "))
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if '.' in Number :
    num, frac = map(str,Number.split('.'))
    num = int(num,Basein)
    a = toBASEint(num,Baseout)
    b = 0
    k = Basein
    for i in frac :
        b += alpha.index(i) / k
        k *= Basein
    b = str(toBaseFrac(b, Baseout)).rstrip('0')
    res = [int(x) for x in str(b)]
    recurr = ([item for item, count in collections.Counter(res).items() if count > 1])
    print(f"Actual result: {a}.{b}")
    print(f"Numbers after floating poing: {res}")
    strings = [str(recurr) for recurr in recurr]
    recurr = "".join(strings)
    print(f"{a}.({recurr}) ") 
	
else :
    print(toBASEint(int(Number,Basein),Baseout))
