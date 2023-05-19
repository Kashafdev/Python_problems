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
# def problem_19():
#     # time1= float(input("Enter the time1"))
#     # time2 = float(input("Enter the time2"))
#     # hours, minutes = calculate_time_difference(time1, time2)
#     # print("hours, mintues")

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
def problem_24():
    num = 1
    n = int(input("Enter the number"))
    for num in range(1, n):
        if num >= 1:
            print(num)

# Calculate the factorial of a positive integer entered by the user
def problem_25():
    num = int(input("Enter a positive integer: "))
    factorial = 1
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("The factorial of", num, "is", factorial)

# Take two positive integers a and n from the user. Calculate and display an. Assume
# that the power operator is not available.
def problem_26():
    a = int(input("Enter a positive integer (a): "))
    n = int(input("Enter a positive integer (n): "))

    result = 1
    for i in range(n):
        result *= a

    print(result)

# Take three number from the user and determine the largest number. Do it using a
# loop
def problem_27():
    largest = None

    for i in range(3):
        num = int(input("Enter the number: "))
        if largest is None or num > largest:
            largest = num
    print(largest)



# Take n number from the user and determine the largest number entered by the user,
# where n is taken from the user as well.
def problem_28():
    n = int(input("Enter the number n: "))
    largest = None

    for i in range(n):
        num = int(input("Enter the number: "))
        if largest is None or num > largest:
            largest = num
    print(largest)

#  Take n numbers from the user and determine both the smallest and the largest
# number entered by the user, where n is taken from the user as well.
def problem_29():
    n = int(input("Enter the number n: "))
    largest = None
    smallest = None

    for i in range(n):
        num = int(input("Enter the number: "))
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    print(largest)
    print(smallest)

