# !/usr/bin/env python3
# n = 29
# sum = 0
# for x in str(n):
#     sum += int(x)

# print(sum)
    



# def largestNumber(n):
#     large = (10 ** n) -1
#     print(large)

# largestNumber(2)

    


# def addTwoDigits(n):
#     sum = 0
#     for x in str(n):
#         sum += int(x)
#     return sum

# print(sum)

# import string
# s = "abacabad"
# x = s.split()
# # for x in range(len(s)):

# print(x)


# def circleOfNumbers(n, firstNumber):
#     x = n/2
#     if firstNumber == x:
#         return(0)
#     if firstNumber > x:
#         l = firstNumber - x
#         return(l)
#     else:
#         return(firstNumber + x)
        

# n = 10
# firstNumber = 2
# print(circleOfNumbers(n, firstNumber))

# def lateRide(n):
#     x = int(n/60)
#     y = n-(x*60)
#     x = str(x)
#     y = str(y)
#     sum1 = 0
#     sum2 = 0
#     for i in str(x):
#         sum1 += int(i)
#     for i in str(y):
#         sum2 += int(i)

#     final = sum1 + sum2
#     return(final)
# n = 807
# print(lateRide(n))

# def phoneCall(min1, min2_10, min11, s):
#     if s < min1:
#         x = 0
#     elif s == min1:
#         x = 1
#     elif s > min1 and s < 10:
#         min1_10 = s - min1
#         y = min1_10/min2_10
#         x = (int(y) + 1)
#     elif s > 11:
#         y = 9/min2_10
#         a = s - min1
#         b = a - (min2_10 * 9)
#         c = b/min11
#         x = int(c) + int(y) + 1
    
#     return x

# min1 = 3
# min2_10 = 1
# min11 = 2
# s = 20

# print(phoneCall(min1, min2_10, min11, s))


# def phoneCall(min1, min2_10, min11, s):
#     if s < min1:
#         x = 0
#     elif s == min1:
#         x = 1
#     elif s > min1 and s < 10:
#         min1_10 = s - min1
#         y = min1_10/min2_10
#         x = (int(y) + 1)
#     elif s > 11:
#         a = s - (min1 + (9*min2_10))
#         b = a/min11
#         x = (1 + 9 + int(b))            
    
#     return x

# min1 = 3
# min2_10 = 1
# min11 = 2
# s = 20

# print(phoneCall(min1, min2_10, min11, s))

# def centuryFromYear(year):
#     h = int(year/100)
#     if year < 100:
#         return(1)
#     if year%100 == 0:
#         return(h)
#     else:
#         if year > 100:
#             return(h+1)

# year = 1930
# x = centuryFromYear(year)
# print(x)


# def reachNextLevel(experience, threshold, reward):
#     if (experience + reward) > threshold-1:
#         return True
#     else:
#         return False
    
    
# experience = 10
# threshold = 15
# reward = 5
    
# print(reachNextLevel(experience, threshold, reward))



# def knapsackLight(value1, weight1, value2, weight2, maxW):
#     one = value1*weight1
#     two = value2*weight2
#     if weight1 > maxW:
#         return value2
#     if weight2 > maxW:
#         return value1
#     if weight1 > maxW and weight2>maxW:
#         return (0)
#     if (weight1 + weight2) <= maxW:
#         return (value1 + value2)
#     if (weight1 + weight2) > maxW:
#         if one > two:
#             return value1
#         else:
#             return value2

# value1 = 10
# weight1 = 5
# value2 = 6
# weight2 = 4
# maxW = 8
# x = knapsackLight(value1, weight1, value2, weight2, maxW)
# print(x)



# def knapsackLight(value1, weight1, value2, weight2, maxW):
#     one = value1+weight1
#     two = value2+weight2
#     if weight1 == maxW and weight1 >= weight2 and weight2 > maxW:
#         return value1
#     elif weight2 == maxW and weight2 >= weight1 and weight1 > maxW:
#         return value2
#     elif value1 == value2 and weight1 == weight2:
#         return value1
#     elif one == two:
#         if value1 > value2:
#             return value1
#         elif value2 > value1:
#             return value2
#     elif weight1 > maxW and weight2>maxW:
#         return (0)
#     elif (weight1 + weight2) <= maxW:
#         return (value1 + value2)
#     elif weight1 > maxW:
#         return value2
#     elif weight2 > maxW:
#         return value1
#     elif (weight1 + weight2) > maxW:
#         if one > two:
#             return value1
#         elif two > one:
#             return value2
    
    

