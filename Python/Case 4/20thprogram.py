#Break
i=1
while i<=5:
    print(i)
    if i==3:
        break
    i=i+1
    print("loop ended")

i=1
while i<=10:
    if (i==5):
        break
    print(i)
    i=i+1

#>Continue
i = 0
while i <=5:
    i=i+1
    if (i==3):
        continue #skip
    print(i)

i = 0
while i <=10:
    i=i+1
    if (i%2==0): #odd numbers 
        continue #skip
    print(i)

i = 0
while i <=10:
    i=i+1
    if (i%2!=0):#Even numbers 
        continue #skip
    print(i)

#Break and Continue
i=0
while i<10:
    i+=1
    if (i==3):
        continue    # 3 skip
    if (i==7):
        break      # loop stop
    print(i)
    