import math

a = int(input("Enter the Length A : "))
b = int(input("Enter the Length B :"))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print (c)
print(type(c))


age = int(input("Enter Your Age : "))
if age >= 18 :
    print("Adult")
elif age <=0 :
    print("Invalid age")
else :
    print("Child")


response = input("Do you want Some Food (Y/N) : ")
if response == "Y" or response == "y":
    print("Yes I have Some Food")
else :
    print("No Enough")


name = input("Enter Your Name : ")

if name == "":
    print("Enter All Fields")
else :
    print(f" {name} ")





