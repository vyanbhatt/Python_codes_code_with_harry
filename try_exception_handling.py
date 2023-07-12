
while(True):
    try: #if code succesfully runs,it comes under try
        a = int(input("Enter your number : "))
        print(a+10)
        break

    except:#when try fails and exception occured it's handled here
        print("You have not entered a valid number,please try again")
'''suppose user enters his name
then to handle such cases we 
do excepton handling,
in above case even if you'll enter a float
it will still goes inside exception since 
according to program logic we are converting
input in integer'''

#To print and check taht exception
try: #if code succesfully runs,it comes under try
        a = float(input("Enter your number : "))
        print(a+10)
    
except Exception as e:#when try fails and exception occured it's handled here
    print("You have not entered a valid number,please try again",e)