# value1 = 10
# weight1 = 5
# value2 = 6
# weight2 = 4
# maxW = 8
# x = knapsackLight(value1, weight1, value2, weight2, maxW)
# print(x)


# def isInfiniteProcess(a, b):
#     x = True
#     while b > 1:
#         if a == b:
#             x = False
#         a += 1
#         b -= 1
#     if x is False:
#         return False
#     else:
#         return True 
        
         
# a = 2
# b = 6

# y = isInfiniteProcess(a, b)
# print(y)   



# def arithmeticExpression(a, b, c):
#     if a+b == c:
#         return True
#     elif a-b == c:
#         return True
#     elif a*b == c:
#         return True
#     elif a/b == c:
#         return True
#     else:
#         return False
        
# a = 2
# b = 3
# c = 5

# x = arithmeticExpression(a, b, c)
# print(x)


# def tennisSet(score1, score2):
#     if score1 == score2:
#         return False
#     elif score1 <= 6 and score2 < 5:
#         return True    
#     elif score1 < 5 and score2 <= 6:
#         return True
#     elif score1 >= 5 and score2 == 7:
#         return True
#     elif score2 >= 5 and score1 == 7:
#         return True
#     else:
#         return False
        
# score1 = 3
# score2 = 6

# print(tennisSet(score1, score2))

# a = int(input("a: "))
# b = int(input("b: "))
# count = 1
# if a % 2 == 0 and b % 2 == 0:
#     count +=1
# if a % 3 == 0 and b % 3 == 0:
#     count +=1
# if a % 5 == 0 and b % 5 == 0:
#     count += 1
# if a % 7 == 0 and b % 7 == 0:
#     count += 1

# print(count)

# N = 5
# A = [1, 2, 3, 4, 5]
# total = sum(A)
# avg = A/N # not checking for zero-divide because conditions say N > 1
# # x = floor(avg + 1)
# print(x)

# # Write your code here
# import numpy as np
# A= [1, 2, 3,4,5]

# for i in range(1, max(A)+1):
#     old = sum(A)
#     new = sum(i*np.ones(len(A)))
    
#     diff = new-old
#     if diff>0:
#         print(i)
#         break

# def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
# def turn_around():
#     turn_left()
#     turn_left()

# def end():
#     turn_right()
#     move()
#     turn_right()
#     drop()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     done()

# def drop():
#     while carries_object():
#         if wall_in_front():
#             toss()
            
# def pick():
#     while object_here():
#         take()
# def motion():
#     while front_is_clear() and wall_on_right():
#         move()
#         pick()
#         if wall_in_front():
#             turn_left()

# motion()
# end()
      

# def checkPalindrome(inputString):
#     if inputString == inputString[::-1]:
#         return True
#     else:
#         return False
        
# inputString = "Adeda"
# inputString = inputString.lower()
# x = checkPalindrome(inputString)
# print(x)

# def adjacentElementsProduct(inputArray):
#     largest_element = inputArray[0]
#     second_largest = inputArray[0]
    
#     smallest_element = inputArray[0]
#     second_smallest = inputArray[0]
    
#     for x in range(len(inputArray)):
#         if inputArray[x] > largest_element:
#             largest_element = inputArray[x]
    
#     for y in range(len(inputArray)):
#          if inputArray[y] < largest_element:
#             if inputArray[y] > second_largest:
#                 second_largest = inputArray[y]
    
#     for x in range(len(inputArray)):
#         if inputArray[x] < smallest_element:
#             smallest_element = inputArray[x]
    
#     for y in range(len(inputArray)):
#          if inputArray[y] > smallest_element:
#             if inputArray[y] < second_smallest:
#                 second_smallest = inputArray[y]
    
#     largest_pos_prod = largest_element * second_largest
#     largest_neg_prod = smallest_element * second_smallest
    
#     if largest_pos_prod > largest_neg_prod:
#         return largest_pos_prod
#     else:
#         return largest_neg_prod

# inputArray = [4,3,9,2,4,-5,-3]    
# x = adjacentElementsProduct(inputArray)
# print(x)
   
    
# inputArray = [4,3,9,2,4,-5,-3,]     
# def adjacentElementsProduct(inputArray):
#     largest_element = 0
        
#     for x in range(len(inputArray)-1):
#         y = (inputArray[x] * inputArray[x+1])
#         if y > largest_element:
#             largest_element = (inputArray[x]* inputArray[x+1])
#     print(largest_element)
    
# adjacentElementsProduct(inputArray)
 


# print("Accessing Students Interest in the class")

# print("To access the student's level of interest in the class, \nenter the following factors as seen on faces ")

# student_names = []
# student_score = []

