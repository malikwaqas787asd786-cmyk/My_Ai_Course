#While Loop
#First Question
i=1
while i<=100:
    print(i)
    i+=1
print("loop ended")


#Second Question
i=100
while i>=1:
    print(i)
    i=i-1
print("loop ended")


#Third Question 
i=1
n=int(input("Enter number"))
while i<=10:
    print(i*n)
    i=i+1

#Fourth Question
n=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(n):
    print(n[idx])
    idx=idx+1

n=["ironman","superman","batman","thor"]
i=0
while i<len(n):
    print(n[i])
    i=i+1


#Fiveth Question 
num=(1,4,9,16,25,36,49,64,81,100)
i=0 #Initialization 
while i<len(num):
    print(num[i])
    i=i+1


num=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0 #Initialization 
while i<len(num):
    if(num[i]==x):
        print("Founded at idx",i)
    else:
        print("Finding....")
    i=i+1

#For Loop Questions
#First Question
list=[1,4,9,16,25,36,49,64,81,100]
for nums in list:
    print(nums)

#Second Question
tup=(1,4,9,16,25,36,49,64,81,100)
x=49
idx=0
for val in tup:
    if (val==x):
        print("value founded at idx",idx)
    idx+=1

#Using for and range:
#1st Question
for i in range(1,101):
    print(i)

#2nd  Question
for i in range(100,0,-1):
    print(i)

#3rd Question
n=int(input("Enter a number"))
for i in range(1,11):
    print(n*i)

#4th Question
n = int(input("Enter n: "))

sum = 0
for i in range(1, n + 1):
    sum = sum + i

print("Sum of first", n, "natural numbers is:", sum)

#Fiveth Question
n = int(input("Enter n: "))

fact = 1
for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is:", fact)
