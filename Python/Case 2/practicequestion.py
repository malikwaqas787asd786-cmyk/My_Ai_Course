#Write a program to check whether a number is even or odd.
num=int(input("Enter a number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

#Write a program to check whether a number is divisible by 7 or not.
num=int(input("Enter a number:"))
if num%7==0:
    print("Divisible by 7")
else:
    print("Not Divisible by 7")

#Write a program to find the largest of three numbers.
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))    
num3=int(input("Enter third number :"))
if num1>=num2 and num1>=num3:
    print("Largest number is:",num1)
elif num2>=num1 and num2>=num3:
    print("Largest number is:",num2)
else:
    print("Largest number is:",num3)