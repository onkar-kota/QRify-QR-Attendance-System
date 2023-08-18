The QR Attendance System project is a clever solution to simplify attendance tracking using QR codes. We built this system with Python and SQL, which allowed us to automate the entire attendance management process.

Here's how it works:

### 1. QR Code Generation:
- We used Python to create QR codes for each student or employee in the system. These QR codes act like unique ID cards for each individual. They contain specific information that helps us identify the person, such as their name and ID.

### 2. QR Code Scanning:
- To mark attendance, students or employees simply need to present their QR code (ID card) in front of a camera. We utilized OpenCV, a library for computer vision, to scan and decode the QR codes from the images captured by the camera.

### 3. Database Management:
- As the QR codes get scanned, Python stores the attendance data in a database using SQL. This database keeps track of who attended and at what time, ensuring accurate attendance records.

### 4. Libraries Used:
- We leveraged helpful libraries like pyqrcode to generate QR codes easily, and qrtools to decode the scanned QR codes effectively.

# Breakdown of the [Code](https://github.com/onkar-kota/QRify/blob/main/QR_Attendance-main/QR_Attendance/Generate.py)

1. Import necessary modules:
```
from MyQR import myqr
import os
```

2. Open and read the 'students.txt' file:
```
f = open('D:/Coding Files/Coding Ninja/5. Projects/2. QR_Attendance/QR_Attendance-main/QR_Attendance/students.txt', 'r')
lines = f.read().split("\n")
print(lines)
```

3. Generate QR codes for each student and customize settings:
```
for _ in range(0, len(lines)):
    data = lines[_]
    version, level, qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="D:/Coding Files/Coding Ninja/5. Projects/2. QR_Attendance/QR_Attendance-main/QR_Attendance/Bg.png",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=str(lines[_] + '.png'),
        save_dir=os.getcwd()
    )

```
This loop iterates through each line in the 'students.txt' file. It takes the current line (student data) and generates a QR code using the myqr.run function. It sets the error correction level to 'H' (high), version to 1, and specifies a background image ('Bg.png') for the QR code. The colorized, contrast, and brightness parameters are also used to customize the appearance of the QR code. The generated QR code is saved with the student's data as the filename (plus '.png') in the current working directory.


# Benefits of the QR Attendance System:

### 1. Accuracy and Efficiency:
- Since QR codes are unique to each individual, the system guarantees accurate identification and prevents attendance errors or proxies.

### 2. Streamlined Process:
- The automation eliminates manual attendance-taking, saving time and effort for both students/employees and teachers/managers.

### 3. Real-time Tracking:
- The system updates attendance records in real-time, providing instant access to attendance information for monitoring and analysis.

### 4. User-Friendly:
- Using QR codes is straightforward for students and employees; they only need to show their QR code to the camera, and the rest is done automatically.
