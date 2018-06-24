#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
import shutil
import tkinter.messagebox
import statics
import queue
from multiprocessing import Process
import threading
from time import sleep

listofsongs = []
realnames = []
directory=""
ret=0
procs=[]

class Application(Frame, object):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.q = queue.Queue(10)
        self.root = Tk()
        self.root.wm_title("MUSIC PLAYER")
        self.root.minsize(500, 500)
        self.v = StringVar()
        self.songlabel = Label(self.root, textvariable=self.v, width=80)
        self.index = 0
        self.count = 0
        self.ctr=0
        self.emotionstatus = ""
        self.label = Label(self.root, text="Music Player")
        self.label.pack()
        self.listbox = Listbox(self.root, selectmode=MULTIPLE, width=100, height=20, bg="grey", fg="black")
        self.listbox.pack(fill=X)
        self.vol = Scale(self.root, from_=10, to=0, orient=VERTICAL, resolution=10)#, command=self.show_value(self))
        self.vol.place(x=85, y=380)
        self.vol.set(10)
        self.framemiddle = Frame(self.root, width=250, height=30)
        self.framemiddle.pack()
        self.framedown = Frame(self.root, width=400, height=300)
        self.framedown.pack()
        self.openbutton = Button(self.framedown, text="open")
        self.openbutton.pack(side=LEFT)

    # mutebutton = Button(framedown,text=u"\U0001F507")
#        self.mutebutton = Button(self.framedown, text="Mute")
#        self.mutebutton.pack(side=LEFT)

        self.previousbutton = Button(self.framedown, text="◄◄")
        self.previousbutton.pack(side=LEFT)
        self.playbutton = Button(self.framedown, text="►")
        self.playbutton.pack(side=LEFT)
        self.stopbutton = Button(self.framedown, text="■")
        self.stopbutton.pack(side=LEFT)
        self.nextbutton = Button(self.framedown, text="►►")
        self.nextbutton.pack(side=LEFT)
        self.pausebutton = Button(self.framedown, text="►/║║")
        self.pausebutton.pack(side=LEFT)
#        self.mutebutton.bind("<Button-1>", self.mute)
        self.openbutton.bind("<Button-1>", self.call)
        self.playbutton.bind("<Button-1>", self.playsong)
        self.nextbutton.bind("<Button-1>", self.nextsong)
        self.previousbutton.bind("<Button-1>", self.previoussong)
        self.stopbutton.bind("<Button-1>", self.stopsong)
        self.pausebutton.bind("<Button-1>", self.pausesong)

        self.emotionchooser()
        self.directorychooser()
        self.ppack()
        self.updatelabel()

#        self.processIn()
#        self.root.mainloop()

    def updatelabel(self):
        global index
        global songname
        self.v.set(listofsongs[index])
        # return songname

    def pausesong(self,event): # 않되면 self,event 해보기,, 아니면 self만 해보기
        self.ctr += 1
        if (self.ctr % 2 != 0):
            pygame.mixer.music.pause()
        if (self.ctr % 2 == 0):
            pygame.mixer.music.unpause()


    def playsong(self,event):
        pygame.mixer.music.play()


    def nextsong(self,event):
        global index
        index += 1
        if (index < count):
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
        else:
            index = 0
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
        try:
            self.updatelabel()
        except NameError:
            print("")


    def previoussong(self,event):
        global index
        index -= 1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        try:
            self.updatelabel()
        except NameError:
            print("")

    def stopsong(self):
        pygame.mixer.music.stop()



#    def mute(self,event):
#        self.vol.set(0)

    def emotionchooser(self):
        global directory
        directory = "/Users/soo/Downloads/Music/data"
        return directory

    def directorychooser(self):
        global count
        global index
        print(directory)
        # directory = "/home/bj/emotion"
        if (directory):
            count = 0
            index = 0
            del listofsongs[:]
            del realnames[:]

            os.chdir(directory)

            for files in os.listdir(directory):
                try:
                    if files.endswith(".mp3"):
                        realdir = os.path.realpath(files)
                        audio = ID3(realdir)
                        realnames.append(audio['TIT2'].text[0])
                        listofsongs.append(files)
                except:
                    print(files + " is not a song")

            if listofsongs == []:
                okay = tkinter.messagebox.askretrycancel("No songs found", "no songs")
                if (okay == True):
                    directorychooser()

            else:
                self.listbox.delete(0, END)
                realnames.reverse()
                for items in realnames:
                    self.listbox.insert(0, items)
                for i in listofsongs:
                    count = count + 1
                pygame.mixer.init()
                pygame.mixer.music.load(listofsongs[1])

                pygame.mixer.music.play()
                try:
                    self.updatelabel()
                except NameError:
                    print("")
        else:
            return 1

    def call(self):
        if (True):
            try:
                k = directorychooser()
            except OSError:
                print("thank you")

    def ppack(self):
        realnames.reverse()
        self.songlabel.pack()

    def show_value(self):
        i = vol.get()
        pygame.mixer.music.set_volume(i)

#########################################################################################
root = Tk()
root.title('Music player')
root.minsize(400, 100)
r= Application(root)


class MultiTest:
    def __init__(self):
        self.queue = queue.Queue()

    def music(self):
        print("music")
        #r.root.mainloop()
        sleep(6)

    def mic(self):
        while True:
            print("mic")
            r.pausesong(1)
            sleep(6)

    def run(self):
        a = Process(self.music())
        print("-------")
        b = Process(self.mic())
        print("a start")
        a.start()
        print("b start22")
        b.start()

    def Multi(self):
        self.run()

if __name__=='__main__':
    pygame.init()
    test = MultiTest()
    test.Multi()