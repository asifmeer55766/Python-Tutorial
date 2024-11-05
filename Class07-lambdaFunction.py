# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# syntax 
# lambda arguments : expression 


# x = lambda a : a*10
# print(x(5))


def myRolNo(rollno):
    return lambda a: a * rollno;
myRolNo = myRolNo (10)
print(myRolNo(5))