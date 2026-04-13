# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("The sum of the two numbers is:" + str(a + b))

# strip()
# s = "***** hello world!  *****    "
# print(s.strip().strip("*").strip().strip("!").title())

# substring
# s = "Hello, welcome to the world of Python programming!"
# print(s[0:5])  # Output: Hello
# print(s[7:14]) # Output: welcome
# print(s[-12:])  # Output: programming!


# s="abc;def;ghi;jkl"

# a= s.index(";")
# b= s.rindex(";")

# print(s[a + 1:])  
# print(s[:b])
# print(s[a + 1:b])

# email = input("Enter your email address: ")
# indx_At = email.index("@")
# print("Hello ", email[:indx_At].title(), "!")


# #all char after the first ';'
# print(s[s.find(";")+1:])  # Output: def;ghi
# #all char before the first ';'
# print(s[:s.find(";")])  # Output: abc
# #include the ';'
# print(s[s.find(";"):s.find(";")+1])  # Output: ;
# #exlude the ';'
# print(s.split(";"))  # Output: ['abc', 'def', 'ghi']

# Replace
s = "cat dog cat bird cat"
print(s.replace("cat", "lion", 2))  # Output: fish dog fish bird fish

