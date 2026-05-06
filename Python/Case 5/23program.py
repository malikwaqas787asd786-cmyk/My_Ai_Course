#Types of functions 
#1. Build in functions 
#print function   
print("Hello Python")

#len function
text = "Python"
print(len(text))

#type function
x = 10
print(type(x))

#input function
name = input("Enter your name: ")
print(name)

#range function
for i in range(5):
    print(i)

#2. User defined functions
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)


def square(num):
    print(num * num)
square(4)

