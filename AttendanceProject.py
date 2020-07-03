import cv2
import os
from Encoding import findEncodings
from Webcam_Recognition import webcamRecognition

path = 'C:/Users/user/Desktop/Project/Attendance Management using Face Recognition/Images'
images = []
classNames = []
classRollno = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    nameLine = os.path.splitext(cl)[0]  # Splitting the image name and extension
    nameEntry = nameLine.split(",")
    classNames.append(nameEntry[0])
    classRollno.append(nameEntry[1])
# print(classNames)


# findEncoding(images) was here

# markAttendance(name, rollno) was here


print('Encoding in progress...')
encodeListKnown = findEncodings(images)
print('Encoding Complete!')

# Webcam function call
webcamRecognition(encodeListKnown, classNames, classRollno)