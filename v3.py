#1 to check if the 3rd last character of a string is a vowel or not.
vowel="aeiou"
x="cat"
if(x[-3]in vowel):
    print("it is a vowel")
else:
    print("it is not a vowel")
#2 Check if the first and last number of any 5 digit number  
x=32165
print(x//10000)
print(x%10)
#4 Write a Python calculate percentage of a student through 5 subjects. Take marks as input from the user
m = float(input("Enter marks of math: "))
p = float(input("Enter marks of physics: "))
c = float(input("Enter marks of chemistry: "))
e = float(input("Enter marks of english: "))
t = float(input("Enter marks of tamil: "))
total = m+p+c+e+t
percentage = (total / 500) * 100
print("Percentage =", percentage, "%")
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")
#5  to convert a celsius value to fahrenheit. Take celsius value as input
c = float(input("Enter temperature: "))
f = (c * 9/5) + 32
print(f)
#6 WAP to calculate the surface area of a triangle. Take the length of sides as input.
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 0.5 * base * height
print('area')
#7 to print the day based on the number
n= int(input("Enter a number (1-7): "))
if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid input")
#8 To check whether a person is eligible to vote or not based on their age.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
#9 To calculate the count of elements in a string.
s = input("Enter a string: ")
c = 0
for i in s:
    c = c + 1
print(c)
#10 to check using the sides of a triangle to tell if it is equilateral triangle or not.
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a == b and b == c:
    print("It is an Equilateral Triangle")
else:
    print("It is NOT an Equilateral Triangle")
#11 to check if the 2nd last digit of numerical input from the user is divisible by 3 or not.
n = int(input("Enter a number: "))
second_last = (n // 10) % 10
if second_last % 3 == 0:
    print("2nd last digit is divisible by 3")
else:
    print("2nd last digit is NOT divisible by 3")
#12 Write a Python program that takes two numbers as input from the user and prints the larger of the two numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("Larger number is:", a)
elif b > a:
    print("Larger number is:", b)
else:
    print("Both numbers are equal")
    
