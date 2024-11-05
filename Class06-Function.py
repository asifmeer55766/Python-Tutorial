# # function in python 

# def printName(name):
#     print("Name is : " + name)

# Name = printName("asif hussain");
# print(Name)



# def printTable(table):
#     for i in range(1,11):
#        print( str(table) + " * " + str(i) + "=" + str(table*i))

# printTable(3)



# def printEvenNumber(evenNumber):
#     if(evenNumber % 2 == 0):
#         print(str(evenNumber) + " is  Even" )
#     else:
#         print(str(evenNumber) + " is Odd " )  

# printEvenNumber(11)



# recursion function 
def recursion(number):

    if(number > 0):
      result = number + recursion(number -1)
      print(result)
    else:
        result = 0;
        return result
recursion(10);