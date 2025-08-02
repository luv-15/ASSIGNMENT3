import math  

number = float(input("Enter a positive number: "))

if number > 0:
    square_root = math.sqrt(number)
    natural_log = math.log(number) 
    sine_value = math.sin(number)  

    print(f"Square root : {square_root}")
    print(f"logarithm : {natural_log}")
    print(f"Sine : {sine_value}")
else:
    print("Please enter a number greater than 0 for valid calculations.")