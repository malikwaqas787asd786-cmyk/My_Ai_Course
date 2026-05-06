#Recursive Function
def countdown(n):
    if n == 0:        
        print("Blast off! 🚀")
    else:
        print(n)
        countdown(n-1)   

countdown(5)

#Factorial of a number using recursion
def factorial(n):
    if n == 1:            # base case
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


#Sum of first n natural numbers
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(10))


#Print all elements of a list using recursion
def print_list(list, index=0):
    if index < len(list):
        print(list[index])
        print_list(list, index + 1)
my_list = [10, 20, 30, 40, 50]
print_list(my_list)