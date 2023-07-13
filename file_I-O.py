st = "Vasu is a good boy" #we want to store this st in text file

'''writing to a file

This is first method to write in a file,
note when we open an existing file in Write
mode and write something, it will totall erase
the old content of file and add newly wrote stuff
with open("text.txt","w") as f:
    f.write(st)

#this is second method exactly similar to above
fp = open("text.txt","w")
fp.write(st)
fp.close()'''

#reading from a file
'''with open("test.txt","r") as f:
    st = f.read()

print(st)'''

#second method
f=open("test.txt","r")
s= f.read()
print(s)
f.close()


'''When we dont want to erase old content of file
and also want to write in it, we open it in append mode'''

#append mode
fp = open("test.txt","a")
fp.write("Yo im writing this in append mode ")
fp.close()