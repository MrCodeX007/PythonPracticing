"""
name = input("Enter your name: ")
print(name)
print(type(name))

num = input ("Enter any number: ")
print(num)
print(type(num))

#explicitly to int
num1 = int(input("Enter any number: "))
print(num1)
print(type(num1))

"""
# Python program to take integer input  in Python
 
# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)   # printing the list
