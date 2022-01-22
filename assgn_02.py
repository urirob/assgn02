# problem 1-For a given input string “Python is a case sensitive language”. Write python code for the following:
#a. Find the length of the input string.
#b. Reverse the order of the string in one line code.
#c. Using Slice function store “a case sensitive” in new string.
#d. Replace “a case sensitive” with “object oriented”.
#e. Find index of substring “a” in the given input string.
#f. Remove the white spaces from the given input string.


a= "Python is a case sensitive language"
# print(len(a)) <----- part (a)

# b=a[::-1]
# print(b)  <---- part(b)

# c=a[9:35]
# print(b)  <---- part (c)

# d=a.replace("a case sensitive language", "object oriented")
# print(d)  <---- part(d)

# e=a.index("a")
# print(e)  <---- part(e)

# def remove(a):
#     return a.replace(" ", "")
# f=print(remove(a))    <---- part(f)


#problem 2- Store your name, SID, department name and CGPA into different variables. With the help of String formatting print the following output:
# Hey, ABC Here!
# My SID is 2110XXXX
# I am from XYZ department and my CGPA is 9.9

a=("Hey, ")
b=input("enter your name : \n")
c=(" Here!")
print(a+b+c)

a1=("My SID is ")
a2=str(int(input("enter you SID :\n")))
print(a1+a2)

b1=("I am from ")
b2=input(("enter the name of department: \n"))
b3=(" and my CGPA is ")
b4=str(float(input("enter your CGPA :\n")))
print(b1+b2+b3+b4)


# probem 3:For a=56 and b=10 with the help of bitwise operators calculate the following:
# a. a&b
# b. a|b
# c. a^b
# d. Left shift both a and b with 2 bits.
# e. Right shift a with 2 bits and b with 4 bits.

a=56
b=10

print("a&b:", a&b)                      

print("a|b:", a|b)                      

print("a^b:", a^b)                      

print("a<<2, b<<2", a<<2, b<<2)                     

print("a>>2, b>>8", a>>2, b>>8)                     


# problem 4:Write a python program to find the greatest of three numbers entered by the user.

a1=int(input("enter the first number: \n"))
a2=int(input("enter the second number: \n"))
a3=int(input("enter the third number: \n"))

if (a1>a2):
    f1=a1
else:
    f1=a2

if(a2>a3):
    f2=a2
else:
    f2=a3

if(f1>f2):
    print(str(f1)+ " is the greatest")
else:
    print(str(f2)+ " is the greatest")

# problem5: Write a python program to check if the word “name” is present in the string entered by the user (Print : “Yes” or “No”).




a= str(input("enter your sentence: \n"))


if (a.find('name')!=-1):
    print("yes")
else:
    print("no")


# problem 6: For any three lengths, there is a simple test to see if it is possible to form a triangle. If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle. Otherwise, Enter three sides of a triangle, converts them to integers, and to check whether the given input lengths can form a triangle or not (Print : “Yes” or “No”).

a=int(input("enter the length of first side: \n"))
b=int(input("enter the length of second side: \n"))
c=int(input("enter the length of third side: \n"))

if (a+b>c):
    print("Yes")

else:
    print("No")
