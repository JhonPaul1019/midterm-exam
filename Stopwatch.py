from tkinter import *
import time
from time import strftime
import calendar

#Stop watch frame
root=Tk()
root.configure(background=("#FFFFFF"))
root.title('Python Project: Stopwatch')
root.geometry("980x720+250+0")
root.resizable(False,True)

#Labels For Stopwatch
label1 = Label(root, text="HOURS", fg="black", bg="white", font=("Arial", 10, "bold"))
label1.place(x=280, y=30, width=50, height=30)
label2 = Label(root, text="MINUTES", fg="black", bg="white", font=("Arial", 10, "bold"))
label2.place(x=455, y=30, width=80, height=30)
label3 = Label(root, text="SECONDS", fg="black", bg="white", font=("Arial", 10, "bold"))
label3.place(x=647, y=30, width=80, height=30)

#Function for Date & Time
def my_time():
    time_string = strftime('%H:%M:%S %p\n %A \n %x')
    l1.config(text=time_string)
    l1.after(1000,my_time)

my_font = ('Arial', 10, 'bold')
l1 = Label(root, font=my_font,bg='white')
l1.grid(row=1,column=1,padx=5,pady=25)
my_time()

#Global Variables
elapsed_time1=0
elapsed_time2=0
elapsed_time3=0
time1=0
time2=0
i=0
j=0

#Functions
def create_label(text,_x,_y):
    label = Label(root,text=text, fg="black", bg="white", font=("Arial", 10, "bold"))
    label.place(x=_x,y=_y, width=50, height= 30)

#Start Function
def start(): 
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=20, y=300, width=300, height=100)
    global elapsed_time1, elapsed_time2, elapsed_time3, time1, self_job, time2
    time2 = int(time.time())
    if time2 != time1:
        time1 = time2
        if elapsed_time1 < 59:
            elapsed_time1 += 1
            clock_frame.config(text=(str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)))
        else:
            elapsed_time1 = 0
            elapsed_time2 += 0
            if elapsed_time2 < 59:
                elapsed_time2 += 1
                clock_frame.config(text=(str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)))
            else:
                elapsed_time2 = 0
                elapsed_time3 += 0
                if elapsed_time3 >= 24:
                    elapsed_time1 = 0
                    elapsed_time2 = 0
                    elapsed_time3 = 0
                else:
                    elapsed_time3 += 1
                    clock_frame.config(text=(str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)))
    self_job = root.after(1000, start)

#Stop Function
def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job = None
    stop_button.place_forget()
    resume_button.place(x=20, y=300, width=300, height=100)

#Reset Function
def reset():
    global elapsed_time1, elapsed_time2, elapsed_time3, time1, self_job, time2, i, j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="00:00:00")
    elapsed_time1 = 0
    elapsed_time2 = 0
    elapsed_time3 = 0
    time1 = 0
    time2 = 0
    i = 0
    j = 0

#Function to Retain Widgets After Reset    
    wig = root.winfo_children()
    for b in wig:
        b.place_forget()
    resume_button.place_forget()
    start_button.place(x=20, y=300, width=300, height=100)
    lap_button.place(x=660, y=300, width= 300, height=100)
    reset_button.place(x=340, y=300, width=300, height=100)
    clock_frame.place(x=200, y=50, width=600, height=200)
    label1 = Label(root,text="HOURS", fg="black", bg="white", font=("Arial", 10, "bold"))
    label1.place(x=280,y=30, width=50, height= 30)
    label2 = Label(root,text="MINUTES", fg="black", bg="white", font=("Arial", 10, "bold"))
    label2.place(x=455,y=30, width=80, height= 30)
    label3 = Label(root,text="SECONDS", fg="black", bg="white", font=("Arial", 10, "bold"))
    label3.place(x=647,y=30, width=80, height= 30)
    
    #Calendar Function
    def createWidgets():
        popupwindow1 = Toplevel(root)
        popupwindow1.title("Calendar Year Input")
        popupwindow1.geometry("300x100+590+300")
        popupwindow1.resizable(False, False)
        label1_1 = Label(popupwindow1, text="Enter the Year in XXXX Format - ")
        label1_1.grid(row=0, column=0, padx=5, pady=5)
        global entry1
        entry1 = Entry(popupwindow1, width=15)
        entry1.grid(row=0, column=1)

        but = Button(popupwindow1, text="Submit", width=10, command=submit)
        but.grid(row=2, column=1)
        
