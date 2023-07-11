#unlike array,in list we can store any type of values together

l1=[1 , 4 , 60.45 , 50 , "jordar bhai"]
print(l1)
print(type(l1)) #type function is used to print data type of variable

#list methods
l1.remove("jordar bhai") #removes element from list
print(l1)

print(l1.count(1)) #counts number of occurences of given element in list
print(l1.count(60))

l1.sort() #to sort the given list
print(l1)

l1.pop() #removes last element
print(l1)

l1.append(0) #adds an element at the end of list
print(l1)

print(l1[2]) #We can acces list elemets in similar way to c++