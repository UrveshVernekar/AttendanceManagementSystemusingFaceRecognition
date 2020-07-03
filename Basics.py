import cv2
import numpy as np
import face_recognition

imgRDJ = face_recognition.load_image_file('Images/RDJ.jpeg')
imgRDJ = cv2.cvtColor(imgRDJ, cv2.COLOR_BGR2RGB)
imgRDJTest = face_recognition.load_image_file('Images/Snehal Chodankar.jpg')
imgRDJTest = cv2.cvtColor(imgRDJTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgRDJ)[0]
encodeRDJ = face_recognition.face_encodings(imgRDJ)[0]
cv2.rectangle(imgRDJ, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)  # top, right, bottom, left

faceLocTest = face_recognition.face_locations(imgRDJTest)[0]
encodeTest = face_recognition.face_encodings(imgRDJTest)[0]
cv2.rectangle(imgRDJTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeRDJ], encodeTest)
faceDis = face_recognition.face_distance([encodeRDJ], encodeTest)
print(results)
cv2.putText(imgRDJTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Elon Musk', imgRDJ)
cv2.imshow('Elon Test', imgRDJTest)
cv2.waitKey(0)