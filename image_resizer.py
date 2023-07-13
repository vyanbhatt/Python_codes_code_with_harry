import cv2

#to load image 
image = cv2.imread('vasu.jpg') 
cv2.imshow('my_photu',image)

#windows will show the mage until you press any key
cv2.waitKey(0)

width = int(input("Please enter width you want to set"))
height = int(input("Please enter height you want to set"))

dsize = (width,height) #its tupple

# resize image
output = cv2.resize(image, dsize)

#make the change pemanent
cv2.imwrite('vasu.jpg',output)

