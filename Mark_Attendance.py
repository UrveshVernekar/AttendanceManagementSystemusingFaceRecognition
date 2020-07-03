from datetime import datetime
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="test", passwd="test", database="test")
cursor = connection.cursor()

def markAttendance(name, rollno):
    with open('C:/Users/user/Desktop/Project/Attendance Management using Face Recognition/Attendance.csv', 'r+') as f:
        nameList = []
        rollnoList = []
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            rollnoList.append(entry[1])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {rollno}, {dtString}')

            # Database table entry
            query = """INSERT INTO attendance (name, rollno, time) VALUES (%s, %s, %s)"""

            tuples = (name, rollno, dtString)
            cursor.execute(query, tuples)
            connection.commit()
            print("Attendance marked for Roll No.: " + rollno)