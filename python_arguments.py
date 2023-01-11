
# Example simple python arguments 
# Created by Laura Reed
# Created on 11/01/2023
#
# 

## Example of a Parameter - used inside the parentheses 

# def my_function (fname):
#     print("First name is: " + fname)

# my_function("Laura")
# my_function("Nick")

## There can be more than one parameter required by the fuction 

print("Enter 2 numbers to be added together ")
num1 = int(input("Enter the first number then press enter: "))
num2 = int(input("Enter the second number then press enter: "))
#sum = num1 + num2

def sum_two_numbers (num1, num2):
    sum = num1 + num2
    print(f"The sum of the numbers is {sum}")

sum_two_numbers(num1, num2)