# Take n numbers from the user and determine that how many positive and negative
# integers were entered by the user
def problem_30():
    n = int(input("Enter the number n: "))
    positive_count = 0
    negative_count = 0

    for i in range(n):
        num = int(input("Enter the number: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print(positive_count)
    print(negative_count)

#  Take a positive integer n from the user. Display all the divisors of n
def problem_31():
    n = int(input("Enter the number"))
    for i in range(1, n+1):
         if n % i == 0:
             print(i)

#Input a positive integer from the user and determine where the number is a perfect.......number itself.)
def problem_32():
    n = int(input("Enter a positive number: "))

    divisor_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")

# Input a positive integer from the user and determine whether is a prime number or not.
# def problem_33():
#     n = int(input("Enter the positive integer:"))


#Take a positive integer from the user. Displaying an error message and prompting for input again and again if the user enters invalid input (negative or zero)
def problem_34():
    while True:
        num = int(input("Enter the number: "))
        if num <= 0:
            print("Input invalid ,Please enter a positive number")
        else:
            break
    print(num)


# Write an algorithm to determine the sum of a variable number of positive integers taken from the user. The algorithm should keep prompting the user for more input until the user enters the sentinel value -999
def problem_35():
    total = 0
    while True:
        num = int(input("Enter the number:"))
        if num == -999:
            break
        elif num > 0:
            total += num
    print(total)


def problem_36():
    num = int(input("Enter the number"))
    negative_num = -num
    print(negative_num)

# Find absolute of an input. Assume that the absolute operator is not available.
def problem_37():
    num = int(input("Enter the number:"))
    absolute_value = num if num >= 0 else -num
    print(absolute_value)

# Input 2 number and find if both are even, both are odd, or 1 even 1 odd.
def problem_38():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number"))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("Both are Even")
    elif num1 % 2 != 0:
        print("Both are odd")
    else:
        print("1even 1 odd")

# Input 3 numbers and find how many are odd.
def problem_39():
    num1 = int(input("Enter the First number"))
    num2 = int(input("Enter the Second number"))
    num3 = int(input("Enter the Third number"))
    odd = 0
    if num1 % 2 != 0:
        odd += 1
    if num2 % 2 != 0:
        odd += 1
    if num3 % 2 != 0:
        odd +=1
    print(odd)

#  Input 3 numbers and print the 2 largest numbers.
def problem_40():
    num1 = int(input("Enter the First number:"))
    num2 = int(input("Enter the Second number:"))
    num3 = int(input("Enter the Third number:"))
    largest = 0

    if num1 > num2 and num1 > num3:
        largest = num1
    if num2 > num1 and num2 > num3:
        largest = num2
    if num3 > num1 and num3 > num2:
        largest = num3
    print(largest)

# Input a number and find if it is 2-digit positive integer or not.
def problem_41():
    num = int(input("Enter the number:"))
    if num >= 10 and num <= 99:
        print("The number is 2-digit positive number")
    else:
        print("The number is not a 2-digit positive number")

#  Input a 2-digit number and find the absolute difference between its digits
def problem_42():
    num = int(input("Enter the number:"))
    tens_digit = num // 10
    ones_digit = num % 10
    difference = abs(tens_digit - ones_digit)
    print(difference)

#  Input an integer (up to 4 digits) and store its reverse in another variable. Then display both integers.
def problem_43():
    num = int(input("Enter the number:"))
    reverse_num = int(str(num)[::-1])
    print(num)
    print(reverse_num)

#  Interchange two numbers
def problem_44():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    temp = num1
    num1 = num2
    num2 = temp
    print(num1)
    print(num2)

# Interchange two numbers without using an extra variable
def problem_45():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num1, num2 = num2, num1
    print(num1)
    print(num2)

# Conversion of microseconds to weeks, days, hours, minutes, seconds, and remaining microseconds
def problem_46():
    n = int(input("Enter the number:"))
    day = n // (24 * 3600)
    n = n % (24 * 3600)
    hour = n // 3600
    n %= 3600
    minutes = n // 60
    n %= 60
    seconds = n
    print(day, "days", hour, "hours",
          minutes, "minutes",
          seconds, "seconds")

# Multiply a number with the sum of its digits.
def problem_47():
    num = int(input("Enter the number:"))
    product = 1

    while (num != 0):
        product = product * (num % 10)
        num = num // 10

    print(product)

# Input 2 numbers and print YES if 1st is divisible by 2nd
def problem_48():
    num1 = int(input("Enter the First number:"))
    num2 = int(input("Enter the Second number:"))
    if num1 % num2 ==0:
        print("YES")
    else:
        print("NO")

# Input 2 numbers and print YES if 2nd is divisible by 1st
def problem_49():
    num1 = int(input("Enter the First number:"))
    num2 = int(input("Enter the Second number:"))
    if num2 % num1 == 0:
       print("YES")
    else:
       print("NO")

#  Input 2 numbers and print YES if one number is divisible by the other.
def problem_50():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    if num1 % num2 == 0 and num2 % num1 == 0:
        print("YES")
    else:
        print("NO")

# Input numbers till user inputs a zero and display their sum.
def problem_51():
    sum = 0
    num = None
    while num != 0:
        num = int(input("Enter the number:"))
        sum += num
    print(sum)

# Input numbers till user inputs a zero and at the end display last non-zero number
def problem_52():
    last_non_zero = None
    num = None

    while num != 0:
        num = int(input("Enter a number: "))
        if num != 0:
            last_non_zero = num

    print(last_non_zero)

# Input numbers till user inputs a zero and display the largest number
def problem_53():
    largest_num = None
    num = None

    while num != 0:
        num = int(input("Enter a number: "))
        if num != 0:
            if largest_num is None or num > largest_num:
                largest_num = num

    print(largest_num)

# Input numbers till user inputs a zero, and display the smallest number
# ⦁ Check if it works for all positive inputs
# ⦁ Now check algorithm # 55 (largest number) if it works for all negative inputs
# ⦁ If you find any problem, then solve it.
def problem_54():
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

# Input 10 numbers, and display the smallest number
def problem_55():
    smallest_num = float()

    for i in range(10):
        num = int(input("Enter a number: "))
    if num < smallest_num:
        smallest_num = min(num)

    print(smallest_num)

#  nput 10 numbers, and display count of even and odd numbers, separately, at the end
def problem_56():
    num = int(input("Enter the number:"))
    even_count = 0
    odd_count = 0

    for i in range(10):
        num = int(input("Enter the number: "))
        if num % 2 == 0:
            even_count += 1
        elif num % 2 != 0:
            odd_count += 1
    print(even_count)
    print(odd_count)

# Input SLimit and Elimit from the user, and display even numbers between range, with both limit, included.
def problem_57():
    SLimit = int(input("Enter the starting limit: "))
    ELimit = int(input("Enter the ending limit: "))

    if SLimit % 2 != 0:
        SLimit += 1

    if ELimit % 2 != 0:
        ELimit -= 1

    if SLimit <= ELimit:
        print(SLimit, "and", ELimit,)
        for num in range(SLimit, ELimit + 1, 2):
            print(num)
    else:
        print(SLimit, "and", ELimit)

# Input SLimit and ELimit from the user and display only those numbers between range which are divisible by 2 or 3 or 5, with both limits included .
def problem_58():
    SLimit = int(input("Enter the Starting Limit:"))
    ELimit = int(input("Enter the Ending limit:"))

    print(SLimit, ELimit)
    for num in range(SLimit, ELimit, 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            print(num)

#   Input 2 numbers and find their GCD
def problem_59():
    import math
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = math.gcd(num1, num2)
    print(result)

# Input 3 numbers and find their GCD
def problem_60():
    import math
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the third number:"))
    result = math.gcd(num1, num2, num3)
    print(result)

# Input 2 numbers and display their LCM.
def problem_61():
    import math
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = math.lcm(num1, num2)
    print(result)

# Input a number and display that how many digits it has.
def problem_62():
    num = int(input("Enter the number:"))
    digit_count = len(str(num))
    print(digit_count)

# Input a base-9 number, digit by digit, then convert it into decimal number. Digits of the input will be entered in order from least significant to most significant. Since valid digits are 0 to 8, hence any other input will be used as the sentinel value.
def problem_63():
    base9_num = 0
    power = 0

    while True:
        digit = int(input("Enter the number: "))

        if digit < 0 or digit > 8:
            break

        base9_num += digit * (9 ** power)
        power += 1

    print(base9_num)

# Input a base-9 number, digit by digit, then convert it into decimal number. Digits of the input will be entered in order from most significant to least significant. Since valid digits are 0 to 8, hence any other input will be used as sentinel value.
def problem_64():
    base9_num = 0
    power = 0

    while True:
        digit = int(input("Enter the number: "))

        if digit < 0 or digit > 8:
            break

        base9_num += digit * (9 ** power)
        power += 1

    print(base9_num)


# practice problem
def problem_prac1():
    unit_list = [
        {"unit": 1, "cost": 10, "margin": 10, "price": 10},
        {"unit": 2, "cost": 5, "margin": 5, "price": 10},
        {"unit": 3, "cost": 6, "margin": 2, "price": 8},
        {"unit": 4, "cost": 7, "margin": 3, "price": 10}
    ]

    expected_units = set(range(1, len(unit_list) + 1))
    actual_units = set(unit['unit'] for unit in unit_list)

    missing_units = expected_units - actual_units

    if missing_units:
        print(f"Error: Missing units {missing_units}")
    else:
        print("All units are present")

def problem_prac2():
    unit_list = [
        {"unit": 1, "cost": 10, "margin": 10, "price": 10},
        {"unit": 2, "cost": 5, "margin": 5, "price": 10},
        {"unit": 3, "cost": 6, "margin": 2, "price": 8},
        {"unit": 4, "cost": 7, "margin": 3, "price": 10}
    ]

    sorted_units = sorted(unit['unit'] for unit in unit_list)


    if sorted_units == list(range(sorted_units[0], sorted_units[-1] + 1)):
        print("OK")
    else:
        print("Error")



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
    # problem_63()
    # problem_64()
    # problem_prac1()
    problem_prac2()
















