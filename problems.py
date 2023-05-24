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
  #   Input 4 number
  num1 = input("Enter the first number:")
  num2 = input("Enter the second number:")
  num3 = input("Enter the third number:")
  num4 = input("Enter the fourth number:")
  # sum of 4 number
  total_sum = int(num1)+int(num2)+int(num3)+int(num4)
  print("The sum for four number is:",total_sum)

#Problem 3: Sum and average of marks of five students taken from the user:
def problem_3():
    # input stu marks
    stu1 = float(input("Enter the first student marks:"))
    stu2 = float(input("Enter the second student marks:"))
    stu3 = float(input("Enter the third student marks:"))
    stu4 = float(input("Enter the fourth student marks:"))
    stu5 = float(input("Enter the five student marks:"))
    # stu marks sum
    sum =  stu1 + stu2 + stu3 + stu4 + stu5
    print("The sum for five student marks is:",sum)
    # stu average
    average = sum / 5
    print("The average of five student:",average)

#problem 4 : Percentage of total marks of four students:
def problem_4():
    # input stu marks
    s1 = 50
    s2 = 40
    s3 = 80
    s4 = 90
    # sum and average stu marks
    sum = s1 + s2 + s3 + s4
    average = sum / 4
    # percentage of stu
    percentage = (sum / 400) * 100
    print("Percentage of total marks of four students:",percentage,"%")

#problem 5: Check if a number is greater than 80, say “good”, if not say, “Try again”
def problem_5():
    # input num
    number = int(input("Enter a number:"))
    if number > 80:
        print("Good")
    else:
        print("Try again")

#problem 6: Check whether a number is divisible by another user-given number or not:
def problem_6():
    #todo what if he devide by zero ??
    num1 = 80
    num2 = int(input("Enter a number:"))
    # conditions
    if num2 == 0:
        print("Cannot divide by zero.")
    elif num1 % num2 == 0:
        print("Number is Divisible")
    else:
        print("Number is not Divisible")

#Problem 7 : Sum of odd numbers from 10 user-given numbers.
def problem_7():
    #fixme what if user enter some even and some odd no=umber the program will end after 10 inputs before getting 10 odd numbers from the user
    oddsum = 0
    count = 0
    # while loop
    while count < 10:
        n = int(input("Enter a number: "))
        if n % 2 != 0:
            oddsum += n
            count += 1

    print("Sum of odd numbers is:", oddsum)


#problem 8: Sum of even number from n user-given numbers. Where n is also user-input
def problem_8():
    evensum = 0
    count = 0
    # while loop
    while count < 10:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            evensum += number
            count += 1

    print("Sum of even numbers:", evensum)

# problem 9: Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
def problem_9():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    # formula
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
    # input student marks
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
    #fixme if both are equal ? then what ?

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
    rate = float(input("Enter the rate:"))
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
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number"))

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

# Calculate the difference between two times given in 24-hour (hh: mm) format.
#fixme use time library i.e deltatime
time1 = input("Enter the first time (hh:mm): ")
time2 = input("Enter the second time (hh:mm): ")

hours1, minutes1 = map(int, time1.split(':'))
hours2, minutes2 = map(int, time2.split(':'))

total_minutes1 = hours1 * 60 + minutes1
total_minutes2 = hours2 * 60 + minutes2

difference_minutes = abs(total_minutes2 - total_minutes1)

difference_hours = difference_minutes // 60
difference_minutes = difference_minutes % 60
print(f"The difference is {difference_hours} hours and {difference_minutes} minutes.")





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

#problem 29:  Display negative of a number
def problem_29():
    num = 5
    negative_num = -num
    print("Negative of", num, "is", negative_num)

#  Take two positive integers a and n from the user. Calculate and display an. Assume
# that the power operator is not available.
def problem_30():
    a = int(input("Enter a positive integer : "))
    n = int(input("Enter a positive integer : "))
    result = 1
    for _ in range(n):
        result *= a
    print(result)

