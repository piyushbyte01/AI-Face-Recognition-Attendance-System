import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font
from database import insert_attendance, get_student_name

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "TrainingImage"
attendance_path = "Attendance"
# for choose subject and fill attendance
def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()

        now = time.time()
        future = now + 20

        if sub == "":
            text_to_speech("Please enter the subject name!!!")
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()

            try:
                recognizer.read(trainimagelabel_path)
            except:
                Notifica.configure(
                    text="Model not found, please train model",
                    bg="black",
                    fg="yellow",
                    width=33,
                    font=("times", 15, "bold"),
                )
                Notifica.place(x=20, y=250)
                text_to_speech("Model not found, please train model")
                return

            facecasCade = cv2.CascadeClassifier(haarcasecade_path)

            cam = cv2.VideoCapture(0)

            if not cam.isOpened():
                text_to_speech("Camera not opening")
                return

            font = cv2.FONT_HERSHEY_SIMPLEX

            col_names = ["Enrollment", "Name"]
            attendance = pd.DataFrame(columns=col_names)

            Subject = sub

            while True:
                ret, im = cam.read()
                if not ret:
                    continue

                if im is None:
                    continue
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = facecasCade.detectMultiScale(gray, 1.2, 5)

                seen = set()

                for (x, y, w, h) in faces:

                    Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

                    if conf is not None and conf < 70:
                        aa = get_student_name(Id)

                        # Student not found in database
                        if aa is None:
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 4)
                            cv2.putText(im, "Unknown", (x, y - 10),
                                        font, 1, (0, 0, 255), 2)
                            continue

                        if Id not in seen:
                            seen.add(Id)
                            attendance.loc[len(attendance)] = [Id, aa]

                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 4)
                        cv2.putText(im, f"{Id}-{aa}", (x, y - 10),
                                    font, 1, (255, 255, 0), 2)

                    else:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 4)
                        cv2.putText(im, "Unknown", (x, y - 10),
                        font, 1, (0, 0, 255), 2)


                attendance = attendance.drop_duplicates(subset=["Enrollment"], keep="first")

                cv2.imshow("Filling Attendance...", im)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

                if time.time() > future:
                    break

            cam.release()
            cv2.destroyAllWindows()

            if attendance.empty:
                text_to_speech("No student recognized")
                return

            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")

            for index, row in attendance.iterrows():
                try:
                    insert_attendance(
                        str(row["Enrollment"]),
                        str(row["Name"]),
                        Subject,
                        date,
                        timeStamp
                    )
                except Exception as e:
                    print("DB ERROR:", e)

            Notifica.configure(
                text="Attendance Filled Successfully",
                bg="black",
                fg="yellow",
                width=33,
                relief=RIDGE,
                bd=5,
                font=("times", 15, "bold"),
            )
            Notifica.place(x=20, y=250)

            text_to_speech("Attendance completed successfully")

        except Exception as e:
            print("ERROR:", e)
            text_to_speech("Something went wrong")
            cv2.destroyAllWindows()

    ###windo is frame for subject chooser
    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="Enter the Subject Name",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)
    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Fill Attendance",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()
