from tkinter import *
import time
#Stop watch frame
root=Tk()
root.configure(background=("#FFFFFF"))
root.title('Python Project: Stopwatch')
root.geometry("980x720+220+0")

# labels for stopwatch
label1 = Label(root, text="HOURS", fg="black", bg="white", font=("Arial", 10, "bold"))
label1.place(x=280, y=30, width=50, height=30)
label2 = Label(root, text="MINUTES", fg="black", bg="white", font=("Arial", 10, "bold"))
label2.place(x=455, y=30, width=80, height=30)
label3 = Label(root, text="SECONDS", fg="black", bg="white", font=("Arial", 10, "bold"))
label3.place(x=647, y=30, width=80, height=30)
