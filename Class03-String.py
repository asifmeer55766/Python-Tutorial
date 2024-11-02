# string slicing 
myString = "Asif Hussain"

print(myString[:10]);
# output Asif Hussa 
print(myString[10:]); # output in Hussain


print(myString.upper())
print(myString.lower())
print(myString.strip()) #output is the same as above because of the no whitespace from end and start
print(myString.replace("Hussain", "Hussaini"))

print(myString.split(",")) #output [Asif Hussain]

firstName = "Muhammad"
lastName = "Asif"
print(firstName + " " + lastName) #output Muhammad Asif


# f string to formate string and put variable  like react {name};
name = "Asif"
age = 25
print(f"Hello, my name is {name} and I am {age} years old")


# string methods 
# 1. startswith() used to validate the string starts  
print(myString.startswith("Asif")) #output True
# 2. endswith() used to validate the string ends
print(myString.endswith("n")) #output True
# 3. find() used to find the index of the first occurrence of the specified value
print(myString.find("H")) #output 2
# 4. rfind() used to find the index of the last occurrence of the specified value
print(myString.rfind("H")) #output 10


