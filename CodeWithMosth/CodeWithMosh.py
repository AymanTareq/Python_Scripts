









# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference


# wb = xl.load_workbook('pywithxl.xlsx')
# sheet = wb['Sheet1']
# # cell = sheet['a1']
# cell = sheet.cell(1, 1) #another approach
# # print(cell.value)
# # print(sheet.max_row)
# for row in range(2, 5):
#     cell = sheet.cell(row, 3)
#     corrected_price = cell.value * 0.9
#     corrected_price_cell = sheet.cell(row, 4)
#     corrected_price_cell.value = corrected_price

# values = Reference(sheet,
#             min_row=2,
#             max_row=4,
#             min_col=4,
#             max_col=4
#             )
# chart = BarChart()
# chart.add_data(values)
# sheet.add_chart(chart, 'e2')

# wb.save('pywithxl3&chart.xlsx')


# from pathlib import Path

# path = Path()
# print(path.glob('*')) # its return an iterable object
# for file in path.glob('*'):
#     print(file)






# from pathlib import Path
# path = Path("emails")
# print(path.exists())
# print(path.is_absolute())
# path.mkdir()
# path.rmdir()




# import random
# class Dice:
#     def roll(self):
        # this method generates two random number and return it. 
#         self.x = random.randint(1, 10)
#         self.y = random.randint(1, 15)
#         return (self.x, self.y)

# roll1 = Dice()
# print(roll1.roll()) 






# import random

# for i in range(5):
#     print(random.random())
#     print(random.randint(10, 50))

# leaders = [ 'Tareq', 'Hossain', 'Iqbal', 'Rahman', 'Ratul']
# print(random.choice(leaders))






# from my_py_package import shipping
# import my_py_package
# shipping.calc_shipping()
# print(type(my_py_package))
# print(type(shipping))
# print(type(shipping.calc_shipping))

# from my_py_package.shipping import calc_shipping
# calc_shipping()

# import my_py_package.shipping
# my_py_package.shipping.calc_shipping()




# my_list = [ 34, 3,43, 34, 34, 3,6,98, 12, 32 ]
# from utils import find_max

# max = find_max(my_list)
# print(max(my_list)) # here max is an int number not a function so we can't call it as function. 
#  it's produce and error TypeError: 'int' object is not callable




# import utils
# from utils import find_max

# my_list = [ 34, 3,43, 34, 34, 3,6,98, 12, 32 ]

# max = utils.find_max(my_list)
# print(max)

# print(find_max(my_list))



# class Mammal:
#     def walk(self):
#         print("Walk")


# class Dog(Mammal):
#     #Dog class inherits the properties of Mammal class
#     def bark(self):
#         print('Dog can bark!')
    

# class Cat(Mammal):
#     pass

# dog1 = Dog()
# dog1.walk()
# dog1.bark()

# cat1 = Cat()
# cat1.walk()




# class Person:

#     def __init__(self, name, language):
#         self.name = name
#         self.language = language
#     def talk(self):
#         print(f"Name: {self.name} and spoken language: {self.language}")

# tareq = Person('Tareq','Bangla')
# tareq.talk()
# name = input('Enter your name: ')
# lan = input('Enter your language: ')
# person2 = Person(name, lan)
# person2.talk()




# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('Hello')

#     def draw(self):
#         print('draw')

# point1 = Point(10, 20)
# print(point1.x)
# print(point1.y)






# try:
#     age = int(input('Age: '))
#     income = 25000
#     risk = income / age
#     print('Risk:',risk)
#     print(age)
# except ZeroDivisionError:
#     print('age cannot be zero.')
# except ValueError:
#     print('Invalid Value!')




# def emoji_converter(text):
#     emoji_mapping = {
#     ':)': '🙂',
#     ':(': '😔'
#     }

#     text_words = text.split(' ')
#     output_text = ''
#     for word in text_words:
#         output_text += emoji_mapping.get(word,word) + ' '
#     return output_text

# text = input('> ')
# print(emoji_converter(text))







# def greet_msg(fname, lname):
#     print(f'Hey, {fname} {lname}!')
#     print('Welcome to Python.')

# greet_msg('Tareq',"Hossain")

'''emoji_mapping = {
    ':)': '🙂',
    ':(': '😔'
}
text = input('> ')
text_words = text.split(' ')
output_text = ''
for word in text_words:
    output_text += emoji_mapping.get(word,word) + ' '
print(output_text)
'''


