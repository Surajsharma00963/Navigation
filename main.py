import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from pong import pong
from time import strftime

from musicplaylish import msp

color = {
    "lightskyblue": "#5AA2E1",
    "green": "#85B314",
    "red": "#CE1515",
    "skyblue": "#4E99DB",
    "black": "#000000",
    "white": "#FFFFFF",
    "blue": "#0000ff",
    "gray": "#3e403f",
    "yellow": "#88cc00",
    "redOrange": "#4d1f00",
    "offwhite": "#f8f8ff"
}

root = tk.Tk()
root.title("Play Mania")
root.config(bg=color["gray"])
root.geometry("1336x768")
btnview = False

def hang():
    import hangman



navIcon = PhotoImage(file="images/menu.png")
NI = navIcon.subsample(100, 100)
navClose = PhotoImage(file="images/close.png")
NC = navClose.subsample(80, 80)
logo = PhotoImage(file="images/logo.png", height="600")

topBar = tk.Frame(root, bg=color["yellow"])
topBar.pack(side=TOP, fill=tk.X)

homeLabel = tk.Label(topBar, text="Playlish Mania", font=('New Rocker', 35, 'bold'), bg=color["yellow"],
                     fg=color["redOrange"], height=2, padx=20)
homeLabel.pack(side=RIGHT, )

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(topBar, font=('New Rocker', 20), background=color["yellow"], foreground="black")
label.pack(side=RIGHT)
time()

frame = tk.Frame(root, width="800", bg=color["gray"])
framelabel = tk.Label(frame, text="WELCOME TO PLAYLISH MANIA", fg=color["yellow"], bg=color["gray"], height="1",
                      font=('New Rocker', 35, 'bold'), pady=20)
framelabel.pack()
frame.pack(side=TOP)

brandFrame = tk.Canvas(root, bg=color["gray"], bd=0, height="350", width="350")
brandFrame.pack(side=TOP)
brandFrame.create_image(0, 0, anchor=NW, image=logo)
navBar = tk.Button(topBar, image=NI, bg=color["yellow"], activebackground=color["yellow"], bd=0, padx=20, command=None)
navBar.place(x=10, y=35)

appFrame = tk.Frame(root, bg=color["redOrange"])
appFrame.pack(side=TOP, pady=30)

appbutton1 = tk.Button(appFrame, bg=color["yellow"], text="Playlish\nPingPong", width=30, height=5,
                       font=('New Rocker', 12, 'bold'), command=pong)
appbutton1.grid(row=0, column=0, padx=10, pady=10)

appbutton2 = tk.Button(appFrame, bg=color["yellow"], text="Playlish\nMusic", width=30, height=5,
                       font=('New Rocker', 12, 'bold'), command=msp)
appbutton2.grid(row=0, column=1, padx=10, pady=10)

appbutton3 = tk.Button(appFrame, text="Playlish\nHangMan", bg=color["yellow"], font=('New Rocker', 12, 'bold'),
                       width=30, height=5, command=hang)
appbutton3.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()