#  Take three number from the user and determine the largest number. Do it using a
# loop
def problem_31():
    largest = None
    for i in range(3):
        num = float(input("Enter a number: "))
        if largest is None or num > largest:
            largest = num
    print(largest)

#problem 32 :Input a positive integer from the user and determine where the number is a perfect
# number or not. (a perfect number is a positive integer that is equal to the sum of its
# proper positive divisors, that is, the sum of its positive divisors excluding the number
# itself.)
def problem_32():
    num = int(input("Enter a positive integer: "))
    divisors = 0
    for i in range(1, num):
        if num % i == 0:
            divisors += i

    if divisors == num:
        print(num, "is a perfect number.")
    else:
        print(num, "is not a perfect number.")

#problem 33: Find absolute of an input. Assume that the absolute operator is not available.
def problem_33():
    num = float(input("Enter a number: "))
    if num < 0:
        abs_value = -num
    else:
        abs_value = num
    print("The absolute value of", num, "is", abs_value)

#problem 34: Take n number from the user and determine the largest number entered by the user,
# where n is taken from the user as well.
def problem_34():

    n = int(input("enter the number of values: "))
    largest = None

    for i in range(n):
     num = float(input("Enter a number: "))
    if largest is None or num > largest:
       largest = num

    print(largest)


# problem 35: Take n numbers from the user and determine both the smallest and the largest
# number entered by the user, where n is taken from the user as well.
def problem_35():
    n = int(input("enter the number of values: "))
    largest = None
    smallest = None

    for i in range(n):
       num = float(input("Enter a number: "))
       if smallest is None or num < smallest:
            smallest = num
       if largest is None or num > largest:
             largest = num
    print(smallest)
    print(largest)

# problem 36: Input 2 number and find if both are even, both are odd, or 1 even 1 odd.
def problem_36():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both numbers are even.")
    elif num1 % 2 != 0 and num2 % 2 != 0:
        print("Both numbers are odd.")
    else:
        print("One number is even and one is odd.")

# problem 37: Input 3 numbers and find how many are odd.
def problem_37():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    odd = 0
    if num1 % 2 != 0:
        odd += 1

    if num2 % 2 != 0:
        odd += 1

    if num3 % 2 != 0:
        odd += 1

    print("Number of odd numbers:", odd)

#problem 38:Input 3 numbers and print the 2 largest numbers/
def problem_38():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    sum = num1 + num2 + num3
    sec_largest = sum - largest - smallest
    print("The two largest numbers are:", largest, "and", sec_largest)


#problem 39:Input a number and find if it is 2-digit positive integer or not.
def problem_39():
    #fixme what if I enter negative number ??
    number = int(input("Enter a number: "))
    if number > 9 and number < 100:
        print("The number is a 2-digit positive integer.")
    else:
        print("The number is not 2-digit positive integer.")


#problem 40 :Input a 2-digit number and find the absolute difference between its digits
def problem_40():
    number = int(input("Enter a 2-digit number: "))
    tens_digit = number // 10
    ones_digit = number % 10
    ab_difference = abs (tens_digit - ones_digit)
    print(ab_difference)

# problem 41: Input an integer (up to 4 digits) and store its reverse in another variable. Then
# display both integers
def problem_41():
    #todo do it without list comrihenshen
    number = int(input("Enter an integer up to 4 digits: "))
    reversed_number = int(str(number)[::-1])
    print("Reversed number:", reversed_number)

#problem 42:Interchange two numbers
def problem_42():
    #todo what if you're not using python
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    num1, num2 = num2, num1

    print("swapping:")
    print("num1 =", num1)
    print("num2 =", num2)

# problem 43: Interchange two numbers without using an extra variable.
def problem_43():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    print("After swapping:")
    print("num1 =", num1)
    print("num2 =", num2)

#problem 44 : Multiply a number with the sum of its digits.
def problem_44():
    number = 1234
    digit_sum = sum(int(digit) for digit in str(number))
    result = number * digit_sum
    print(result)
    sum = 0
    for num in str(number):
        sum += int(num)


# problem 45:Input 2 numbers and print YES if 1st is divisible by 2nd
def problem_45():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 % number2 == 0:
        print("YES")
    else:
        print("NO")

