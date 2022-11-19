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

    #adding labels to the individual tabs
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu", 48))
        self.pomodoro_timer_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 48))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 48))
        self.long_break_timer_label.pack(pady=20)
    
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

    #creating start, skip and reset button under the time
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoro: 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False

        self.root.mainloop()


    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()

#define the start_timer fuunction
    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -=1

            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoro: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                self.start_timer

        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -=1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -=1

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()


    def reset_clock(self):
        pass

    def skip_clock(self):
        pass


#call to check if it works
PomodoroTimer()