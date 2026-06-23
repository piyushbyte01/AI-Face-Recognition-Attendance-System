import tkinter as tk
from tkinter import *
from database import get_students

def view_students():

    data = get_students()

    root = Tk()
    root.title("Registered Students")
    root.geometry("700x500")
    root.configure(background="black")

    headers = ["Enrollment", "Student Name"]

    for c, header in enumerate(headers):
        label = tk.Label(
            root,
            text=header,
            width=25,
            fg="yellow",
            bg="black",
            relief=RIDGE,
            font=("times", 15, "bold")
        )
        label.grid(row=0, column=c)

    for r, row_data in enumerate(data, start=1):
        for c, value in enumerate(row_data):
            label = tk.Label(
                root,
                text=str(value),
                width=25,
                fg="yellow",
                bg="black",
                relief=RIDGE,
                font=("times", 15)
            )
            label.grid(row=r, column=c)

    root.mainloop()