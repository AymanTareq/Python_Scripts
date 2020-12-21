txt = "bangladesh is my HOMELAND."

# print(txt.upper())          # convert the whole string into uppercase 
# print(txt.lower())          # convert the whole string into lowercase
# print(txt.casefold())       # Similar to lower() method. but more strong.
# print(txt.capitalize())     # Capitilize first chr of every line.  
# print(txt.title())          # Capitilize first chr of every word in a line.

# word_lst = txt.split()      # Return a list of words in txt.
# print(word_lst)

# new_txt = txt.replace('my', 'our')  # replace a substring with another substring
# print(new_txt)

# txt1 = 'Ayman Tareq'
# x = txt1.center(150, "x")
# print(x)

# print(txt.count('a'))       # it returns how many times 'a' occurs in txt.
# print(txt.count('a',2,10))       # it returns how many times 'a' occurs in txt.

# print()

# Python String encode() Method
# The encode() method encodes the string, using the specified encoding. If no encoding # is specified, UTF-8 will be used.

# encoded_txt = txt.encode()      # default encoding value is UTF-8
# print(encoded_txt)

# txt2 = "My name is Ståle"
# txt2 = "My name is Tareq"
# txt2 = "My name is Tareq💦❤🆎Â"

# print(txt2.encode(encoding="ascii",errors="backslashreplace"))
# print(txt2.encode(encoding="utf-8",errors="ignore"))
# print(txt2.encode(encoding="ascii",errors="namereplace"))
# print(txt2.encode(encoding="ascii",errors="replace"))
# print(txt2.encode(encoding="ascii",errors="xmlcharrefreplace"))

# # string.endswith(value, start, end) 
# print(txt.endswith('.'))        # return True or False

# # string.expandtabs(tabsize)    default is 8
# txt3 = "H\te\tl\tl\to"

# print(txt3)
# print(txt3.expandtabs())
# print(txt3.expandtabs(tabsize=2))
# print(txt3.expandtabs(4))
# print(txt3.expandtabs(10))

# Python String find() Method
# syntax: string.find(value, start, end)
# print(txt.find('my'))       # return index of 'my'
# The find() method is almost the same as the index() method, the only difference is #that the index() method raises an exception if the value is not found.
# print(txt.index('my'))

##  Python String format() Method
# # syntax: string.format(value1, value2...) 
# txt4 = "For only {price:.2f} dollars!"
# print(txt4.format(price = 49))

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)
# print(txt2)
# print(txt3)



