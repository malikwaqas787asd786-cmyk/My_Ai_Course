#Tuple Slicing
data=(10,20,30,40,50,60,70,80,90)
print(data) # Original Tuple
print(data[2:7]) #(30, 40, 50, 60, 70)
print(data[:5]) #(10, 20, 30, 40, 50)
print(data[4:]) #(50, 60, 70, 80, 90)
print(data[-5:-2]) #(50, 60, 70)

#Tuples Methods
data=(10,20,30,40,50,30,30)
print(data)
print(type(data))
print(data.count(30))  # Count occurrences of 30
print(data.index(30))  # Find index of 3runner