# student_number = int(input("Number of students in class: "))
# for x in range(student_number):
#     name = str(input(f"{x+1}. Enter student name: "))
#     joy = int(input("Level of Joy(%): "))
#     smile = int(input("Level of smile(%): "))
#     anger = int(input("Level of anger(%): "))
#     contribution = int(input("Level of contribution(%): "))
#     interest = int(input("Level of interest(%): "))
#     print("\n")
#     result = ((((2*joy)+(2*smile)+(2*contribution)+(2*interest))/8) + anger)/2 
#     student_names.append(name)
#     student_score.append(result)
# for x in range(len(student_names)):
#     print(f"{student_names[x]} : {student_score[x]}%")




# N = int(input("Value for N = "))
# M = int(input("Value for M: "))

# arr = []
# for x in range(M):
#     element = input("Element:")
#     arr.append(element)

# print(arr)

# import time
# from playsound import playsound

# mp3File = "/home/logan/VS Code Projects/Python/others/single beep.mp3"

# playsound(mp3File)
# for x in range(2):
#     playsound(mp3File) 

# single_beep = "/home/logan/VS Code Projects/Python/others/single_beep2.mp3"
# double_beep = "/home/logan/VS Code Projects/Python/others/double_beep2.mp3"
# def dit():
#     playsound(single_beep)

# def dah():
#     playsound(double_beep)

# morse_code = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.", 
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     " ": " ",
# }
# def sound():
#     if letter == "A": 
#         dit()
#         dah()
#     elif letter == "B":
#         dah()
#         dit()
#         dit()
#         dit()
#     elif letter == "C":
#         dah()
#         dit()
#         dah()
#         dit()
#     elif letter == "D":
#         dah()
#         dit()
#         dit()
#     elif letter == "E":
#         dit()
#     elif letter == "F":
#         dit()
#         dit()
#         dah()
#         dit()
#     elif letter == "G":
#         dah()
#         dah()
#         dit()
#     elif letter == "H":
#         dit()
#         dit()
#         dit()
#         dit()
#     elif letter == "I":
#         dit()
#         dit()
#     elif letter == "J":
#         dit()
#         dah()
#         dah()
#         dah()
#     elif letter == "K":
#         dah()
#         dit()
#         dah()
#     elif letter == "L":
#         dit()
#         dah()
#         dit()
#         dit()
#     elif letter == "M":
#         dah()
#         dah()
#     elif letter == "N":
#         dah()
#         dit()
#     elif letter == "O":
#         dah()
#         dah()
#         dah()
#     elif letter == "P":
#         dit()
#         dah()
#         dah()
#         dit()
#     elif letter == "Q":
#         dah()
#         dah()
#         dit()
#         dah()
#     elif letter == "R":
#         dit()
#         dah()
#         dit()
#     elif letter == "S":
#         dit()
#         dit()
#         dit()
#     elif letter == "T":
#         dah()
#     elif letter == "U":
#         dit()
#         dit()
#         dah()
#     elif letter == "V":
#         dit()
#         dit()
#         dit()
#         dah()
#     elif letter == "W":
#         dit()
#         dah()
#         dah()
#     elif letter == "X":
#         dah()
#         dit()
#         dit()
#         dah()
#     elif letter == "Y":
#         dah()
#         dit()
#         dah()
#         dah()
#     elif letter == "Z":
#         dah()
#         dah()
#         dit()
#         dit()

         
 
     
    
# out = []
# word = input('Statement: ')
# word = word.upper()
# for letter in word:
#     out.append(morse_code[letter])
#     sound()
#     out.append("|")
#     time.sleep(0.2)
# out = "".join(out)
# print(f"Morse Encryption : {out}")




# def shapeArea(n):
#     start = 1
#     for x in range(n):
#         start += 2
#         mid = start
#         for x in range(n-1):
#             next = 

def shapeArea(n):
    n = int(input("n = "))
    middle_row = (n*2)-1
    side_sum = 0
    for x in range(n):
        row = ((n-x)*2)-1
        side_sum += row
    side_sum = side_sum - middle_row
    full_sum =  side_sum * 2
    total = middle_row + full_sum
    return total

n = 5
x = shapeArea(n)
print(x)

def makeArrayConsecutive2(statues):
    largest = statues[0]
    smallest = statues[0]
    for x in range(len(statues)):
        if statues[x] > largest:
            largest = statues[x]
    for x in range(len(statues)):
        if statues[x] < smallest:
            smallest = statues[x]
    n = 1 + largest - smallest - len(statues)
    return n

statues = [4, 6, 7, 3, 10, 5]
x = makeArrayConsecutive2(statues)
print(x)