# problem 46: Input 2 numbers and print YES if 2nd is divisible by 1st
def problem_46():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number2 % number1 == 0:
        print("YES")
    else:
        print("NO")
# problem 47: Input 2 numbers and print YES if one number is divisible by the other.
def problem_47():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 % number2 == 0 or number2 % number1 == 0:
        print("YES")
    else:
        print("NO")

# problem 48: Input numbers till user inputs a zero and display their sum
def problem_48():
    sum = 0
    num = int(input("Enter a number: "))
    while num != 0:
        sum += num
        num = int(input("Enter a number: "))
    print("The sum of the entered numbers is:", sum)

# problem 49: Input numbers till user inputs a zero and display the largest number
def problem_49():
    largest = 0

    while True:
        number = int(input("Enter a number: "))
        if number == 0:
            break
        if number > largest:
            largest = number
    print("The largest number entered is:", largest)

# problem 50: Input 10 numbers, and display the smallest number
def problem_50():
    smallest = None

    for _ in range(10):
        number = int(input("Enter a number: "))
        if smallest is None or number < smallest:
            smallest = number

    print("The smallest number enter is :", smallest)

# problem 51:Input 10 numbers, and display count of even and odd numbers, separately, at the
# end
def problem_51():
    count_even = 0
    count_odd = 0

    for _ in range(10):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    print("Count of even numbers:", count_even)
    print("Count of odd numbers:", count_odd)

#problem 52:input SLimit and Elimit from the user, and display even numbers between range,
# with both limit, included.
def problem_52():
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))
    for num in range(start_limit, end_limit + 1):
        if num % 2 == 0:
            print(num)

#problem 53: Input SLimit and ELimit from the user and display only those numbers between
# range which are divisible by 2 or 3 or 5, with both limits included
def problem_53():
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))
    for num in range(start_limit, end_limit + 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            print(num)


# problem 54: Input 2 numbers and find their GCD
def problem_54():
    #fixme what if you're not using python
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    gcd = num1
    print("The GCD of", num1, "and", num2, "is:", gcd)


 #problem 55: Input a number and display that how many digits it has
def problem_55():
    number = int(input("Enter a number: "))

    digit_count = len(str(abs(number)))

    print("The number", number, "has", digit_count, "digits.")

#problem 56: Input a positive integer from the user and determine whether is a prime number or
# not
def problem_56():
    num = int(input("Enter a positive integer: "))
    if num <= 1:
        print(num, "is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")


# problem 57: Take a positive integer from the user. Displaying an error message and prompting
# for input again and again if the user enters invalid input (negative or zero)
def problem_57():
    while True:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            break

    print("Valid input received:", num)


# problem 58:Write an algorithm to determine the sum of a variable number of positive integers
# taken from the user. The algorithm should keep prompting the user for more input
# until the user enters the sentinel value -999.
def problem_58():
    sum_of_integers = 0
    while True:
        num = int(input("Enter a positive integer: "))
        if num == -999:
            break
        elif num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            sum_of_integers += num
    print("Sum of the positive integers:", sum_of_integers)

#problem 59: Find absolute of an input. Assume that the absolute operator is not available.
def problem_59():
    def absolute_value(num):
        if num < 0:
            return -num
        else:
            return num

    input_num = -5
    abs_num = absolute_value(input_num)
    print(abs_num)

#problem 60:Input numbers till user inputs a zero, and display the smallest number
# Check if it works for all positive inputs
# Now check algorithm # 55 (largest number) if it works for all negative inputs
# If you find any problem, then solve it.
def problem_60():
    smallest_num = None
    num = None
    while num != 0:
        num = int(input("Enter a number: "))
        if num != 0:
            if smallest_num is None or num < smallest_num:
                smallest_num = num
    print(smallest_num)
    largest_num = None
    num = None
    while num != 0:
        num = int(input("Enter a number: "))
        if num != 0:
            if largest_num is None or num > largest_num:
                largest_num = num
    print(largest_num)

# problem 61:Input 3 numbers and find their GCD
def problem_61():
    #fixme without using python
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))

    while num2 != 0:
        num1, num2 = num2, num1 % num2
    gcd = num1
    print("The GCD of the three numbers is:", gcd)

