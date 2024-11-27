import math
import string
#'''Question 1'''
# num1=int(input('Enter a Number::  '))
# add3=num1+3;
# multiply2=add3*2;
# sub3=multiply2-4;
# add3again=sub3+3;
# print(add3again)

# '''Question 2'''
# tempCelsius=int(input('Enter the temperatuer in Celsius::  '));
# ConvertIntoFarhenheit=((tempCelsius*1.8)+32)
# print(ConvertIntoFarhenheit)
# '''Question 3'''
# radius=int(input('ENter a radius '));
# Area=math.pi*radius**2;
# print(Area)

'''Question 4'''
#Ask user for their favourite color
# color = str(input("What's your favourite color? "))

# # Print the color 10 times without spaces, then 2 times with spaces
# print((color + "") * 10)
# print(color, color)
# print((color + "") * 10)
# '''Question 5'''

# name="\t\tAnas\n\t"
# print(name)
# print (name.rstrip())
# print(name.strip())
# print(name.lstrip())
#question 6

# num=int(input('Enter a number: '));
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
    
#question 7
# def describe_city(country='pakistan',city=''):
#     print(city,' is in ',country)
   
# describe_city(city='karachi') 
# describe_city(city='islamabad')
# describe_city(city='Dehli')

#question 8

# def Absolute_num(num):
#     if(num>0):
#         return abs(num)
#     else:
#         return 'number is negative there fore can no be absolute '
    
# print(Absolute_num(8.8))

#question 9


# def vowels_check(vowels,All_Letters):
#  for vowel in vowels:
#     for letter in All_Letters:
#         if(vowel==letter):
#             print(letter,'is vowel')
       
            
# vowels=['a','e','i','o','u','A','E','I','O','U']


# All_Letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# vowels_check(vowels,All_Letters)

# question 10
# def is_prime(num):
#     # Check if number is less than 2, not a prime
#     if num < 2:
#         return False

#     # Check for factors from 2 to the square root of num
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False  # Found a factor, not a prime number

#     return True  # No factors found, it is a prime number


# # Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is prime
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

#question 11
# num=6
# for i in range(num+1):
#     if i==3:
#         continue
#     else:
#         print(i)

#question 12
# Outer loop for the rows (1 to 5)
# for i in range(1, 6):
#     # Inner loop to print 'i', i times
#     for j in range(i):
#         print(i, end=" ")
#     # Move to the next line after each row
#     print()


#question 13

def findStageofPerson(age):
    if age<2:
        print('person is baby')
    elif age==4 | age <13:
        print('person is kid')
    elif age>=13 | age<20:
        print('person is teenage')
    elif age>=20 | age<65:
        print('petson is adult')
    elif age>=65:
        print('person is elder')

age=int(input('enter persons age: '))

findStageofPerson(age)