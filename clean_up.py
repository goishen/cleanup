#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:01:01 2020

@author: Chris Harris

To help you clean up your home directory

"""
import tkinter as tk
from tkinter import ttk
import os
import shutil
import tkinter.font as font


class Clean_Up(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Clean up your home folder")
        
        get_user = os.getlogin()
        
        self.files = os.listdir(os.path.join("/", 'home', get_user))
        self.source = os.path.join("/", 'home', get_user) 
        os.chdir(self.source)
        
        text_label = ttk.Label(self, text="A tool to help you keep your home folder clean")
        text_label.grid(row=0, column=0, sticky="E", padx=10, pady=(10,10))
        begin_scan_button = ttk.Button(self, text="Begin scan of your home directory", command=self.Begin_Scan)
        begin_scan_button.grid(row=1, column=0, sticky="EW", padx=10, pady=(10, 10))
        
        quit_button = ttk.Button(self, text="Quit", command=self.destroy)
        quit_button.grid(row=6, column=0, padx=10, pady=(10, 10))
        # text_label.columnconfigure(0, weight=1)
        # text_label.rowconfigure(0, weight=0)
    def Begin_Scan(self):
        self.pict = []
        self.movies = []
        self.music = []
        self.documents = []
        for i in self.files:
            if ".jpg" in i:
                self.pict.append(i)
                self.Pictures(i)
            elif ".jpeg" in i:
                self.pict.append(i)
                self.Pictures(i)
            elif ".png" in i:
                self.pict.append(i)
                self.Pictures(i)
            elif ".mp4" in i:
                self.movies.append(i) 
                self.Videos(i)
            elif ".mkv" in i:
                self.movies.append(i)
                self.Videos(i)
            elif ".opus" in i:
                self.music.append(i)
                self.Music(i)
            elif ".mp3" in i:
                self.music.append(i)
                self.Music(i)
            elif ".docx" in i:
                self.documents.append(i)
                self.Documents(i)
            elif ".pdf" in i:
                self.documents.append(i)
                self.Documents(i)
                
        # print(i, "Worked", self.pict)        
    def Pictures(self, i):
        pictures_label = ttk.Label(self, text="Moved pictures")
        pictures_label.grid(row=2, column=0)
#        pictures_entry = ttk.Entry(self, width=20, textvariable=self.pict) 
#        pictures_entry.grid(row=1, column=1)
        shutil.move(i, os.path.join(self.source, 'Pictures'))
#        print("Moved pictures")
        #return pict_have_moved
    def Videos(self, i):
        shutil.move(i, os.path.join(self.source, 'Videos'))
        mov_video = ttk.Label(self, text="Moved video")
        mov_video.grid(row=3, column=0)
      #  print("Moved video")
        #return
    def Music(self, i):
        shutil.move(i, os.path.join(self.source, 'Music'))
        mov_aud = ttk.Label(self, text="Moved audio")
        mov_aud.grid(row=4, column=0)
     #   print("Moved audio")
        #return
    def Documents(self, i):
        shutil.move(i, os.path.join(self.source, 'Documents'))
        mov_doc = ttk.Label(self, text="Moved documents")
        mov_doc.grid(row=5, column=0)
    #   print("Moved documents")
        

root = Clean_Up()

font.nametofont("TkDefaultFont").configure(size=12)

root.mainloop()