'''num_spelling = {
    '1': 'one ',
    '2': 'two ',
    '3': 'three ',
    '4': 'Four ',
    '5': 'Five ',
    '6': 'six ',
    '7': 'seven ',
    '8': 'eight ',
    '9': 'nine ',
    '0': 'zero '
}
phone = input('Phone: ')
for digit in phone:
    print(num_spelling.get(digit), end = '')
'''


# dictionaries
# customer = {
#     'name' : 'Tareq',
#     'phone': '01815475818'
# } 
# customer['age'] = 23
# print(customer.get('class'))
# print(customer)



# t1 = (2, 4, 5,)
# print(t1.index(4,1,3))

# # Unpacking
# x , y, z = t1
# print(x)
# print(y)
# print(x * y * z)



# # remove dupllicate from a list.
# lst = [ 3, 5, 6, 1, 4, 4, 3, 23, 5, 3]
# for item in lst:
#     if lst.count(item) > 1:
#         lst.remove(item)
# print(lst)


# # remove dupllicate from a list. 
# lst = [ 3, 5, 6, 1, 4, 4, 3, 23, 5, 3]
# lst2 = list()
# for item in lst:
#     if item not in lst2:
#         lst2.append(item)
# print(lst)
# print(lst2)





# lst = [2, 4, 33, 41, 34, 6, 76, 9]
# lgst = None
# for num in lst:
#     if lgst is None or lgst < num:
#         lgst = num
# print(lgst)
# # or use max fucntion
# print(max(lst))


'''lst = [ 5, 2, 5, 2, 2]
for i in lst:
    output = ''
    for item in range(i):
        output = output + 'X'
    print(output)'''



# already_start = False
# already_stop = False
# while True:
#     user_cmd = input('> ').lower()
#     ins_for_user = '''
#     start - To start car.
#     stop - To stop car.
#     help - To get instructions. 
#     quit - To exit.
#     '''
#     if user_cmd == 'help':
#         print(ins_for_user)
#     elif user_cmd == 'start':
#         if already_start:
#             print('Hey, Car has been alrady started.')
#             continue
#         print('Car started...Ready to go!')
#         already_start = True
#         already_stop = False
#     elif user_cmd == 'stop':
#         if already_stop:
#             print("Hey, Car has already stopped.")
#             continue
#         print('Car stopped.')
#         already_stop = True
#         already_start = False
#     elif user_cmd == 'quit':
#         quit()
#     else:
#         print("I don't understand what you say.")






"""secret_num = 5
i = 1

while i <= 3:
    guess_num = int(input('Guess: '))
    i += 1
    if guess_num == secret_num:
        print('You Won!')
        break
    else:
        continue
else:
    print('Sorry You failed.')
"""



'''weight = input('Weight: ')
lbs_or_kg = input('(L)bs or (K)g: ').lower()

if lbs_or_kg == 'l':
    weight = float(weight) * 0.45
    print('You are',weight, 'pounds.')
elif lbs_or_kg == 'k':
    weight = float(weight) / 0.45
    print('You are',weight, 'kilos.')
else:
    print('Wrong Input.')
'''



'''name = input('Enter your name: ')
if len(name) < 3:
    print('Name must be at least 3 characters long.')
elif len(name) > 50:
    print('Name can be maximum of 50 characters.')
else:
    print('Name looks good!')

'''

"""import math

x = 2.6
y = math.floor(x)
print(y)
print(math.ceil(x))
n = 10
print(math.factorial(n))
"""



'''fname = 'Ayman'
lname = 'Tareq'
message = f'{fname} [{lname}] is a coder.'
print(message)
'''



'''name = 'Jennifer'
print(name[1:-1])'''


"""
email = '''
Hi Tareq,

Here is our first email to you.

Thank you,
The support team
'''
print(email)"""



'''weight = input('Weight (lbs): ')
weight_kg = float(weight) * 0.45
print("You are", weight_kg,'kg.')'''



'''name = input('what is your name? ')
color = input('What is your favourite color? ')

print(name + ' likes ' + color)

'''
'''print('hello')
print('o----')
print(' ||||')
print('*' * 10, '^' * 5)
print('         [<>]' * 5)'''

