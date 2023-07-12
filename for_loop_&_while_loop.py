
#note -> Python has continue and break similar to c++ and can be used with for and while loop

#1)for loop

for i in range(5): #i starts form 0 and goes till 4
    print(i)

print()

#we can set the range of our for loop in below way
#suppose we want to run our for loop from 80 to 85
for a in range(80,86):
    print(a)

print()

a = [1 , 4 , 5 , 5 , 6 , 6 , 10] #here inplace of list we can use set,tupple and dictionary
for j in a:
    print(j)

print()

s  = {1 , 4 , 5 , 5 , 6 , 6 , 10 , 0} #with set
for j in s:
    print(j)

print("below is while loop")
#2)while loop
i= 5
while(i>0):
    print(i)
    i-=1

print("While loop completed")