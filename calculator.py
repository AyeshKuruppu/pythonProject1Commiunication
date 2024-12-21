operator = input("Enter an Operator (+ - * /) : ")
number1 = float(input("Enter the First Number : "))
number2 = float(input("Enter the Second Number : "))

if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "--":
    result = number1 - number2
    print(result)
elif operator == "*" :
   result = number1 * number2
   print(result)
elif operator == "/" :
   result = number1 / number2
   print(result)
else :
    print(f"{operator} is invalid ")
