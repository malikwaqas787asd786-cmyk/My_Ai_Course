#Conditional Statements

# If statement
age=21
if age>=18:
    print("You are eligible to vote.")

# If-Else statement
age=16
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# If-Elif-Else statement
marks=85
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Grade D")

marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Grade D")

# Nested If statement
age=18
if age>=18:
    if age<=60:
        print("You are eligible to work")
    else:
        print("You are retired")
else:
    print("You are not eligible to work")   

#Nested If-Else statement
age=int(input("Enter your age:"))
if age>=18:
    if age<=60:
        print("You are eligible to work")
    else:
        print("You are retired")
else:
    print("You are not eligible to work")