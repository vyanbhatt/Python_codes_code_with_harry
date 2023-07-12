def greetHello(): #Defining a function
    print("Hello bro")


greetHello() #calling a function

#function with arguments
def add_val(a,b):
    print(a+b)

def greet_name(name):
    print("Hello "+name) #addition operator will concatenate

add_val(23,10)
greet_name(input("enter your name "))

#function with argument and return value
def add_ret(a , b):
    return a+b

b = add_ret(23,60)
print(b)