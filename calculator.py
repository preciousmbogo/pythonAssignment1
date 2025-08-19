num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
mathOperation = input("Enter mathematical operation (+, -, *, /): ")
if mathOperation == "+":
    results = num1+num2
    print(f"{num1}+{num2}={results}")
elif mathOperation == "-":
    results = num1-num2
    print(f"{num1}-{num2}={results}")
elif mathOperation == "*":
    results = num1-num2
    print(f"{num1}*{num2}={results}")
elif mathOperation == "/":
    if num2 != 0:
        results = num1/num2
        print(f"{num1}/{num2}={results}")
    else:
        print("Error: division by 0 is not allowed.")
else:
    print("Invalid operation")