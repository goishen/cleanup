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

    def Begin_Scan(self):
        self.pict = ['.jpg', '.jpeg', '.gif', '.png']
        self.movies = ['.mp4', '.mkv', 'webm']
        self.music = ['.mp3', '.opus', '.ogg', '.m4a', '.wav']
        self.documents = ['.docx', '.pdf', '.txt']
        try:
            for i in self.files:
                if i.endswith( tuple(self.pict)):
                    self.Pictures(i)
                    pictures_label = ttk.Label(self, text="Moved pictures " + i)  
                    pictures_label.grid(row=2, column=0)
                elif i.endswith( tuple(self.movies)):
                    self.Videos(i)
                    mov_video = ttk.Label(self, text="Moved video " + i)
                    mov_video.grid(row=3, column=0)
                elif i.endswith( tuple(self.music)):
                    self.Music(i)
                    mov_aud = ttk.Label(self, text="Moved audio " + i)  
                    mov_aud.grid(row=4, column=0)
                elif i.endswith( tuple(self.documents)): 
                    self.Documents(i)
                    mov_doc = ttk.Label(self, text="Moved documents " + i)
                    mov_doc.grid(row=5, column=0)
                else:
                    if i != i.endswith( tuple(self.pict)) and i != i.endswith(tuple(self.movies)) \
                                        and i != i.endswith(tuple(self.music)) and i != i.endswith(tuple(self.documents)):
                        nothing_to_do = ttk.Label(self, text="Nothing to do!")
                        nothing_to_do.grid(row=7, column=0)
        except shutil.Error as e:
            horribly_awry = ttk.Label(self, text=e)
            horribly_awry.grid(row=8, column=0)        
    def Pictures(self, i):
        shutil.move(i, os.path.join(self.source, 'Pictures'))
    def Videos(self, i):
        shutil.move(i, os.path.join(self.source, 'Videos'))
    def Music(self, i):
        shutil.move(i, os.path.join(self.source, 'Music'))
    def Documents(self, i):
        shutil.move(i, os.path.join(self.source, 'Documents'))
        

root = Clean_Up()

font.nametofont("TkDefaultFont").configure(size=12)

root.mainloop()



