# PRACTICE PRACTICE PRACTICE
def problem_1():
    # QUOTIENT OF DIVISION OF TWO NUMBERS
    numerator = 10
    denominator = 3
    quotient = numerator // denominator
    print(quotient)


def problem_2():
    # INPUT FOUR NUMBERS AND GENERATE SUM
    num1 = 10
    num2 = 15
    num3 = 20
    num4 = 25
    total = num1 + num2 + num3 + num4
    print("The sum is:", total)


def problem_3():
    # SUM AND AVG OF MARKS OF 5 STUDENTS
    # Initialize a list to store the marks of the five students
    marks = []

    # Prompt the user to input the marks of the five students
    for i in range(5):
        mark = int(input("Enter the mark of student {}: ".format(i + 1)))
        marks.append(mark)

    # Calculate the sum of the marks using the built-in sum() function
    total_marks = sum(marks)

    # Calculate the average of the marks
    average_marks = total_marks / len(marks)

    # Print the sum and average of the marks
    print("The sum of the marks is:", total_marks)
    print("The average of the marks is:", average_marks)


def problem_4():
    # %AGE OF TOTAL MARKS OF FOUR STUDENTS
    marks1 = 90
    marks2 = 95
    marks3 = 85
    marks4 = 80
    sum = marks1 + marks2 + marks3 + marks4
    possible_total_marks = 500
    total_marks = sum / possible_total_marks * 100
    print("The percentage of total marks:", total_marks)


def problem_5():
    # Check if a number is greater than 80, say “good”, if not say, “Try again”
    number = float(input("Enter a number: "))
    if number > 80:
        print("good:")
    else:
        print("try again:")


def problem_6():
    # Check whether a number is divisible by another user-given number or no
    number = int(input("Enter a number:"))
    divisor = int(input("Enter a divisor number:"))
    if number % divisor:
        print("Number is divisible by the divisor:")
    else:
        print("Number is divisible by the divisor:")


def problem_7():
    # Sum of odd numbers from 10 user-given numbers
    #todo create a loop and take 10 inputs from user
    user1 = 3
    user2 = 5
    user3 = 7
    user4 = 9
    user5 = 11
    user6 = 13
    user7 = 15
    user8 = 17
    user9 = 19
    user10 = 21
    sum = user1 + user2 + user3 + user4 + user5 + user6 + user7 + user8 + user9 + user10
    print("The sum of odd numbers:", sum)


def problem_75():
    #  Sum of odd numbers from 10 user-given numbers (USING LOOPS)
    # Initialize the sum variable
    sum_of_odds = 0

    # Iterate 10 times
    for _ in range(10):
        number = int(input("Enter a number: "))
        if number % 2 != 0:
            sum_of_odds += number
    print("Sum of odd numbers:", sum_of_odds)


def problem_8():
    # Sum of even number from n user-given numbers. Where n is also user-input
    n = int(input("Enter the value of n: "))  # prompt user to input n

    sum_of_evens = 0  # initialize sum of even numbers to 0

    for i in range(n):
        num = int(input("Enter a number: "))  # prompt user to input a number
        if num % 2 == 0:  # check if the number is even
            sum_of_evens += num  # add the number to the sum of even numbers

    print("The sum of even numbers is:", sum_of_evens)  # print the sum of even numbers


def problem_9():
    #    Show first n terms of Fibonacci series
    n = int(input("Enter the number of terms to display: "))

    # Initializing the first two terms of the series
    a, b = 0, 1

    # Displaying the first 'n' terms of the series
    print("The first {} terms of the Fibonacci series are:".format(n))
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def problem_10():
    # Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the formula: C = (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * (5 / 9)

    print("The temperature in Celsius is:", celsius)


def problem_11():
    # Calculating pay for an employee, given the hours worked and rate per hour.
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_per_hour = float(input("Enter the rate per hour: "))

    # Calculate the pay by multiplying the hours worked with the rate per hour
    pay = hours_worked * rate_per_hour

    print("The employee's pay is:", pay)


def problem_12():
    # Determine the status of a student (pass or fail) given his/her marks in a subject  (passing marks = 50)
    passing_marks = 50
    marks = float(input("Enter the marks: "))

    # Determine the status (pass or fail) based on the marks
    if marks >= passing_marks:
        status = "Pass"
    else:
        status = "Fail"

    print("The student's status is:", status)


