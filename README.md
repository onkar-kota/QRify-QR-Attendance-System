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

### Breakdown of the code [Code](https://github.com/onkar-kota/QRify/blob/main/QR_Attendance-main/QR_Attendance/Generate.py)

```
from MyQR import myqr
import os

```





# Benefits of the QR Attendance System:

### 1. Accuracy and Efficiency:
- Since QR codes are unique to each individual, the system guarantees accurate identification and prevents attendance errors or proxies.

### 2. Streamlined Process:
- The automation eliminates manual attendance-taking, saving time and effort for both students/employees and teachers/managers.

### 3. Real-time Tracking:
- The system updates attendance records in real-time, providing instant access to attendance information for monitoring and analysis.

### 4. User-Friendly:
- Using QR codes is straightforward for students and employees; they only need to show their QR code to the camera, and the rest is done automatically.
