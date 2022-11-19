#Create a pomodoro timer using python https://www.youtube.com/watch?v=FJeXp5yZd-g .
#It is a timer that is used to help the person for a better time management while working.
#This basically gives 25 minutes to work and 5 minutes break that will run 4 times then proceed to a long 15-minute break

#import libraries
import time
import threading
import tkinter as tk
from tkinter import ttk

#create a class for Pomodoro Timer:
class PomodoroTimer:
    #define a function to show the window for the pomodoro timer
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")

    #customize the content
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

    #creating tabs for the timer
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
    
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.root.mainloop()
     


#call to check if it works
PomodoroTimer()