def problem_13():
    #  Calculate pay of an employee based on the hours worked. The input includes the
    # employee total hours worked this week and their hourly pay rate. The employee is
    # to be paid their basic wage for the first 40 hours and time-and-a-half (i.e. 50%
    # more) for all hours above 40 (overtime pay). Output the regular pay. Overtime pay
    # and total pay for the week on the screen. If the employee worked 40 hours or less,
    # don’t output any information about overtime pay
    hours_worked = float(input("Enter the number of hours worked this week: "))
    hourly_rate = float(input("Enter the hourly pay rate: "))

    regular_hours = min(hours_worked, 40)  # Calculate regular hours (up to 40 hours)
    overtime_hours = max(hours_worked - 40, 0)  # Calculate overtime hours (hours above 40)

    regular_pay = regular_hours * hourly_rate  # Calculate regular pay
    overtime_pay = overtime_hours * hourly_rate * 1.5  # Calculate overtime pay (time-and-a-half)
    total_pay = regular_pay + overtime_pay  # Calculate total pay

    print("Regular Pay:", regular_pay)
    if overtime_hours > 0:
        print("Overtime Pay:", overtime_pay)
    print("Total Pay:", total_pay)


def problem_14():
    # Take two number from the user and determine the largest number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Determine the largest number
    if num1 > num2:
        largest = num1
    else:
        largest = num2

    print("The largest number is:", largest)


def problem_15():
    # Take three number from the user and determine the largest number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number:"))
    # Determine the largest number
    largest = max(num1, num2, num3)

    print("The largest number is:", largest)


def problem_16():
    # Take three number from the user and determine the largest number with values
    # (using nested if-else)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Determine the largest number
    if num1 >= num2:
        if num1 >= num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3

    print("The largest number is:", largest)


def problem_17():
    # Take three number from the user and determine the largest number with values
    # (using compound conditions)

    # Taking input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    # Using compound conditions to determine the largest number
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # Printing the largest number
    print("The largest number is:", largest)


def problem_18():
    # Take three number from the user and determine the largest number with values
    # (Comparing numbers one by one)
    # Taking input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    # Assuming the first number is the largest
    largest = num1

    # Comparing the largest with the other numbers
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3

    # Printing the largest number
    print("The largest number is:", largest)


def problem_19():
    # Determine the grade of a student from the marks obtained (90-100, A; 80-29, B;
    # 70-79, C; 60-69, D; <60, F)

    marks = int(input("Enter the marks obtained: "))
    if marks >= 90 and marks <= 100:
        grade = "A"
    elif marks >= 80 and marks < 90:
        grade = "B"
    elif marks >= 70 and marks < 80:
        grade = "C"
    elif marks >= 60 and marks < 70:
        grade = "D"
    # Marks are below 60
    else:
        grade = "F"
    print("The grade is:", grade)


def problem_20():
    # Input a number and determine whether the number is even or odd.

    number = int(input("Enter the number:"))
    if number % 2 == 0:
      print("The number is Even")
    else:
       print("The number is Odd")


def problem_21():
    # Input 3 numbers. Determine whether: all are same, all are different or exactly two
    # are same.
    def compare_numbers(a, b, c):
        if a == b == c:
            return f"All numbers ({a}, {b}, {c}) are the same."
        elif a != b and a != c and b != c:
            return f"All numbers ({a}, {b}, {c}) are different."
        else:
            return f"Exactly two numbers are the same ({a}, {b}, {c})."

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    result = compare_numbers(num1, num2, num3)
    print(result)


def problem_22():
    # Finding the sum of 10 numbers taken from the user
    numbers = []  # Create an empty list to store the numbers

    # Use a for loop to iterate 10 times
    sum =0
    for i in range(10):
        # Prompt the user to enter a number and convert it to float
        num = float(input(f"Enter number {i + 1}: "))
        sum = sum + num
        # Add the number to the 'numbers' list
        # numbers.append(num)

    # Calculate the sum of the numbers using the sum() function
    # sum_of_numbers = sum(numbers)

    # Print the sum of the numbers
    print("The sum of the numbers is:", sum)


