# This is simple calculator made by me.
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

print("Choose an option:\n 1.Add \n 2.Subtract \n 3.Multiply\n 4.Division")
user_choice = input(">")
while user_choice not in ['1', '2', '3', '4']:
    print("invalid choice!")
    user_choice = input(">")
    continue
else:
    try:
        num1 = int(input("First number:"))
        num2 = int(input("Second number:"))
        if user_choice == "1":
            print("Result = ",add(num1,num2))
        elif user_choice == "2":
            print("Result = ",subtract(num1,num2))

        elif user_choice == "3":
            print("Result = ",multiply(num1,num2))

        elif user_choice == "4":
            print("Result = ",division(num1, num2))
        else:
            pass
    except:
        print("Cannot divided by zero")


# Another way to do this. this code collected from geeksforgeeks
"""
# Python program for simple calculator 

# Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 

print("Please select operation -\n" \ 
		"1. Add\n" \ 
		"2. Subtract\n" \ 
		"3. Multiply\n" \ 
		"4. Divide\n") 


# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :")) 

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

if select == 1: 
	print(number_1, "+", number_2, "=", 
					add(number_1, number_2)) 

elif select == 2: 
	print(number_1, "-", number_2, "=", 
					subtract(number_1, number_2)) 

elif select == 3: 
	print(number_1, "*", number_2, "=", 
					multiply(number_1, number_2)) 

elif select == 4: 
	print(number_1, "/", number_2, "=", 
					divide(number_1, number_2)) 
else: 
	print("Invalid input") 


"""
# Another way to do this. this code collected from Programiz.com, i think a little bit better way.
"""
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

"""