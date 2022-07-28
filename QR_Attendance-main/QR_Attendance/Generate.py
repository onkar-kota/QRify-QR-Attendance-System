from MyQR import myqr
import os

f = open('D:/Coding Files/Coding Ninja/5. Projects/2. QR_Attendance/QR_Attendance-main/QR_Attendance/students.txt','r')
lines = f.read().split("\n")
print(lines)

for _ in range (0,len(lines)):
    data = lines[_]
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="D:/Coding Files/Coding Ninja/5. Projects/2. QR_Attendance/QR_Attendance-main/QR_Attendance/Bg.png",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.png'),
        save_dir=os.getcwd()
    )