def problem_23():
    # Finding the sum of n numbers taken from the user. Where n is taken from the user
    # as well.
    #todo  do it without list comprihenshion
    n = int(input("Enter the value of n: "))
    numbers = []
    for i in range(n):
        num = float(input(f"Enter  number {i + 1}: "))
        numbers.append(num)
    sum_of_numbers = sum(numbers)
    print("The sum of the numbers is:", sum_of_numbers)

def problem_76():
    #      Finding the sum of n numbers taken from the user. Where n is taken from the user
    #     as well. ( WITHOUT LIST COMPREHENSION)

    # Ask the user for the value of n
    n = int(input("Enter the value of n: "))

    # Initialize the sum variable
    sum_of_numbers = 0

    # Iterate 'n' times
    for _ in range(n):
        # Ask the user for a number
        number = int(input("Enter a number: "))

        # Add the number to the sum
        sum_of_numbers += number

    # Print the sum of numbers
    print("Sum of numbers:", sum_of_numbers)


def problem_24():
    # Finding the average of n number from the user, where n is user-given value.
    n = int(input("Enter the value of n:"))
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number{i + 1}:"))
        numbers.append(num)
        sum_of_numbers = sum(numbers)
        average = sum_of_numbers / n
        print("The average of the numbers is:", average)


def problem_25():
    # Displaying positive integers in the range from 1 to n, where n is taken from the user.
    n = int(input("Enter a positive integer: "))
    #fixme do it using loop thia logic is wrong
    if n < 1:
        print("Please enter a positive integer.")
    else:
        print("Number\tValue")
        for i in range(1, n + 1):
            print(i, "\t", i * i)

def problem_77():
    # Displaying positive integers in the range from 1 to n, where n is taken from the user.
    # (USING LOOPS)
    # Ask the user for the value of n
    n = int(input("Enter the value of n: "))

    # Iterate from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Display the positive integer
        print(i)


