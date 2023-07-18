import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0) #here the argument means which web-cam you want to use,here 0th webcam

#Load known faces

vasu_image = face_recognition.load_image_file("faces/vasu.jpeg")
#creating encoding of images in numbers to make comparison of images possible
vasu_encoding = face_recognition.face_encodings(vasu_image)[0]
'''above we did [0] because if image has multiple faces
it will create encodings for all so we only need encoding for the 
first face(in our case it's the ony face)'''

babaji_image = face_recognition.load_image_file("faces/babaji.jpg")
babaji_encoding = face_recognition.face_encodings(babaji_image)[0]

#storing names of encodings
known_face_encodings = [vasu_encoding , babaji_encoding]
known_face_names = ["vasu" , "babaji"]


#list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

#GEt the current date and time

now = datetime.now()
current_date = datetime.now().strftime("%Y-%m-%d")


f = open(f"{current_date}.csv" , "w+", newline="")
lnwriter = csv.writer(f)

name = None

while True:
    #since read returns two arguments(success(bool),frame)
    # Hence we are writing it as _ , frame since we only want 
    # frame
    _, frame = video_capture.read()
    #below resizes the frame into smaller frame
    small_frame = cv2.resize(frame, (0,0), fx=0.25 , fy=0.25)
    
    #below converts bgr to rgb
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)

    #Converts webcam faces into encodings
    face_encodings = face_recognition.face_encodings(rgb_small_frame , face_locations)

    for face_encoding in face_encodings:
        #compares konwn face encodings to face encodings of webcam
        matches = face_recognition.compare_faces(known_face_encodings , face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings , face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

        #add text on person's video
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX #to choose font
            bottomLeftCorneroftext = (10,100)
            fontScale = 1.5
            font_clr = (255 , 0 , 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", bottomLeftCorneroftext , font , fontScale , font_clr , thickness , lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H - %M - %S")
                lnwriter.writerow([name, current_time])

    #to show the frame
    cv2.imshow("Attendace",  frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()







