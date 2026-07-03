# AI Face Recognition Attendance System

A Face Recognition based Attendance Management System developed using **Python, OpenCV, Tkinter, and MySQL**. The system automatically recognizes registered students through facial recognition and records attendance in a MySQL database.

## Features

* Face Registration using Webcam
* Face Recognition Based Attendance
* MySQL Database Integration
* Student Management System
* View Registered Students
* View Attendance Records
* Subject-wise Attendance Tracking
* Duplicate Enrollment Prevention
* User-Friendly GUI using Tkinter
* Text-to-Speech Notifications

---

## Technologies Used

* Python 3.x
* OpenCV
* Tkinter
* NumPy
* Pandas
* Pillow (PIL)
* MySQL
* pyttsx3

---

## Project Structure

AI-Face--Recognition-Attendance-System/
│
├── TrainingImage/
├── TrainingImageLabel/
├── UI_Image/
│
├── automaticAttedance.py
├── attendance.py
├── database.py
├── show_attendance.py
├── takeImage.py
├── trainImage.py
├── view_students.py
│
├── haarcascade_frontalface_alt.xml
├── haarcascade_frontalface_default.xml
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Database Setup

### Create Database

```sql
CREATE DATABASE attendance_system;
```

### Use Database

```sql
USE attendance_system;
```

### Create Students Table

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment VARCHAR(50) UNIQUE,
    name VARCHAR(100)
);
```

### Create Attendance Table

```sql
CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment VARCHAR(50),
    name VARCHAR(100),
    subject VARCHAR(100),
    date DATE,
    time_stamp TIME
);
```

---

## Installation

### Clone Repository

```bash
git clone <https://github.com/piyushbyte01/AI-Face-Recognition-Attendance-System.git>
```

### Move to Project Directory

```bash
cd Attendance-Management-System
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Configure Database

Open `database.py` and update the database credentials according to your MySQL configuration:

```python
host=""
user=""
password="You Password"
database="attendance_system"
```

---

## How to Run

Run the following command:

```bash
python attendance.py
```

---

## Project Workflow

### 1. Register Student

* Click **Register New Student**
* Enter Enrollment Number and Name
* Click **Take Image**
* The system captures multiple facial images
* Images are stored in the `TrainingImage` folder

### 2. Train Images

* Click **Train Image**
* The system trains the face recognition model
* Trained model is stored in `TrainingImageLabel/Trainner.yml`

### 3. Take Attendance

* Click **Take Attendance**
* Enter Subject Name
* Camera starts automatically
* Registered faces are recognized
* Attendance is stored in the MySQL database

### 4. View Attendance

* Click **View Attendance**
* Select a subject
* Attendance records are displayed in tabular format

### 5. View Students

* Click **View Students**
* Displays all registered students from the database

---

## Security Features

* Duplicate Enrollment Prevention
* Unknown Face Detection
* Database-Based Student Verification
* Subject-wise Attendance Storage

---

## Future Enhancements

* Admin Login System
* Attendance Percentage Calculation
* Excel/PDF Report Export
* Email Notifications
* Cloud Database Integration
* Anti-Spoofing Face Verification

---

## Author

**Piyush Kumar Sahu**

B.Tech CSE(AI & ML)

AI Face Recognition Attendance System using Python, OpenCV, Tkinter, and MySQL.