def problem_26():
    #     Calculate the factorial of a positive integer entered by the user
    def factorial(n):
        if n == 0:
            return 1
        else:
            fact = 1
            print("Number\tFactorial")
            for i in range(1, n + 1):
                fact *= i
                print(i, "\t", fact)
            return fact


    n = int(input("Enter a positive integer: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(n)
        print("Factorial of", n, "is", result)


def problem_27():
    # Take two positive integers a and n from the user. Calculate and display an. Assume
    # that the power operator is not available.
    def calculate_power(a, n):
        result = 1
        explanation = str(a) + "^0 = 1"
        for i in range(1, n + 1):
            result *= a
            explanation += "\n" + str(a) + "^" + str(i) + " = " + str(result)
        return result, explanation


    a = int(input("Enter a positive integer for the base (a): "))
    n = int(input("Enter a positive integer for the exponent (n): "))

    if a < 0 or n < 0:
        print("Both numbers should be positive integers.")
    else:
        power, explanation = calculate_power(a, n)
        print("\nExplanations:")
        print(explanation)
        print("\nResult:")
        print(a, "^", n, "is", power)


def problem_28():
    # Take three number from the user and determine the largest number. Do it using a
    # loop

    numbers = []

    # Input three numbers
    for i in range(3):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Find the largest number
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    # Display the largest number
    print("The largest number is:", largest)


def problem_29():
    n = int(input("Enter the total number of values: "))

    # Initialize largest to the smallest possible value
    largest = float('-inf')

    # Input 'n' numbers
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        if num > largest:
            largest = num

    # Display the largest number
    print("The largest number is:", largest)


def problem_30():
    # Take n numbers from the user and determine both the smallest and the largest
    # number entered by the user, where n is taken from the user as well.

    n = int(input("Enter the total number of values: "))

    # Initialize smallest to the largest possible value and largest to the smallest possible value
    smallest = float('inf')
    largest = float('-inf')

    # Input 'n' numbers
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Display the smallest and largest numbers
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)


def problem_31():
    # Take n numbers from the user and determine that how many positive and negative
    # integers were entered by the user.

    n = int(input("Enter the number of integers: "))
    positive_count = 0
    negative_count = 0

    for i in range(n):
        num = int(input("Enter an integer: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print("Positive integers entered:", positive_count)
    print("Negative integers entered:", negative_count)


def problem_32():
    #  Take a positive integer n from the user. Display all the divisors of n.
    n = int(input("Enter a positive integer: "))

    print("Divisors of", n, ":")

    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            # divisors.append(i)
            print(n)

    # for divisor in divisors:
    #     print(divisor)


def problem_33():
    # Input a positive integer from the user and determine where the number is a perfect
    # number or not. (a perfect number is a positive integer that is equal to the sum of its
    # proper positive divisors, that is, the sum of its positive divisors excluding the number
    # itself.

    n = int(input("Enter a positive integer: "))

    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")

def problem_34():
    # Input a positive integer from the user and determine whether is a prime number or
    # not.
    n = int(input("Enter a positive integer: "))

    if n <= 1:
        print(n, "is not a prime number.")
    else:
        is_prime = True
        # for i in range(2, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print(n, "is a prime number.")
        else:
            print(n, "is not a prime number.")


def problem_35():
    # Take a positive integer from the user. Displaying an error message and prompting
    # for input again and again if the user enters invalid input (negative or zero)
    while True:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            print("You entered:", n)
        else:
            print("Invalid input. Please enter a positive integer.")

    # Continue with the rest of your code using the valid 'n'



def problem_36():
    # Write an algorithm to determine the sum of a variable number of positive integers
    sum = 0
    num = int(input("Enter a positive integer or -999 to stop: "))

    while num != -999:
        sum += num
        num = int(input("Enter a positive integer or -999 to stop: "))

    print("The sum is:", sum)


def problem_37():
    # Display negative of a number
    number = float(input("Enter a number: "))
    negative = -1 * number

    print("The negative of", number, "is", negative)


def problem_38():
    #   Find absolute of an input. Assume that the absolute operator is not available.
    number = float(input("Enter a number: "))

    if number < 0:
        number = -1 * number

    print("The absolute value is:", number)


def problem_39():
    # Input 2 number and find if both are even, both are odd, or 1 even 1 odd.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 % 2 == 0 and number2 % 2 == 0:
        print("Both numbers are even.")
    elif number1 % 2 != 0 and number2 % 2 != 0:
        print("Both numbers are odd.")
    else:
        print("One number is even and the other is odd.")

def problem_40():
    #  Input 3 numbers and find how many are odd.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    count = 0

    if number1 % 2 != 0:
        count += 1

    if number2 % 2 != 0:
        count += 1

    if number3 % 2 != 0:
        count += 1

    print("Number of odd numbers:", count)

def problem_41():
    #todo do it without using max()
    # Input 3 numbers and print the 2 largest numbers
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    largest = max(number1, number2, number3)

    if number1 == largest:
        second_largest = max(number2, number3)
    elif number2 == largest:
        second_largest = max(number1, number3)
    else:
        second_largest = max(number1, number2)

    print("Largest numbers:", largest, second_largest)


def problem_42():
    # Input a number and find if it is 2-digit positive integer or no
    #fixme if user enter -99  hint: use len()
    number = int(input("Enter a number: "))

    if number >= 10 and number < 100:
        print(number, "is a two-digit positive integer.")
    else:
        print(number, "is not a two-digit positive integer.")

def problem_43():
    # Input a 2-digit number and find the absolute difference between its digits
    number = int(input("Enter a two-digit number: "))

    tens_digit = number // 10
    ones_digit = number % 10

    absolute_difference = abs(tens_digit - ones_digit)

    print("The absolute difference between the digits is:", absolute_difference)


def problem_44():
    # Input an integer (up to 4 digits) and store its reverse in another variable. Then
    # display both integers.
    number = int(input("Enter an integer (up to 4 digits): "))
    original_number = number
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number = number // 10

    print("Original number:", original_number)
    print("Reversed number:", reversed_number)


def problem_45():
    # Interchange two number
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    temp = number1
    number1 = number2
    number2 = temp

    print("After interchange:")
    print("First number:", number1)
    print("Second number:", number2)


def problem_46():
    # Interchange two numbers without using an extra variable.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2

    print("After interchange:")
    print("First number:", number1)
    print("Second number:", number2)


def problem_47():
    #  Conversion of microseconds to weeks, days, hours, minutes, seconds, and
    # remaining microseconds.
    microseconds = int(input("Enter the duration in microseconds: "))

    seconds = microseconds // 1000000
    weeks = seconds // 604800
    seconds %= 604800
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    print("Duration:")
    print("Weeks:", weeks)
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print("Remaining Microseconds:", microseconds % 1000000)


def problem_48():
    # Multiply a number with the sum of its digits.
    number = int(input("Enter a number: "))

    sum_of_digits = 0
    temp_number = number

    while temp_number > 0:
        last_digit = temp_number % 10
        sum_of_digits += last_digit
        temp_number = temp_number // 10

    product = number * sum_of_digits

    print("Product:", product)

def problem_49():
    #fixme what if number2 = 0 ?
    # Input 2 numbers and print YES if 1st is divisible by 2nd.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 % number2 == 0:
        print("YES")
    else:
        print("NO")


def problem_50():
    # Input 2 numbers and print YES if 2nd is divisible by 1st.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number2 % number1 == 0:
        print("YES")
    else:
        print("NO")


def problem_51():
    #  Input 2 numbers and print YES if one number is divisible by the other.
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    if number1 % number2 == 0 or number2 % number1 == 0:
        print("YES")
    else:
        print("NO")


def problem_52():
    # Input numbers till user inputs a zero and display their sum.
    sum = 0

    while True:
        number = int(input("Enter a number (or 0 to exit): "))

        if number == 0:
            break

        sum += number

    print("Sum of the numbers:", sum)


def problem_53():
    #  Input numbers till user inputs a zero and at the end display last non-zero number.
    last_non_zero = 0

    while True:
        number = int(input("Enter a number (or 0 to exit): "))

        if number == 0:
            break

        last_non_zero = number

    print("Last non-zero number:", last_non_zero)


def problem_54():
    # Input numbers till user inputs a zero and display the largest number.
    largest = float('-inf')

    while True:
        number = int(input("Enter a number (or 0 to exit): "))

        if number == 0:
            break

        if number > largest:
            largest = number

    print("Largest number:", largest)


def problem_55():
    # Input numbers till user inputs a zero, and display the smallest number.
    #  Check if it works for all positive inputs
    #  Now check algorithm # 55 (largest number) if it works for all negative inputs
    #  If you find any problem, then solve it.
    #todo -float('inf') explain ?
    largest = -float('inf')

    while True:
        number = int(input("Enter a number (or 0 to exit): "))

        if number == 0:
            break

        if number > largest:
            largest = number

    print("Largest number:", largest)


def problem_56():
    # Input 10 numbers, and display the smallest number.
    smallest = float('inf')

    for _ in range(10):
        number = int(input("Enter a number: "))

        if number < smallest:
            smallest = number

    print("Smallest number:", smallest)


def problem_57():
    #  Input 10 numbers, and display count of even and odd numbers, separately, at the end.
    even_count = 0
    odd_count = 0

    for _ in range(10):
        number = int(input("Enter a number: "))

        if number % 2 == 0:
            even_count += 1
        elif number % 2 != 0:
            odd_count += 1

    print("Count of even numbers:", even_count)
    print("Count of odd numbers:", odd_count)


def problem_58():
    # Input SLimit and Elimit from the user, and display even numbers between range,
    # with both limit, included.
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))

    even_numbers = []

    for number in range(start_limit, end_limit + 1):
        if number % 2 == 0:
            even_numbers.append(number)

    print("Even numbers between", start_limit, "and", end_limit, "are:", even_numbers)


def problem_59():
    #  Give an efficient solution that does not check divisibility of each number in
    # the given range.
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))

    even_numbers = []

    if start_limit % 2 != 0:
        start_limit += 1

    for number in range(start_limit, end_limit + 1, 2):
        even_numbers.append(number)

    print("Even numbers between", start_limit, "and", end_limit, "are:", even_numbers)


