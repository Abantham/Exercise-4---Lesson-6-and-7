fruits = ("apple", "pineapple", "bannana", "pear")

for fruit in fruits:
 print(fruit)




count = 5

while count > 0:
 print(count)
 count -= 1




for i in range(1,11):
 square = i ** i
 print(f"The square of {i} is {square}")






import random 
colors = ("black", "grey" , "blue" , "green" , "yellow")

for _ in range(3):
 random_color = random.choice(colors)
 print(random_color)


import math_operations

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    
    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break
        

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
            
    
        if choice == '1':
            result = math_operations.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = math_operations.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = math_operations.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = math_operations.divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid Choice. Please select a number from 1 to 5.")
