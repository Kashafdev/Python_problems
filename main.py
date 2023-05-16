# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Get quotient of division of two numbers
def problem_1():
    num1 = 10
    num2 = 2
    print(num1 / num2)

# Input four numbers and generate the sum of these
def problem_2():
    num1 = int(input("Enter the first num"))
    num2 = int(input("Enter the second num"))
    num3 = int(input("Enter the third num"))
    num4 = int(input("Enter the forth num"))
    Sum = num1 + num2 + num3 + num4
    print("The sum of these numbers are:", Sum)

# Sum and average of marks of five students taken from the user
def problem_3():
    std1 = int(input("Enter the first std"))
    std2 = int(input("Enter the second std"))
    std3 = int(input("Enter the third std"))
    std4 = int(input("Enter the forth std"))
    std5 = int(input("Enter the fifth std"))
    Sum = std1 + std2 + std3 + std4 + std5
    print("The sum of marks of Five students are:", Sum)
    Average = (std1 + std2 + std3 + std4 + std5) / 5
    print("The average of marks of five students is:", Average)

# Percentage of total marks of four students
def problem_4():
    std1 = 97
    std2 = 89
    std3 = 98
    std4 = 87
    total = std1 + std2 + std3 + std4
    Average = total / 4
    percentage = (total / 400) * 100
    print("The percentage of four students is:", percentage, "%")

# Check if a number is greater than 80, say “good”, if not say, “Try again”
def problem_5():
    num = int(input("Enter the number"))
    if num > 80:
        print("good")
    else:
        print("Try again")

# Check whether a number is divisible by another user-given number or not
def problem_6():
    num1 = 20
    num2 = int(input("Enter the number"))
    if num1 % num2 == 0:
        print("num1 is divisible by num2")
    else:
        print("num1 is not divisible by num2")

# Sum of odd numbers from 10 user-given numbers
def problem_7():
    n = int(input("Enter the number"))
    print(sum([i for i in range(1, n + 1, 2)]))

# Sum of even number from n user-given numbers. Where n is also user-input.
def problem_8():
    n = int(input("Enter the number"))
    print(sum([i for i in range(2, n+1, 2)]))

# Show first n terms of Fibonacci series
def problem_9():
    n = 10
    n1, n2 = 0, 1
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

# Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
def problem_10():
    F = float(input("Enter the temperature in F"))
    C = (F-32) * (5/9)
    print(C)

# Calculating pay for an employee, given the hours worked and rate per hour.
def problem_11():
    hours = int(input('Enter total number of hours worked: '))
    rate = int(input('Enter per hour payment in $: '))
    def calculate_pay(hours, rate):
        if hours > 40:
            extra_hours = hours - 40
            total_pay = 40 * rate + extra_hours * 1.5 * rate
            return total_pay

        return hours * rate
    print('pay: ${}'.format(calculate_pay(hours, rate)))

# Determine the status of a student (pass or fail) given his/her marks in a subject  (passing marks = 50)
def problem_12():
    subMarks = int(input("Enter the subject marks"))
    if subMarks >= 50:
        print("Pass")
    else:
        print("Fail")

# Calculate pay of an employee based on the ..............about overtime pay
def problem_13():
    hrs = input("Enter Hours:")
    h = float(hrs)
    xx = input("Enter the Rate:")
    x = float(xx)
    if h <= 40:
        print(h * x)
    elif h > 40:
        print(40 * x + (h - 40) * 1.5 * x)

#  Take two number from the user and determine the largest number
def problem_14():
    num1 = int(input("Enter the First number"))
    num2 = int(input("Enter the second number"))
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    print(larger)

# Take four numbers from the user and determine the largest using the most suitable
# approach from a, b and c given above.
def problem_16():
    num1 = int(input("Enter the First number"))
    num2 = int(input("Enter the second number"))
    num3 = int(input("Enter the third number"))
    num4 = int(input("Enter the forth number"))
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        larger = num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        larger = num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        larger = num3
    else:
        larger = num4
    print(larger)

# Determine the grade of a student from the marks obtained (90-100, A; 80-29, B;
# 70-79, C; 60-69, D; <60, F)
def problem_17():
    marks = float(input("Enter the marks"))
    if marks >= 90 and marks < 100:
        print("Grade: A")
    elif marks >= 80 and marks < 90:
        print("Grade: B")
    elif marks >= 70 and marks < 80:
        print("Grade: C")
    elif marks >= 60 and marks < 70:
        print("Grade: D")
    else:
        print("Grade: F")

# Input a number and determine whether the number is even or odd.
def problem_18():
    num = int(input("Enter the number"))
    if num % 2 == 0 :
        print("Even Number")
    else:
        print("Odd Number")

# Calculate the difference between two times given in 24-hour (hh: mm) format.
def problem_19():
    # time1= float(input("Enter the time1"))
    # time2 = float(input("Enter the time2"))
    # hours, minutes = calculate_time_difference(time1, time2)
    # print("hours, mintues")

# Input 3 numbers. Determine whether: all are same, all are different or exactly two
# are same.
def problem_20():
    num1 = int(input("Enter the First number"))
    num2 = int(input("Enter the second number"))
    num3 = int(input("Enter the third number"))
    if num1 == num2 and num2 == num3:
        print("All are same")
    elif num1 != num2 and num2 != num3 and num1 != num3:
        print("All are different")
    else:
        print("Exactly two are same")

# Finding the sum of 10 numbers taken from the user.
def problem_21():
    n = 0

    for i in range(0, 10):
        a = int(input("Enter the number"))
        n += a

    print(n)

# Finding the sum of n numbers taken from the user. Where n is taken from the user
# as well.
def problem_22():
    n = int(input("Enter the number of n: "))
    sum = 0

    for i in range(n):
        a = int(input("Enter the number"))
        sum += a

    print(sum)

#  Finding the average of n number from the user, where n is user-given value.
def problem_23():
    n = int(input("Enter number of n:"))
    sum = 0

    for num in range(1, n + 1, 1):
        sum = sum + num
    print("Sum of first ", n, "numbers is: ", sum)
    average = sum / n
    print("Average of ", n, "numbers is: ", average)

# Displaying positive integers in the range from 1 to n, where n is taken from the user.























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
    # problem_11()
    # problem_12()
    # problem_13()
    # problem_14()
    # problem_16()
    # problem_17()
    # problem_18()
    # problem_20()
    # problem_21()
    # problem_22()
    problem_23()















