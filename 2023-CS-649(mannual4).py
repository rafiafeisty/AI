#Task 1

num1=10
num2=6
num3=15
print("The maximum of three numbers",num1,",",num2,", and ",num3, "is: ", max(num1,num2,num3))


#Task 2
s=input("Enter a string: ")
print("The reverse string is: ",s[::-1])


#Task 3
def factorial(s):
    if s>0:
        if s==0:
            return 1
        elif s==1:
            return 1
        else:
            return factorial(s-1)*s

s2=int(input("Enter a number: "))
print("Factorial of the ", s2, " is: ",factorial(s2))
