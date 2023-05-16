# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# problem 1: Get quotient of division of two numbers:
def problem_1():
    num1 = 20
    num2 = 4
    quotient = num1 / num2
    print(quotient)

# Problem 2 :Input four numbers and generate the sum of these:
def problem_2():
  num1 = input("Enter the first number:")
  num2 = input("Enter the second number:")
  num3 = input("Enter the third number:")
  num4 = input("Enter the fourth number:")
  total_sum = int(num1)+int(num2)+int(num3)+int(num4)
  print("The sum for four number is:",total_sum)

#Problem 3: Sum and average of marks of five students taken from the user:
def problem_3():
    stu1 = float(input("Enter the first student marks:"))
    stu2 = float(input("Enter the second student marks:"))
    stu3 = float(input("Enter the third student marks:"))
    stu4 = float(input("Enter the fourth student marks:"))
    stu5 = float(input("Enter the five student marks:"))
    sum =  stu1 + stu2 + stu3 + stu4 + stu5
    print("The sum for five student marks is:",sum)
    average = sum / 5
    print("The average of five student:",average)

#problem 4 : Percentage of total marks of four students:
def problem_4():
    s1 = 50
    s2 = 40
    s3 = 80
    s4 = 90
    sum = s1 + s2 + s3 + s4
    average = sum / 4
    percentage = (sum / 400) * 100
    print("Percentage of total marks of four students:",percentage,"%")

#problem 5: Check if a number is greater than 80, say “good”, if not say, “Try again”
def problem_5():
    number = int(input("Enter a number:"))
    if number > 80:
        print("Good")
    else:
        print("Try again")

#problem 6: Check whether a number is divisible by another user-given number or not:
def problem_6():
    num1 = 80
    num2 = int(input("Enter a number:"))
    if num1 % num2 == 0:
        print("Number is Divisible")
    else:
        print("Number is not Divisible")

#Problem 7 : Sum of odd numbers from 10 user-given numbers.
def problem_7():
    oddsum = 0
    for _ in range(10):
        n = int(input("Enter the end number : "))
        if n % 2 != 0:
             oddsum += n
        print("Sum of odd numbers is:",oddsum)

#problem 8: Sum of even number from n user-given numbers. Where n is also user-input
def problem_8():
    n = int(input("Enter the number of n: "))
    evensum = 0

    for i in range(n):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            evensum += number

    print("Sum of even numbers:", evensum)

# problem 9: Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
def problem_9():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)
    print("Temperature in Celsius:", celsius)

# problem 10: Calculating pay for an employee, given the hours worked and rate per hour.
def problem_10():
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_per_hour = float(input("Enter the rate per hour: "))
    pay = hours_worked * rate_per_hour
    print("Total pay:", pay)

#  Determine the status of a student (pass or fail) given his/her marks in a subject
# (passing marks = 50
def problem_11():
    marks = float(input("Enter the student's marks: "))
    passing_mark = 50

    if marks >= passing_mark:
        print("Pass")
    else:
        print("Fail")
#problem 12: Take two number from the user and determine the largest number
def problem_12():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    if num1 > num2:
        largest = num1
    else:
        largest = num2
    print("The largest number is:",largest)
#  Take four numbers from the user and determine the largest using the most suitable
# approach from a, b and c given above.
def problem_13():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    num3 = float(input("Enter the third number:"))
    num4 = float(input("Enter the forth number:"))
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        largest = num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        largest = num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        largest = num3
    else:
        largest = num4
    print("Larger number is:",largest)
#problem 14: Determine the grade of a student from the marks obtained (90-100, A; 80-29, B;
# 70-79, C; 60-69, D; <60, F)
def problem_14():
    marks = float(input("Enter the marks obtained: "))
    if marks >= 90 and marks <= 100:
        grade = "A"
    elif marks >= 80 and marks < 90:
        grade = "B"
    elif marks >= 70 and marks < 80:
        grade = "C"
    elif marks >= 60 and marks < 70:
        grade = "D"
    else:
        grade = "F"

    print("The grade is:", grade)
