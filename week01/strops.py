y = "SAMPLE STRING"
x = "sample string"
print(x.capitalize()) # capitalize first word of entire string
print(y.casefold()) #lower case the string
print(x.center(50)) # center the string in a field of a given width (50 in this case) and fill the remaining space with spaces
print(x.count("s")) # return the total number of  char in the string             
print(y.encode())# return the encoded version of the string in bytes
print(x.endswith("g")) # return true if the string ends with the given char
print("hello\tworld".expandtabs(4))#manually change tab size in the string
# x = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# print(x) # formst specified values in string
print(x.index("g"))
# isalpha(), is alnum(), isdigit(), isascii(), isidentifier()
# is numeric() Everything accepted by isdigit() plus other numeric Unicode characters (fractions, numerals, etc.)
print(x.isalnum())
print("py" in x) # membership operator
print("py" not in x) #membership
print(f"reversed string: {x[::-1]}") #indexing
txt = "     hello     "
print("hi, " + txt.lstrip()) #lstrip removes spaces before and after the string 
print(x.split(" ",-1)) # split the string into elements of list according to the spaces
# first is separator and second is how many splits -1 means max
print(y.swapcase()) # swap lowercase with upper and upper with lower

z = x+"s"
z = "-".join(x)#join each char of string with given char in join
# q = y.join(x)  can work with var with string also
print(z)
f = x.find("p")#find the index of given character in the string
print(f)
print(y.title()) # capitalize first letter of each word in the string
print(x.upper())# convert the string to uppercase
print(x.replace(" ", "``")) #replace the given char with new char


# dict = {"string":"word"}
# print(x.translate(dict)) #-----later