# problem 62: Input 2 numbers and display their LCM
def problem_62():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    a = num1
    b = num2
    while b != 0:
        a, b = b, a % b
    lcm = (num1 * num2) // a
    print("The LCM of the two numbers is:", lcm)

#problem 63:Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
# the input will be entered in order from least significant to most significant. Since
# valid digits are 0 to 8, hence any other input will be used as the sentinel value.
def problem_63():
    #todo do it your self
    base9_num = 0
    power = 0
    while True:
        digit = int(input("Enter the number: "))
        if digit < 0 or digit > 8:
            break
        base9_num += digit * (9 ** power)
        power += 1
    print(base9_num)


#problem 64 Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
# the input will be entered in order from most significant to least significant. Since
# valid digits are 0 to 8, hence any other input will be used as sentinel value.
def problem_64():
    base9_num = 0
    power = 0
    digit = int(input("Enter the number: "))

    while 0 <= digit <= 8:
        base9_num += digit * (9 ** power)
        power += 1
        digit = int(input("Enter the next digit (0-8) or any other value to stop: "))

    print("Decimal equivalent:", base9_num)


# problem 65: Input a number and display its equivalent in base-9 (one digit per line, starting from
# the least significant)

def problem_65():
    number = int(input("Enter a number: "))
    result = []
    while number > 0:
        digit = number % 9
        result.append(digit)
        number //= 9
    if len(result) == 0:
        result.append(0)
    result.reverse()
    print("Equivalent in base-9:")
    for digit in result:
        print(digit)

#problem 66: Input number and store its equivalent in base-9 as a single numeric value and
# display it
def problem_66():
    number = int(input("Enter a number: "))

    result = 0
    multiplier = 1
    while number > 0:
        digit = number % 9
        result += digit * multiplier
        number //= 9
        multiplier *= 10
    print("Equivalent in base-9:", result)

#problem 67: Input a base-9 number, digit by digit, then convert it into binary number a single
# numeric value. Digits of the input will be entered in order from least significant to
# most significant. Since valid digits are 0 to 8, hence any other input will be used as
# sentinel value
def problem_67():
    base9_num = []
    while True:
        digit = input("Enter a digit (0-8) of the base-9 number (Enter any other value to stop): ")
        if not digit.isdigit() or int(digit) > 8:
            break
        base9_num.append(int(digit))

    if not base9_num:
        print("No valid digits entered. Conversion not possible.")
    else:
        decimal_value = 0
        for digit in base9_num:
            decimal_value = decimal_value * 9 + digit

        binary_value = bin(decimal_value)[2:]

        print("Binary value: " + binary_value)


# problem 68: Conversion of microseconds to weeks, days, hours, minutes, seconds, and remaining microseconds
def problem_68():
    n = int(input("Enter the number:"))
    day = n // (24 * 3600)
    n = n % (24 * 3600)
    hour = n // 3600
    n %= 3600
    minutes = n // 60
    n %= 60
    seconds = n
    print(day, "days", hour, "hours",minutes, "minutes",seconds, "seconds")


# problem 69:  Three numbers denoted by the variables A, B and C are supplied as input data. Print
# these three number in ascending order.
def problem_69():
    A = float(input("Enter the first number (A): "))
    B = float(input("Enter the second number (B): "))
    C = float(input("Enter the third number (C): "))
    minimum = min(A, B, C)
    maximum = max(A, B, C)
    middle = A + B + C - minimum - maximum
    print("Numbers in ascending order:")
    print(minimum)
    print(middle)
    print(maximum)

# problem 70: Write an if-else statement that outputs the word “Warning” provided that either the
# value of the variable temperature is greater than or equal to 100, or the value of the
# variable pressure is greater than or equal to 200, or both. Otherwise, the if-else
# statement outputs the work “OK”
def problem_70():
    temperature = float(input("Enter the temperature: "))
    pressure = float(input("Enter the pressure: "))
    if temperature >= 100 or pressure >= 200:
        print("Warning")
    else:
        print("OK")

