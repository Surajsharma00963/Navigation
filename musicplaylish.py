import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Progressbar

from mutagen.mp3 import MP3
from pygame import mixer

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
slidetext = "Developed by Suraj & Swati  "
count = 0
text = ''


def msp():
    def createWidgets():
        s = ttk.Style(root)
        s.theme_use('clam')
        s.configure("black.Horizontal.TProgressbar", background=color['black'])
        TitleLabel = Label(root, bg=color['gray'], fg=color['yellow'], text="PlayLish Music Player",
                           font=('New Rocker', 25, 'bold'))
        TitleLabel.pack(side=TOP, pady=15)

        root.inputframe = Frame(root, bg=color['gray'])
        root.inputframe.pack(side=TOP)
        Tracklabel = Label(root.inputframe, bg=color['gray'], fg=color['yellow'], text="Select Track: ",
                           font=('New Rocker', 15, 'bold', 'italic',))
        Tracklabel.grid(row=0, column=0, padx=10, pady=10)

        root.audiostatuslabel = Label(root, bg=color['gray'], fg=color['yellow'],
                                      font=('New Rocker', 13, 'bold', 'italic',), height=2)
        root.audiostatuslabel.pack(side=TOP)

        Searchbtn = Button(root.inputframe, text="Browse Songs", bg=color['blue'], fg=color['offwhite'],
                           font=('New Rocker', 13, 'bold', 'italic'), width=12, bd=3, command=musicurl)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)

        root.TracklabelEntry = Label(root.inputframe, bg=color['offwhite'], fg=color['gray'],
                                     font=('New Rocker', 13, 'bold', 'italic'), width="50")
        root.TracklabelEntry.grid(row=0, column=1, columnspan=2, padx=10)

        root.musicprogressLabel = Label(root, bg=color['gray'])
        root.musicprogressLabel.pack(side=TOP, pady=20)

        root.musicprogressstarttimeLabel = Label(root.musicprogressLabel, bg=color['red'], text='0:00:0',
                                                 font=('New Rocker', 10, 'italic'), fg=color['offwhite'])
        root.musicprogressstarttimeLabel.grid(row=0, column=1, padx=5)
        root.musicprogressstarttimeLabel.grid_remove()

        root.musicprogressBar = Progressbar(root.musicprogressLabel, style='black.Horizontal.TProgressbar',
                                            orient=HORIZONTAL, mode='determinate', length=380)
        root.musicprogressBar.grid(row=0, column=2)
        root.musicprogressBar.grid_remove()

        root.musicprogressendtimeLabel = Label(root.musicprogressLabel, bg=color['red'], text='0:00:0',
                                               font=('New Rocker', 10, 'italic'), fg=color['offwhite'])
        root.musicprogressendtimeLabel.grid(row=0, column=3, padx=5)
        root.musicprogressendtimeLabel.grid_remove()

        controlFrame = Frame(root, bg=color['yellow'])
        controlFrame.pack(side=TOP)

        volup = Button(controlFrame, text="+", font=('New Rocker', 13, 'bold', 'italic'), width=5, bd=3,
                       bg=color['skyblue'], fg=color['white'], command=volumeup)
        volup.grid(row=4, column=2, columnspan=2, padx=20, pady=10)

        voldown = Button(controlFrame, text="-", font=('New Rocker', 13, 'bold', 'italic'), width=5, bd=3,
                         bg=color['skyblue'], fg=color['white'], command=volumedown)
        voldown.grid(row=4, column=0, columnspan=1, padx=20, pady=10)

        root.playbtn = Button(controlFrame, text="Play", font=('New Rocker', 13, 'bold', 'italic'), width=10, bd=3,
                              bg=color['green'], fg=color['white'], command=playmusic)
        root.playbtn.grid(row=2, column=1, columnspan=2, padx=20, pady=10)

        root.pausebtn = Button(controlFrame, text="Pause", font=('New Rocker', 13, 'bold', 'italic'), width=10, bd=3,
                               bg=color['red'], fg=color['white'], command=pausemusic)
        root.pausebtn.grid(row=1, column=1, columnspan=1, padx=20, pady=10)

        root.resumebtn = Button(controlFrame, text="Resume", font=('New Rocker', 13, 'bold', 'italic'), width=10, bd=3,
                                bg=color['skyblue'], command=resumemusic)
        root.resumebtn.grid(row=1, column=1, columnspan=1, padx=20, pady=10)
        root.resumebtn.grid_remove()

        stopbtn = Button(controlFrame, text="Stop", font=('New Rocker', 13, 'bold', 'italic'), width=10, bd=3,
                         bg=color['red'], fg=color['white'], command=stopmusic)
        stopbtn.grid(row=4, column=1, columnspan=2, padx=20, pady=10)

        prevbtn = Button(controlFrame, text="Previous", font=('New Rocker', 13, 'bold', 'italic'), bg=color['red'],
                         fg=color['white'], width=10, bd=3)
        prevbtn.grid(row=1, column=0, rowspan=4, padx=20, pady=10)

        nextbtn = Button(controlFrame, text="Next", font=('New Rocker', 13, 'bold', 'italic'), bg=color['red'],
                         fg=color['white'], width=10, bd=3)
        nextbtn.grid(row=1, column=3, rowspan=4, padx=20, pady=10)

        root.progressbarLabel = Label(controlFrame, text='', bg=color['red'])
        root.progressbarLabel.grid(row=5, column=0, columnspan=4, padx=20, pady=10)

        root.volprogrss = Progressbar(root.progressbarLabel, style='black.Horizontal.TProgressbar', orient=HORIZONTAL,
                                      mode='determinate', value=40, length=200)
        root.volprogrss.grid(column=0, row=0, padx=2, pady=2)

        root.volprogrsslabel = Label(root.progressbarLabel, text='40%')
        root.volprogrsslabel.grid(column=0, row=0, padx=2, pady=2)

        SlideFrame = Frame(root, bg=color['gray'])
        SlideFrame.pack(side=BOTTOM, pady=10)
        SlideLabel = Label(SlideFrame, text=slidetext, font=('New Rocker', 20, 'bold', 'italic'), bg=color['gray'],
                           fg=color['offwhite'])
        SlideLabel.grid()

        def Introlable():
            global count, text
            if count >= len(slidetext):
                count = -1
                text = ''
                SlideLabel.configure(text=text)
            else:
                text = text + slidetext[count]
                SlideLabel.configure(text=text)
            count += 1
            SlideLabel.after(200, Introlable)

        Introlable()

    def musicurl():
        try:
            Audio = filedialog.askopenfilename(initialdir='C:/Users/Suraj/Music',
                                               title="Select Audio Files",
                                               type=(('MP3', '*.mp3'), ('WAV', '*.wav')))
        except:
            Audio = filedialog.askopenfilename()
        trackname.set(Audio)
        root.TracklabelEntry.configure(text=Audio)

    def playmusic():
        ad = trackname.get()
        mixer.music.load(ad)
        mixer.music.play()
        mixer.music.set_volume(0.4)
        root.volprogrss['value'] = 40
        root.volprogrsslabel['text'] = '40%'
        root.audiostatuslabel.configure(text="Playing\n" + ad)

        song = MP3(ad)
        totallength = int(song.info.length)
        root.musicprogressBar['maximum'] = totallength
        root.musicprogressLabel.configure(bg=color['red'])
        root.musicprogressBar.grid()
        root.musicprogressendtimeLabel.grid()
        root.musicprogressstarttimeLabel.grid()
        root.musicprogressendtimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totallength))))

        def musictimetick():
            currentlength = mixer.music.get_pos() // 1000
            root.musicprogressBar['value'] = currentlength
            root.musicprogressstarttimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentlength))))
            root.musicprogressBar.after(2, musictimetick)

        musictimetick()

    def pausemusic():
        mixer.music.pause()
        ad = trackname.get()
        root.pausebtn.grid_remove()
        root.resumebtn.grid()
        root.audiostatuslabel.configure(text="Paused\n" + ad)

    def resumemusic():
        mixer.music.unpause()
        ad = trackname.get()
        root.resumebtn.grid_remove()
        root.pausebtn.grid()
        root.audiostatuslabel.configure(text="Playing\n" + ad)

    def volumeup():
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol + 0.05)
        root.volprogrsslabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
        root.volprogrss['value'] = mixer.music.get_volume() * 100

    def volumedown():
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol - 0.05)
        root.volprogrsslabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
        root.volprogrss['value'] = mixer.music.get_volume() * 100

    def stopmusic():
        mixer.music.stop()
        root.musicprogressBar.grid_remove()
        root.musicprogressendtimeLabel.grid_remove()
        root.musicprogressstarttimeLabel.grid_remove()
        root.musicprogressLabel.configure(bg=color['gray'])
        root.audiostatuslabel.configure(text="")
        root.TracklabelEntry.configure(text='')

    root = Tk()
    root.geometry('1000x550')
    root.title("Playlish Music Player")
    root.resizable(False, False)
    root.configure(bg=color['gray'])
    trackname = StringVar()
    mixer.init()
    mixer.music.set_volume(40)
    createWidgets()
    root.mainloop()
