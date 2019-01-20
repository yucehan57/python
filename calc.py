"""
Python 3.7.1
Author: Yucehan Kucukmotor
01/19/2019
Name of the Application: To the Power Calculator (TPC)
---Flow---:
1) Ask user how many numbers would s/he want to convert?
2) Create an empty list and by using control flow:
    3) Prompt users to input numbers one by one,
    4) Append numbers provided to the list 'numbers_list'
    5) Display updated list to user everyone a number is added
6) Ask user to what power s/he would like to take the numbers_list
7) Display the answer using list comprehension
-----------------------------------------------------------------
A function called TPC created as an update. It takes two arguments
1) x, how many numbers to be converted to the power k, our second argument?
2) k, to the power of what number?
TO IMPORT:
>>> from calc import TPC
Once function is run (i.e. TPC(2,4)), user is asked to provide
x numbers (e.g. TPC(2,4) -> it is 2 numbers, our first argument.
"""
# x = int(input("how many numbers would you like to convert? "))
# num = 1
# numbers_list = []
# while num <= x:
#     print("add number {}, please: ".format(num))
#     y = int(input())
#     numbers_list.append(y)
#     print("List to be converted: " , numbers_list)
#     num += 1
#
# print("\n")
# k = input("To the power of what?: ")
# print("Find answer below: ")
# print([j**int(k) for j in numbers_list])

#Convert the above program to a function
def TPC(x="how many numbers", k="to the power of what?"):
    # x = int(input("How many numbers do you want to convert?"))
    num = 1
    numbers_list = []
    while num <= x:
        print("add number {}, please: ".format(num))
        y = int(input())
        numbers_list.append(y)
        print("List to be converted: " , numbers_list)
        num += 1
        # k = int(input("to the power of what?"))
        print("answer is below:")
        print([j**k for j in numbers_list])
