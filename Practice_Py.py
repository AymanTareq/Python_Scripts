


# p = ['pen','pencil']
# pp = [10,20]

# pd = {}
# pd.update({'a':20,'b':10})
# print(pd)



# def odd_even_checker(*vlaue):
#     for i in range(0,len(vlaue)):
#         if vlaue[i]%2==0:
#             return 'even'
#         else:
#             return 'odd'

# print(odd_even_checker(20))






# number = int(input("Enter number "))
# number1 = int(input("Enter number "))

# print("\n")
# # 'd' is for integer number formatting
# print("The number is:{:d}".format(number))

# 'o' is for octal number formatting, binary and hexadecimal format
# print('Output number in octal format : {0:o}'.format(number))

# 'b' is for binary number formatting
# print('Output number in binary format: {0:b}'.format(number))

# 'x' is for hexadecimal format
# print('Output number in hexadecimal format: {0:x}'.format(number))

# 'X' is for hexadecimal format
# print('Output number in HEXADECIMAL: {0:X}'.format(number, number1))



# text = input("Enter text: ")

# print("\n")
# # left aligned
# print('{:<100}'.format(text)) 
# # Right aligned 
# print('{:>100}'.format(text))
# # centered
# print('{:^100}'.format(text))


# my_info = []
# print("Tell me about yourself: ")
# while True:
#     single_line = input()
#     if single_line:
#         my_info.append(single_line)
#     else:
#         break
# my_info = '\n'.join(my_info)
# print('\n')
# print(my_info)



# name, age = input('Enter your name and age: ').split()
# print(f"{name} is  {age} years old.")


# name, age, phone = input("Enter your name, Age, Percentage separated by space ").split()
# print("\n")
# print("User Details: ", name, age, phone)


# listLen = int(input("Enter the number of sublist "))

# print("\n")
# finalList = [[int(input("Enter number: ")) for _ in range(listLen)] for _ in range(listLen)]
# print("List is")
# print(finalList)



# n = int(input("Enter the size of the list: "))
# print("\n")
# sum = 0
# numList = list(sum + int(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]
# print("User List: ", numList)
# print(sum)



# numberList = []
# n = int(input("Enter the list size : "))
# x, y = 10, 20
# print("\n")
# for i in range(0, n):
#     item = int(input(f"Enter number x}, {y{} at location {i}: "))
#     # item = int(input())
#     numberList.append(item)
# print("User List is ", numberList)
# print(sum(numberList))



# x = input('Entr a num: ')
# y = input(f"a num less than {x} : ")
# print(y)


# numberList = []
# n = int(input("Enter the list size : "))

# print("\n")
# for i in range(1, n+1):
#     print("Enter number at location", i, ":")
#     item = int(input())
#     numberList.append(item)
# print("User List is ", numberList)




# lst =input('Enter a lst of numbers: ').split(' ')
# x, y, z = lst

# print(lst)
# print('\n')
# print(x)
# print(y)
# print(z)
# print('\n')
# sum = 0
# for num in lst:
#     sum += int(num)

# print(sum)
# # print(sum(lst))






# z = eval(input('num1: '))
# h = eval(input('num2: '))
# s = z + h
# print(s)



# name = input("Enter Employee Name ")
# salary = input("Enter salary ")
# company = input("Enter Company name ")

# print("\n")
# print("Printing Employee Details")
# print("Name", "Salary", "Company")
# print(name, salary, company)
# print('ehlool sdfd dkf dsfj fjdslk kjfl df fj jd')
# print('\n')
# # print('\n')
# # print('\n')
# print("You're my best friend. ")