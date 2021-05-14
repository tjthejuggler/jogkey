#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox
import json
import sys
import os
import pygame 
import pygame.midi
from pygame.locals import *
from socket import *
import struct
import time
import painteditor

udp_header = struct.pack("!bIBH", 66, 0, 0, 0)
s = socket(AF_INET, SOCK_DGRAM)
ball_size = 120

class Ball( tk.Frame ):

    def __init__(self, master, *args, **kwargs):

        super().__init__(master)
        self.pack()
        self.master = master
        self.track_length = None
        self.canvas = None
        self.virtual_ball = None
        self.currentColor = "Black"
        self.ip = None
        self.entry = None
        self.sv = None
        self.timeline_markers = None
        self.create_Widgets()

    def set_IP(self, ip):
        self.ip = ip

    def change_virtual_color(self, color):
        self.canvas.delete("all")
        self.canvas.pack(padx=15, anchor = 'w')
        self.canvas.create_oval(0, 0, ball_size, ball_size, fill = color)

    def change_real_color(self, color):
        rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        data = struct.pack("!BBBB", 0x0a, rgb[0], rgb[1], rgb[2])
        s.sendto(udp_header+data, ('192.168.43.'+self.ip, 41412));

    def set_timeline_markers(self, timeline_markers):
        self.timeline_markers = timeline_markers

    def update_color(self, timeline_markers, playtime):
        if timeline_markers:
            getNextLowest  = lambda seq,x: min([(float(x)-float(i),i) for i in seq if float(x)>=float(i)] or [(0,None)])
            if isinstance(timeline_markers, str):
                timeline_markers = json.loads(timeline_markers)
            newLowest = getNextLowest(list(timeline_markers.keys()), playtime)
            if newLowest[1] != None:
                nextLowestColor = timeline_markers[newLowest[1]]
                self.change_virtual_color( nextLowestColor )
                self.change_real_color( nextLowestColor)
                self.currentColor = nextLowestColor

    def get_dict_from_text(text):
        local_dict_file = first_lang+'_'+second_lang+'.json'
        dest_text = ''
        if path.exists(cwd+'/local_dictionaries/'+local_dict_file):         
            with open(cwd+'/local_dictionaries/'+local_dict_file) as json_file:
                local_dict = json.load(json_file)
        return dest_text

    def create_Widgets ( self ):

        def OnSpinBoxChange(event):
            self.ip=self.sv.get().strip()
            print('Text has changed ? ', self.ip)
            self.focus()

        def editbutton_clicked():
            print('editbutton_clicked')
            print('self.timeline_markers', self.timeline_markers)
            results = json.dumps(self.timeline_markers)
            print('results',results)
            test = PaintEditor(results).show()
            self.timeline_markers = test.result
            print('test.result444', test.result)

        PaintEditor = painteditor.PaintEditor
        PaintEditor.root = self
        self.sv = tk.StringVar()
        print( '\ndef create_Widgets ( self ):' )
        self.canvas = tk.Canvas(self, width=ball_size, height=ball_size)
        self.canvas.pack(padx=15, anchor = 'w')
        self.canvas.create_oval(0, 0, ball_size, ball_size, fill = "black")
        self.spinbox = tk.Spinbox(self.canvas, from_= 0, to = 120, textvariable=self.sv, validate="focusout" )
        self.spinbox.bind("<KeyRelease>", OnSpinBoxChange)
        self.spinbox.place(x = 25, y = 30, width = 50)  
        self.editbutton = tk.Button(self.canvas, text='edit', command=editbutton_clicked)
        self.editbutton.place(x=25, y=60, width = 50)
