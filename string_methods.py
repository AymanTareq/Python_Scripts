txt = "bangladesh is my HOMELAND."

print(txt.upper())          # convert the whole string into uppercase 
print(txt.lower())          # convert the whole string into lowercase
print(txt.casefold())       # Similar to lower() method. but more strong.
print(txt.capitalize())     # Capitilize first chr of every line.  
print(txt.title())          # Capitilize first chr of every word in a line.

word_lst = txt.split()      # Return a list of words in txt.
print(word_lst)

new_txt = txt.replace('my', 'our')  # replace a substring with another substring
print(new_txt)

txt1 = 'Ayman Tareq'
x = txt1.center(150, "x")
print(x)

print(txt.count('a'))       # it returns how many times 'a' occurs in txt.
print(txt.count('a',2,10))       # it returns how many times 'a' occurs in txt.

# print()

# Python String encode() Method
# The encode() method encodes the string, using the specified encoding. If no encoding # is specified, UTF-8 will be used.

encoded_txt = txt.encode()      # default encoding value is UTF-8
print(encoded_txt)

txt2 = "My name is Ståle"
txt2 = "My name is Tareq"
txt2 = "My name is Tareq💦❤🆎Â"

print(txt2.encode(encoding="ascii",errors="backslashreplace"))
print(txt2.encode(encoding="utf-8",errors="ignore"))
print(txt2.encode(encoding="ascii",errors="namereplace"))
print(txt2.encode(encoding="ascii",errors="replace"))
print(txt2.encode(encoding="ascii",errors="xmlcharrefreplace"))

# # string.endswith(value, start, end) 
# print(txt.endswith('.'))        # return True or False

# string.expandtabs(tabsize)    default is 8
txt3 = "H\te\tl\tl\to"

print(txt3)
print(txt3.expandtabs())
print(txt3.expandtabs(tabsize=2))
print(txt3.expandtabs(4))
print(txt3.expandtabs(10))

# Python String find() Method
# syntax: string.find(value, start, end)
# print(txt.find('my'))       # return index of 'my'
# The find() method is almost the same as the index() method, the only difference is #that the index() method raises an exception if the value is not found.
# print(txt.index('my'))

##  Python String format() Method
# # syntax: string.format(value1, value2...) 
txt4 = "For only {price:.2f} dollars!"
print(txt4.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

print(txt.isalnum())
"""The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

Example of characters that are not alphanumeric: (space)!#%&? etc."""

txt = "helo12"
print(txt.isalpha())
txt = "332"
print(txt.isdigit())

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

a = "\u0030" #unicode for 0     #true
b = "\u00B2" #unicode for ²     # true
c = "10km2"         #false
d = "-1"            #false
e = "1.5"           # false
f = "2154"          # True

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print(f.isnumeric())

txt = "I'm ayman\n I'm from Bangladesh\n Programming is my favourite game!\n"
line = txt.splitlines()
print(line)             
# ["I'm ayman", " I'm from Bangladesh", ' Programming is my favourite game!']

txt = "Hello, bROthEr"
print(txt.swapcase())       # return hELLO, BroTHeR

# The zfill() method adds zeros (0) at the beginning of the string, 
# until it reaches the specified length.
a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))          # 00000hello
print(b.zfill(10))          # welcome to the jungle
print(c.zfill(10))          # 000010.000

txt = 'Hello world.'
print(txt.startswith('H'))      # True
print(txt.startswith('h'))      # False




