# working with string
print("giraffe \n academy")
print("giraffe \" academy")
# creating string variable
phrase= "girrafe academy"
print(phrase)
# functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[1])
print(phrase.index("acad"))
# working with numbers
print(2+5 )
my_num=-5
print(my_num)
print(str(my_num) + "my favorite number")
print(abs(my_num))
print(pow(5,2))
print(max(5,2))
print(min(5,2))
print(round(5.5))
# importing functions
from gettext import install, translation
from math import *
from platform import java_ver
from re import T
from wsgiref.simple_server import software_version
print(floor(3.9))
print(ceil(3.3))
print(sqrt(9))
# getting input from user
# name=input("Enter your name:")
# age=input("Enter your age:")
# print("hello " + name + "! You are "+ age +" years old")
#  building basic calculator
# num1=input("enter the first number:")
# num2=input("enter the second number:")
# add=float(num1)+float(num2)
# print(add)
#  mad libs game
# color=input("enter a color:")
# plural=input("enter a plural noun:")
# celebrity=input("enter a celebrity:")

# print("Roses are "+ color)
# print(plural+" are blue")
# print("I love "+ celebrity)
# lists
friends =["kelvin","muiz","saad","bola", "kola","ade"]
print(friends[1:3])
# list function
number=[4, 8, 35, 16, 12, 42]
# friends.extend(number)
print(friends)
friends.sort()
print(friends)
number.reverse()
print(number)
num = number.copy()
num.append(friends)
print(num)
# tuples in python: a container to store data(it it immutable)
coordinates = (4, 5)
print(coordinates[1])
# functions
def greet(name):
    print ("hi "+ name)
greet("mike")
def add(x,y):
    z=x+y
    print("the answer is "+ str(z))

add (4,5)
# using return statement in python function
def cube (num):
    return num*num*num
    
print(cube(3))  
# if statement
IsMale = False
if IsMale:
    print("you are a male")
else:
    print("you are not a male")  
def max(num1, num2, num3):
    if num1>=num2 and num1>=num3:
       return num1
    elif num2>=num1 and num2>=num3:
            return num2
    else:
       return num3
print(max(39,12,3))
# dictionaries
monthConversion = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
}
print(monthConversion["feb"])
print(monthConversion.get("mar"))
# while loop
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    print(sum)
    i +=1
# building a guessing game
# secretWord = "software"
# guess = ""
# count = 0
# limit = 3
# outOfGuess = False
# while guess != secretWord and not(outOfGuess):
#     if count < limit:
#         guess = input ("enter guess: ")
#         count += 1
#     else:
#         outOfGuess = True 
# if outOfGuess:
#     print( "you lost, try again") 
# else:     
#     print(" You won!")
# using for loop
for index in range(10):
    print(index)
for letter in "Giraffe Academy":
    print(letter)
# exponent function using for loop
def exponent(base, pow):
    result = 1
    for i in range (pow):
        result = result * base
    return result
    
print(exponent(3,4))
# 2 dimensional list and nested loop
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# print(number_grid [0][2])
# nested for loop
for row in number_grid:
    for column in row:
        print(column)
# building a translator
def translate(phrase):
     translation = ""
     for letter in phrase:
         if letter in "AEIOUaeiou":
             translation = translation + "g"
         else:
             translation = translation + letter
     return translation
print(translate(input("enter a phrase: ")))
def display_message():
    print("I am learning python")
    
display_message()
def favorite_book(title):
    print("one of my favorite book is: " + title)

favorite_book("pyhton crash course")
    
