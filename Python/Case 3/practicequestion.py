# Practice Questions of List
# Favorite Movies Input
movies=[]
movie1=input("Enter the name of your first favorite movie:")
movie2=input("Enter the name of your second favorite movie:")
movie3=input("Enter the name of your third favorite movie:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print("Your favorite movies are:", movies)

# Palindrome Check
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()
if copy_list1==list1:
    print("Palindrome")
else:
    print("Not Palindrome")
 
#Occurrence Count of A in a Tuple
grades=("C","D","A","A","B","B","A")
print(grades)
print(grades.count("A"))

#Sorting the grades 
grades=["C","D","A","A","B","B","A"]
grades.sort()
print(grades)