def submit():
    global entry1
    Alarmtime = entry1.get()
    text = calendar.calendar(int(Alarmtime))
    popupwindow = Toplevel(root)
    popupwindow.title("Calendar")
    popupwindow.geometry("620x650+430+20")
    popupwindow.resizable(False, False)
    label_1 = Label(popupwindow, text="CALENDAR", bg="white", fg="black", font=("Times", 28, "bold"))
    label_1.grid(row=1,column=1)
    popupwindow.config(background="white")
    l_1=Label(popupwindow, text=text, font=('Courier', 10, 'bold'), justify=LEFT, bg='white')
    l_1.grid(row=2, column=1, padx=20)
    popupwindow.mainloop()

#Button for Calendar
button = Button(root, text="Calendar", fg="black", command=createWidgets, font=("Arial", 8, "bold"))
button.place(x=12,y=60, width=60, height= 30)

#Lap Function
def lap():
    global elapsed_time1, elapsed_time2, elapsed_time3, time1, self_job, time2, i, j
    if i < 9:
        create_label((str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)), 20 + (110*i), 400+(j*50))
    else:
        j += 1
        i = 0
        create_label((str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)), 20 + (110*i), 400+(j*50))
    i += 1

#Calendar Function
def createWidgets():
    popupwindow1 = Toplevel(root)
    popupwindow1.title("Calendar Year Input")
    popupwindow1.geometry("300x100+590+300")
    popupwindow1.resizable(False, False)
    label1_1 = Label(popupwindow1, text="Enter the Year in XXXX Format - ")
    label1_1.grid(row=0, column=0, padx=5, pady=5)
    global entry1
    entry1 = Entry(popupwindow1, width=15)
    entry1.grid(row=0, column=1)

    but = Button(popupwindow1, text="Submit", width=10, command=submit)
    but.grid(row=2, column=1)
    
def submit():
    global entry1
    Alarmtime = entry1.get()
    text = calendar.calendar(int(Alarmtime))
    popupwindow = Toplevel(root)
    popupwindow.title("Calendar")
    popupwindow.geometry("620x650+430+20")
    popupwindow.resizable(False, False)
    label_1 = Label(popupwindow, text="CALENDAR", bg="white", fg="black", font=("Times", 28, "bold"))
    label_1.grid(row=1,column=1)
    popupwindow.config(background="white")
    l_1=Label(popupwindow, text=text, font=('Courier', 10, 'bold'), justify=LEFT, bg='white')
    l_1.grid(row=2, column=1, padx=20)
    popupwindow.mainloop()

#Button for Calendar
button = Button(root, text="Calendar", fg="black", command=createWidgets, font=("Arial", 8, "bold"))
button.place(x=12,y=60, width=60, height= 30)
    
#Stopwatch Frame
clock_frame = Label(text="00:00:00", bg="white", fg="black", font=("Arial", 100, "bold"))
start_button = Button(text="Start", bg="green", fg="black", command=start, font=("Arial", 50, "bold"))
stop_button = Button(text="Stop", bg="red", fg="black", command=stop, font=("Arial", 50, "bold"))
resume_button = Button(text="Resume", bg="green", fg="black", command=start, font=("Arial", 50, "bold"))
lap_button = Button(text="Lap", bg="yellow", fg="black", command=lap, font=("Arial", 50, "bold"))
reset_button = Button(text="Reset", bg="orange", fg="black", command=reset, font=("Arial", 50, "bold"))

#Buttons Placement
start_button.place(x=20,y=300, width=300, height=100)
lap_button.place(x=660 ,y=300, width=300, height=100)
reset_button.place(x=340 ,y=300, width=300, height=100)
clock_frame.place(x=200 ,y=50, width=600, height=200)

root.mainloop()
