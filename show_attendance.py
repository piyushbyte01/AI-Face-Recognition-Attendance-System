from database import get_attendance
import tkinter
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get().strip()
        if Subject == "":
            text_to_speech("Please enter the subject name.")
            return

        data = get_attendance(str(Subject).strip())

        if len(data) == 0:
            text_to_speech("No attendance found for this subject")
            return

        root = tkinter.Tk()
        root.title("Attendance of " + Subject)
        root.configure(background="black")

        headers = [
            "Enrollment",
            "Student Name",
            "Date",
            "Time"
        ]

        for c, header in enumerate(headers):
            label = tkinter.Label(
                root,
                text=header,
                width=20,
                height=1,
                fg="yellow",
                bg="black",
                relief=tkinter.RIDGE,
                font=("times", 15, "bold"),
            )
            label.grid(row=0, column=c)

        for r, row_data in enumerate(data, start=1):
            for c, value in enumerate(row_data):
                label = tkinter.Label(
                    root,
                    text=str(value),
                    width=20,
                    height=1,
                    fg="yellow",
                    bg="black",
                    relief=tkinter.RIDGE,
                    font=("times", 15),
                )
                label.grid(row=r, column=c)

        root.mainloop()

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
        text="Which Subject of Attendance?",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)
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
        text="View Attendance",
        command=calculate_attendance,
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
