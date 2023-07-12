a = int(input("Enter number a : "))

'''match case is exactly switch case in c++
    but unlike in c++ where we can put default case
    anywhere here we must put it in the end else will
    give an error'''
match a:

    case 1:
        print("a is 1 ")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:  #represents default case
        print("Number a is not 1 , 2 and 3 ")