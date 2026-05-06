#for loop
nums=[1,3,5,7,9,11]
for val in nums:
    print(val)

tup=(1,2,3,4,5,8,9)
for num in tup:
    print(num)

str="apnacollege"
for chr in str:
    if(chr=="o"):
        print("o founded")
        break
    print(chr)
else:
    print("end")

#Range Function
for i in range(10):  #range(stop))
    print(i)
print("loop ended")

for i in range(2,10):  #range(start,stop)
    print(i)
print("loop ended")

for i in range(2,10,2):  #range(start,stop,step)
    print(i) 
print("loop ended")   

for i in range(2,100,2):  #Even Numbers
    print(i)
print("loop ended")


for i in range(1,100,2):  #Odd Numbers
    print(i)
print("loop ended")

#Pass Statement
for i in range(5):
    pass

if i>=5: 
    pass
print("some useful work")