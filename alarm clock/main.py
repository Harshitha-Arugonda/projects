#replit is not supporting this project,pygame is not working
#It is working in terminal
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pytz import timezone
import pygame

# Initializing our audio mixer and setting the wav alarm file we want it to play when the alarm goes off
pygame.mixer.init(42050, -16, 2, 2048)
alarm_sound = pygame.mixer.Sound("ALARM_CLOCK_MyAlarm.wav")
# Setting our initial global values
done = False
stop_clicked = False

class AlarmApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Alarm Clock")
        self.resizable(width=False, height=False)
        self.hr = tk.StringVar(self)
        self.min = tk.StringVar(self)
        self.ampm = tk.StringVar(self)
        self.hr.set('12')
        self.min.set("00")
        self.ampm.set("AM")
        hours = [str(i).zfill(2) for i in range(1, 13)]
        minutes = [str(i).zfill(2) for i in range(60)]
        ampmlist = ["AM", "PM"]
        self.popmenuhours = ttk.Combobox(self, textvariable=self.hr, values=hours, state="readonly")
        self.popmenuminutes = ttk.Combobox(self, textvariable=self.min, values=minutes, state="readonly")
        self.popmenuAMPM = ttk.Combobox(self, textvariable=self.ampm, values=ampmlist, state="readonly")
        self.popmenuhours.pack(side="left")
        self.thing = tk.Label(text=":").pack(side="left")
        self.popmenuminutes.pack(side="left")
        self.popmenuAMPM.pack(side="left")
        self.alarmbutton = tk.Button(self, text="Set Alarm", command=self.start_clock)
        self.cancelbutton = tk.Button(self, text="Cancel Alarm", command=self.stop_clock, state="disabled")
        self.stopalarmbutton = tk.Button(self, text="Stop Alarm", command=self.stop_audio, state="disabled")
        self.alarmbutton.pack()
        self.cancelbutton.pack()
        self.stopalarmbutton.pack()

    def start_clock(self):
        global done, stop_clicked
        if not done:
            self.cancelbutton.config(state="active")
            self.alarmbutton.config(state="disabled")
            hour_value = self.hr.get()
            if self.ampm.get() == "AM" and self.hr.get() == '12':
                hour_value = '00'
            elif self.ampm.get() == "PM" and self.hr.get() != '12':
                hour_value = str(int(self.hr.get()) + 12)
            self.Alarm(hour_value, self.min.get())
        if stop_clicked:
            done = False
            stop_clicked = False

    def stop_clock(self):
        global done, stop_clicked
        print("Alarm set for {}:{}{} has been canceled".format(self.hr.get(), self.min.get(), self.ampm.get()))
        stop_clicked = True
        done = True
        self.cancelbutton.config(state="disabled")
        self.alarmbutton.config(state="active")

    def stop_audio(self):
        pygame.mixer.Sound.stop(alarm_sound)
        self.stopalarmbutton.config(state="disabled")
        self.alarmbutton.config(state="active")

    def Alarm(self, myhour, myminute):
        global done
        if not done:
            myhour, myminute = str(myhour), str(myminute)
            a = str(datetime.now(timezone("Asia/Kolkata")))
            b = a.split(" ")[1].split(":")
            hour = b[0]
            minute = b[1]
            if hour == myhour and minute == myminute:
                pygame.mixer.Sound.play(alarm_sound, loops=-1)
                print("Alarm is ringing!")
                done = True
                self.cancelbutton.config(state="disabled")
                self.stopalarmbutton.config(state="active")
            else:
                self.after(1000, self.start_clock)
            done = False

app = AlarmApp()
app.mainloop()
