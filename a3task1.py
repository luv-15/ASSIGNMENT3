def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  
    return result  

number=int(input("enter a number :"))
print(f"factorial of {number} is: {factorial(number)}")