# problem 70:Input two positive integers and a and b from the user. Determine the integer of a/b.
# Assume that the division operator is not available:
def problem_71():
    #fixme what if b > a ??
    a = int(input("Enter a positive integer a: "))
    b = int(input("Enter a positive integer b: "))
    quotient = 0

    while a >= b:
        a -= b
        quotient += 1
    print("Integer division a/b:", quotient)

#problem 72: Input two positive integers a and b from the user. Determine the remainder of a/b.
# Assume that the division and modulus operators are not available
def problem_72():
    a = int(input("Enter a positive integer a: "))
    b = int(input("Enter a positive integer b: "))
    if b == 0:
        print("Error: Division by zero")
    else:
        remainder = a
        while remainder >= b:
            remainder -= b
        print("Remainder of a/b:", remainder)

# Input a decimal integer and display its hexadecimal equivalent digit-by-digit. The
# hexadecimal output should be in order from least significant to most significant
def problem_73():
    decimal = int(input("Enter a decimal integer: "))
    hexadecimal = ""

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = str(remainder) + hexadecimal
        decimal = decimal // 16

    print("Hexadecimal equivalent: 0x" + hexadecimal)







# # unit_list [{"unit":1, "cost":10, "margin":10, "price":10}
# # {"unit":2, "cost":5, "margin":5, "price":10}
# # {"unit":3, "cost":6, "margin":2, "price":8}
# # {"unit":4, "cost":7, "margin":3, "price":10}]
# def problem_73():
#     unit_list = [
#         {"unit": 1, "cost": 10, "margin": 10, "price": 10},
#         # {"unit": 2, "cost": 5, "margin": 5, "price": 10},
#         # {"unit": 3, "cost": 6, "margin": 2, "price": 8},
#         {"unit": 4, "cost": 7, "margin": 3, "price": 10}
#     ]
#     num_units = len(unit_list)
#     expected_units = set(range(1, num_units + 1))
#     for unit in unit_list:
#         expected_units.discard(unit['unit'])
#     if expected_units:
#         missing_units = ', '.join(str(unit) for unit in expected_units)
#         print(f"Error: Missing unit(s) {missing_units}")
#     else:
#         print("All units are present")
#
# #
#
# def problem_74():
#     unit_list = [
#         {"unit": 1, "cost": 10, "margin": 10, "price": 10},
#         {"unit": 2, "cost": 5, "margin": 5, "price": 10},
#         # {"unit": 3, "cost": 6, "margin": 2, "price": 8},
#         {"unit": 4, "cost": 7, "margin": 3, "price": 10}
#     ]
#
#     is_continuous = all(unit_list[i]["unit"] + 1 == unit_list[i+1]["unit"] for i in range(len(unit_list)-1))
#
#     if is_continuous:
#         print("OK")
#     else:
#         print("Error")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # problem_1()
    # problem_2()
    # problem_3()
    # problem_4()
    # problem_5()
    # problem_6()
    problem_7()
    problem_8()
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
    # problem_28()
    # problem_30()
    # problem_31()
    # problem_32()
    # problem_33()
    # problem_34()
    # problem_35()
    # problem_36()
    # problem_37()
    # problem_38()
    # problem_39()
    # problem_40()
    # problem_41()
    # problem_42()
    # problem_43()
    # problem_44()
    # problem_45()
    # problem_46()
    # problem_47()
    # problem_48()
    # problem_49()
    # problem_50()
    # problem_51()
    # problem_52()
    # problem_53()
    # problem_54()
    # problem_55()
    # problem_56()
    # problem_57()
    # problem_58()
    # problem_59()
    # problem_60()
    # problem_61()
    # problem_62()
    # problem_63()
    # problem_64()
    #  problem_65()
    # problem_66()
    # problem_67()
    # problem_68()
    # problem_69()
    # problem_70()
    # problem_71()
    # problem_72()
    # problem_73()
    # problem_74()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/





