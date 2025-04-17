
def factorial(n):
    if n<2:
        return 1
    else:
        return n* factorial(n-1)
    
num=input("Enter a number: ")
result=factorial(int(num))
print("Factorial of "+num+" is: "+str(result))
