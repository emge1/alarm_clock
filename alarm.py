import tkinter
import os
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import ttk
import time
from threading import *
from pygame import mixer

root = Tk()

mixer.init()

"""  'FRONTEND'  """
root.geometry('250x350')
root.title('Alarm clock')
root['bg'] = '#252729'

page_font_big = ("Arial", 40)
page_font_mid = ("Arial", 20)
page_font_smol = ("Arial", 8)

front = {"bg": "#252729",
        "fg": "#ffffff",
        "borderwidth": 1,
        "highlightthickness": 0,
        "width": 15,
        "font": "Arial 28 bold",
        "justify": "right"
        }

# Combobox style
style = ttk.Style()

root.option_add('*TCombobox*Listbox*Background', '#252729')
root.option_add('*TCombobox*Listbox*Foreground', "#ffffff")
root.option_add('*TCombobox*Listbox*selectBackground', "#ffffff")
root.option_add('*TCombobox*Listbox*selectForeground', '#252729')

style.map('TCombobox', fieldbackground=[('readonly', '#252729')])
style.map('TCombobox', selectbackground=[('readonly', '#252729')])
style.map('TCombobox', selectforeground=[('readonly', "#ffffff")])
style.map('TCombobox', background=[('readonly', '#252729')])
style.map('TCombobox', foreground=[('readonly', "#ffffff")])


''' FUNCTIONS '''
def time1():
    hour_string = strftime('%H:%M:%S')
    date_string = strftime('%A, %d.%m.%y')

    hour_label.config(text=hour_string)
    hour_label.after(1000, time1)

    date_label.config(text=date_string)
    date_label.after(1000, time1)

def main_to_settings():
    hour_label.pack_forget()
    date_label.pack_forget()
    main_to_settings_button.pack_forget()

    set_time_label.pack()
    hour_frame.pack()
    hrs.pack(side=LEFT)
    mins.pack(side=LEFT)
    snooze_label.pack()
    snooze_frame.pack()
    snooz.pack(side=LEFT)
    ring_label.pack()
    ring_frame.pack()
    rin.pack(side=LEFT)
    settings_to_main_button.pack(side='bottom')

def settings_to_main():
    set_time_label.pack_forget()
    hour_frame.pack_forget()
    hrs.pack_forget()
    mins.pack_forget()
    snooze_label.pack_forget()
    snooze_frame.pack_forget()
    snooz.pack_forget()
    ring_label.pack_forget()
    ring_frame.pack_forget()
    rin.pack_forget()
    settings_to_main_button.pack_forget()

    hour_label.pack(side='top')
    date_label.pack(side='top')
    main_to_settings_button.pack(side='bottom')

    Threading_not_snooze()

def main_to_alarm():
    activate_snooze_button.pack()
    alarm_to_main_button.pack(side='bottom')

def alarm_to_main():
    activate_snooze_button.pack_forget()
    alarm_to_main_button.pack_forget()

def snooze_alarm_to_main():
    activate_snooze_button.pack_forget()
    alarm_to_main_button.pack_forget()
    Threading_snooze()


'''Main page widgets'''
hour_label = Label(root, cnf=front, font=page_font_big)
hour_label.pack(side='top')

date_label = Label(root, cnf=front, font=page_font_mid)
date_label.pack(side='top')

time1()

'''Settings page widgets'''
def Threading_not_snooze():
    t1 = Thread(target=alarm)
    t1.start()

def Threading_snooze():
    t1=Thread(target=alarm(True))
    t1.start()

is_snooze = False

def alarm(is_snooze):
    start_snooze = datetime.now()
    while True:
        # setting alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:00"
        if is_snooze == True:
            snooze_get = int(snooze.get())
            snooze_hour = start_snooze.hour
            if start_snooze.minute + int(snooze.get()) >= 60:
                snooze_get -= 60
                snooze_hour += 1
            set_alarm_time = (f"{snooze_hour}:{start_snooze.minute + snooze_get}:{start_snooze.second}")
            if len(set_alarm_time) == 7:
                set_alarm_time = (f"{snooze_hour}:0{start_snooze.minute + snooze_get}:{start_snooze.second}")

        time.sleep(2)
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            # playing sound
            main_to_alarm()
            print("alarm")
            sound = mixer.Sound(ring.get())
            mixer.music.load(sound)
            mixer.music.play(sound)
            print("end of alarm")


#  alarm time
set_time_label = Label(root, cnf=front, text="Set time", font=page_font_mid)

hour_frame = Frame(root)
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
         '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = ttk.Combobox(hour_frame, textvariable=hour, values=hours, width=10)

minute = StringVar(root)
minutes = ('00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60')
minute.set(minutes[0])
mins = ttk.Combobox(hour_frame, textvariable=minute, values=minutes, width=10)

# snooze
snooze_label = Label(root, cnf=front, text="Set snooze",font=page_font_mid)
snooze_frame = Frame(root)

snooze = StringVar(root)
snoozes = ('00', '05', '10', '15', '20', '25', '30')
snooze.set(drzemki[0])
snooz = ttk.Combobox(snooze_frame, textvariable=snooze, values=drzemki)

# ringtone
ring_label = Label(root, cnf=front, text="jaki dzwonek",font=page_font_mid)
ring_frame = Frame(root)
ring = StringVar(root)

folder = 'rings_files'
rings = [fname for fname in os.listdir(folder) if fname.endswith('.wav')]
ring.set(rings[0])
rin = ttk.Combobox(ring_frame, textvariable=ring, values=rings)


'''BUTTONS'''
main_to_settings_button = tkinter.Button(root, cnf=front, text='ustawienia', command=lambda: main_to_settings(),
        font=page_font_mid)
main_to_settings_button.pack(side='bottom')


settings_to_main_button = tkinter.Button(root, cnf=front, text='powrót', command=lambda: settings_to_main(),
        font=page_font_mid)

activate_snooze_button = tkinter.Button(root, cnf=front, text='OK', command=lambda: snooze_alarm_to_main(),
        font=page_font_big)

alarm_to_main_button = tkinter.Button(root, cnf=front, text='Snooze', command=lambda: alarm_to_main(),
        font=page_font_mid)


root.mainloop()