def problem_60():
    # Input SLimit and ELimit from the user and display only those numbers between
    # range which are divisible by 2 or 3 or 5, with both limits included.
    start_limit = int(input("Enter the start limit: "))
    end_limit = int(input("Enter the end limit: "))

    divisible_numbers = []

    for number in range(start_limit, end_limit + 1):
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            divisible_numbers.append(number)

    print("Numbers divisible by 2, 3, or 5 between", start_limit, "and", end_limit, "are:", divisible_numbers)

def problem_61():
    # Input SLimit and ELimit from user and display only those numbers between range
    # which divisible by 2 and 3 and 5, with both limits included.

    SLimit = int(input("Enter the starting limit: "))
    ELimit = int(input("Enter the ending limit: "))

    # Ensure the starting limit is less than or equal to the ending limit
    if SLimit > ELimit:
        print("Invalid range. The starting limit should be less than or equal to the ending limit.")
    else:
        # Iterate through the range and check divisibility by 2, 3, and 5
        for num in range(SLimit, ELimit + 1):
            if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
                print(num)


def problem_62():
    #     Input 2 numbers and find their GCD
    #todo explain
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd = find_gcd(num1, num2)
    print("The GCD of", num1, "and", num2, "is", gcd)


def problem_63():
    # Input 3 numbers and find their GCD
    #todo explain
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def find_gcd_three_numbers(a, b, c):
        gcd_ab = find_gcd(a, b)
        gcd_abc = find_gcd(gcd_ab, c)
        return gcd_abc

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    gcd = find_gcd_three_numbers(num1, num2, num3)

    print("The GCD of", num1, ",", num2, ", and", num3, "is", gcd)


