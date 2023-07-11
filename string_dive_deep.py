name1="vasu bhatt"
name2='bholo'
#It allows string between single and double quotes both

print(name1)
print(name2)

#how to slice the string
#Note that in slicing, python creates a new string and copied chars from original string
print(name1[0:2])#starts from 0 and goes till 1
print(name1[0:4])#starts from 0 and goes till 3

#String functions
print(name1.capitalize())#converts the string in capital
print(name2.count('bh'))#counts occurences of substring bh in given string
