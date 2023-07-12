s = {1,1,2,3,4,4,6,0} #removes duplicates and sorts the elements

#following is the way to define empty set
a = set()
print(type(a))


print(s) 

#set methods
s1 = {1,1,2,3,6,7}
s2 = {1,1,2,3,6,9}

print(s1.intersection(s2))

print(s1.pop()) #Removes and returns an arbitrary set element

print(s1)