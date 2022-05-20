from tkinter import *
import time
from time import strftime

#Stop watch frame
root=Tk()
root.configure(background=("#FFFFFF"))
root.title('Python Project: Stopwatch')
root.geometry("980x720+220+0")

#Function for Date & Time
def my_time():
    time_string = strftime('%H:%M:%S %p\n %A \n %x')
    l1.config(text=time_string)
    l1.after(1000,my_time)

my_font = ('Arial', 10, 'bold')
l1 = Label(root, font=my_font,bg='white')
l1.grid(row=1,column=1,padx=5,pady=25)
my_time()

# labels for stopwatch
label1 = Label(root, text="HOURS", fg="black", bg="white", font=("Arial", 10, "bold"))
label1.place(x=280, y=30, width=50, height=30)
label2 = Label(root, text="MINUTES", fg="black", bg="white", font=("Arial", 10, "bold"))
label2.place(x=455, y=30, width=80, height=30)
label3 = Label(root, text="SECONDS", fg="black", bg="white", font=("Arial", 10, "bold"))
label3.place(x=647, y=30, width=80, height=30)

#Global Variables
elapsed_time1=0
elapsed_time2=0
elapsed_time3=0
time1=0
time2=0
i=0
j=0

# Start Function
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
            elapsed_time2 += 1
            if elapsed_time2 < 59:
                elapsed_time2 += 1
                clock_frame.config(text=(str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)))
            else:
                elapsed_time2 = 0
                elapsed_time3 += 1
                if elapsed_time3 >= 24:
                    elapsed_time1 = 0
                    elapsed_time2 = 0
                    elapsed_time3 = 0
                else:
                    elapsed_time3 += 1
                    clock_frame.config(text=(str(elapsed_time3).zfill(2) + ":" + str(elapsed_time2).zfill(2) + ":" + str(elapsed_time1).zfill(2)))
    self_job = root.after(1000, start)

root.mainloop()