def problem_64():
    # Input 2 numbers and display their LCM.
    def find_lcm(a, b):
        # Find the maximum of the two numbers
        max_num = max(a, b)

        # Start with the larger number as the LCM
        lcm = max_num

        # Check if the current lcm is divisible by both numbers
        while True:
            if lcm % a == 0 and lcm % b == 0:
                break
            lcm += max_num

        return lcm
    # Input the two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate and display the LCM
    lcm = find_lcm(num1, num2)
    print("The LCM of", num1, "and", num2, "is", lcm)


def problem_65():
    # Input a number and display that how many digits it has.
    def count_digits(num):
        # Convert the number to a string and calculate the length
        num_str = str(num)
        num_digits = len(num_str)
        return num_digits
    num = int(input("Enter a number: "))
    # Calculate and display the number of digits
    num_digits = count_digits(num)
    print("The number", num, "has", num_digits, "digits.")

def problem_66():
    #   Input a base-9 number, digit by digit, then convert it into decimal number. Digits of
    # the input will be entered in order from most significant to least significant. Since
    # valid digits are 0 to 8, hence any other input will be used as sentinel value.
    def convert_to_decimal(base9):
        decimal = 0
        power = 0

        # Iterate through each digit in reverse order.
        for digit in reversed(base9):
            # Check if the digit is within the valid range
            if digit < 0 or digit > 8:
                break

            # Calculate the decimal value of the digit
            decimal += digit * (9 ** power)
            power += 1

        return decimal

    # Input the base-9 number digit by digit
    base9 = []
    while True:
        digit = int(input("Enter a digit (0 to 8) or any other value to stop: "))
        if digit < 0 or digit > 8:
            break
        base9.append(digit)

    # Convert the base-9 number to decimal
    decimal = convert_to_decimal(base9)
    print("The decimal equivalent of the base-9 number is:", decimal)


def problem_67():
    # Input a number and display its equivalent in base-9 (one digit per line, starting from
    # the least significant.
    def convert_to_base9(decimal):
        base9 = []

        # Convert the decimal number to base-9
        while decimal > 0:
            digit = decimal % 9
            base9.append(digit)
            decimal //= 9

        # Reverse the base-9 digits to get the correct order
        base9.reverse()

        return base9

    # Input the decimal number
    decimal = int(input("Enter a decimal number: "))

    # Convert the decimal number to base-9
    base9 = convert_to_base9(decimal)

    # Display the base-9 digits
    print("The base-9 equivalent of the decimal number is:")
    for digit in base9:
        print(digit)


def problem_68():
    # Input number and store its equivalent in base-9 as a single numeric value and
    # display it.
    def convert_to_base9(decimal):
        base9 = 0
        power = 0

        # Convert the decimal number to base-9
        while decimal > 0:
            digit = decimal % 9
            base9 += digit * (10 ** power)
            decimal //= 9
            power += 1

        return base9

    # Input the decimal number
    decimal = int(input("Enter a decimal number: "))

    # Convert the decimal number to base-9
    base9 = convert_to_base9(decimal)

    # Display the base-9 value
    print("The base-9 equivalent of the decimal number is:", base9)