#problem 15: Show first n terms of Fibonacci series:
def problem_15():
    n = 10
    n1, n2 = 0, 1
    print("fibonacci series:",n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
#problem 16: Calculate pay of an employee based on the hours worked.....
def problem_16():
    hours = input("Enter hours:")
    h = float(hours)
    rate = input("Enter the rate:")
    x = float(rate)
    if h <= 40:
     print(h + x)
    elif h > 40:
     print (40 * x + (h - 40) * 1.5 * x)

#  Take three number from the user and determine the largest number.
# ⦁ First approach: using nested if-else
def problem_17():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))

    if a>b:
        if a>c:
            greater=a
        else:
            greater=c
    else:
        if b>c:
            greater=b
        else:
            greater=c

    # print the largest number
    print("Greater  = ",greater)

#  Second approach: using compound conditions
def problem_18():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if (num1 >= num2) and (num1 >= num3):
            largest = num1
    elif (num2 >= num1) and (num2 >= num3):
            largest = num2
    else:
            largest = num3

    print("The largest number is", largest)

# Third approach: call the first number the largest. Revise the estimate of
# the largest number after comparing it with the rest of the numbers one by
# one
def problem_19():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    largest = num1

    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    print("Largest number:", largest)

#problem 20: Input a number and determine whether the number is even or odd:
def problem_20():
    number = int(input("Enter a number:"))
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

# problem 21:Input 3 numbers. Determine whether: all are same, all are different or exactly two
# are same.
def problem_21():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    if num1 == num2 == num3:
        print("All numbers are the same.")
    elif num1 != num2 != num3 != num1:
        print("All numbers are different.")
    else:
        print("Exactly two numbers are the same.")

#problem 22: Finding the sum of 10 numbers taken from the user.
def problem_22():
    sum = 0
    for i in range(10):
        number = int(input("Enter a number: "))
        sum += number
    print("The sum is:", sum)

#problem 23:finding the sum of n numbers taken from the user. Where n is taken from the user
# as well.
def problem_23():
    n = int(input("Enter the number of n: "))
    sum = 0
    for i in range(n):
        number = int(input("Enter a number: "))
        sum += number
    print("The sum is:", sum)

#problem:24 Finding the average of n number from the user, where n is user-given value.

def problem_24():
    n = int(input("Enter the number of values: "))
    sum = 0
    for i in range(n):
        number = int(input("Enter a number: "))
        sum += number
        average = sum / n
    print("The average is:",average)

# problem 25: Displaying positive integers in the range from 1 to n, where n is taken from the user.
def problem_25():
    n = int(input("Enter a positive integer: "))
    for i in range(1, n + 1):
        print(i)

#problem 26: Calculate the factorial of a positive integer entered by the user
def problem_26():
    n = int(input("Enter a positive integer: "))
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print("The factorial of", n, "is:", factorial)

#problem 27: Take n numbers from the user and determine that how many positive and negative
# integers were entered by the user.
def problem_27():
    positive = 0
    negative = 0
    n = int(input("Enter the number of: "))

    for i in range(n):
        num = int(input("Enter an integer: "))
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
    print("Number of positive integers:", positive)
    print("Number of negative integers:", negative)

#problem 28: Take a positive integer n from the user. Display all the divisors of n
def problem_28():
    n = int(input("Enter a positive integer: "))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

#problem 29:




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # problem_1()
    # problem_2()
    # problem_3()
    # problem_4()
    # problem_5()
    # problem_6()
    # problem_7()
    # problem_8()
    # problem_9()
    # problem_10()
    # problem_11()
    # problem_12()
    # problem_13()
    # problem_14()
    # problem_15()
    # problem_16()
    # problem_17()
    # problem_18()
    # problem_19()
    # problem_20()
    # problem_21()
    # problem_22()
    # problem_23()
    # problem_24()
    # problem_25()
    # problem_26()
    # problem_27()
    problem_28()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/





