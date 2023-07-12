a = {} #this represents a dicstionary and not an empty set
print(a,type(a))

a = {2:5 , 3:6} #Key:Value

print(a[2]) #Similar to c++ we can access value by indexing keys

b={"vasu":1 , "batman":2 , "flash":100}
print(b["vasu"],b["flash"])

#Methods
print(b.get("vasu"))
print(b.get("Chipkali")) #when the key doesnt exist it gives none
b["rambo"]=100 #dicstionary is mutable
print(b)

print(b.keys())
print(b.values())