def problem_69():
    # Input a base-9 number, digit by digit, then convert it into binary number a single
    # numeric value. Digits of the input will be entered in order from least significant to
    # most significant. Since valid digits are 0 to 8, hence any other input will be used as
    # sentinel value.
    def convert_to_binary(base9):
        binary = 0
        power = 0

        # Iterate through each digit in reverse order
        for digit in reversed(base9):
            # Check if the digit is within the valid range
            if digit < 0 or digit > 8:
                break

            # Convert the base-9 digit to binary and add it to the result
            binary += digit * (9 ** power)
            power += 1

        return bin(binary)[2:]  # Convert to binary string and remove the '0b' prefix

    # Input the base-9 number digit by digit
    base9 = []
    while True:
        digit = int(input("Enter a digit (0 to 8) or any other value to stop: "))
        if digit < 0 or digit > 8:
            break
        base9.append(digit)

    # Convert the base-9 number to binary
    binary = convert_to_binary(base9)

    # Display the binary value
    print("The binary equivalent of the base-9 number is:", binary)


def problem_70():
    #  Input a decimal integer and display its hexadecimal equivalent digit-by-digit. The
    # hexadecimal output should be in order from least significant to most significant.
    def convert_to_hex(decimal):
        hex_digits = "0123456789ABCDEF"
        hex_value = ""

        # Convert the decimal number to hexadecimal
        while decimal > 0:
            digit = decimal % 16
            hex_value = hex_digits[digit] + hex_value
            decimal //= 16

        return hex_value

    # Input the decimal integer
    decimal = int(input("Enter a decimal integer: "))

    # Convert the decimal number to hexadecimal
    hexadecimal = convert_to_hex(decimal)

    # Display the hexadecimal digits
    print("The hexadecimal equivalent of the decimal integer is:")
    for digit in hexadecimal:
        print(digit)


def problem_71():
    #  Three numbers denoted by the variables A, B and C are supplied as input data. Print
    # these three number in ascending order.
    # Input the three numbers
    A = float(input("Enter the first number (A): "))
    B = float(input("Enter the second number (B): "))
    C = float(input("Enter the third number (C): "))

    # Find the minimum, middle, and maximum values
    min_value = min(A, B, C)
    max_value = max(A, B, C)
    mid_value = (A + B + C) - min_value - max_value

    # Print the numbers in ascending order
    print("The numbers in ascending order are:")
    print(min_value)
    print(mid_value)
    print(max_value)


def problem_72():
    # Write an if-else statement that outputs the word “Warning” provided that either the
    # value of the variable temperature is greater than or equal to 100, or the value of the
    # variable pressure is greater than or equal to 200, or both. Otherwise, the if-else
    # statement outputs the work “OK”.
    # Example values for temperature and pressure
    temperature = 98
    pressure = 210

    # Check the conditions and output the result
    if temperature >= 100 or pressure >= 200:
        print("Warning")
    else:
        print("OK")


def problem_73():
    # Input two positive integers and a and b from the user. Determine the integer of a/b.
    # Assume that the division operator is not available.
    def integer_division(a, b):
        count = 0

        while a >= b:
            a -= b
            count += 1

        return count

    # Getting input from the user
    num1 = int(input("Enter the dividend (a): "))
    num2 = int(input("Enter the divisor (b): "))

    result = integer_division(num1, num2)
    print(f"The integer division of {num1}/{num2} is: {result}")


def problem_74():
    # Input two positive integers a and b from the user. Determine the remainder of a/b.
    # Assume that the division and modulus operators are not available.
    def integer_division(a, b):
        count = 0

        while a >= b:
            a -= b
            count += 1

        return count

    # Getting input from the user
    num1 = int(input("Enter the dividend (a): "))
    num2 = int(input("Enter the divisor (b): "))

    result = integer_division(num1, num2)
    print(f"The integer division of {num1}/{num2} is: {result}")




if __name__ == '__main__':

    # problem_1()
    # problem_2()
    # problem_3()
    # problem_4()
    problem_5()
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
    # problem_28()
    # problem_29()
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
    #  problem_63()
    # problem_64()
    # problem_65()
    # problem_66()
    # problem_67()
    # problem_68()
    # problem_69()
    # problem_70()
    # problem_71()
    # problem_72()
    # problem_73()
    # problem_74()
    # problem_75()
    # problem_76()
    problem_77()