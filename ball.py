#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox

import sys
import os
import pygame 
import pygame.midi
from pygame.locals import *
from socket import *
import struct
import time

import texteditbox


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
        self.create_Widgets()

    def set_IP(self, ip):
        self.ip = ip

    def change_virtual_color(self, color):
        self.canvas.delete("all")
        self.canvas.pack(padx=15, anchor = 'w')
        self.canvas.create_oval(0, 0, ball_size, ball_size, fill = color)

    def change_real_color(self, color):
        rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        #print('change color', color)
        data = struct.pack("!BBBB", 0x0a, rgb[0], rgb[1], rgb[2])
        #print('the self ip', self.ip)
        s.sendto(udp_header+data, ('192.168.43.'+self.ip, 41412));

    def update_color(self, timeline_markers, playtime):
        if timeline_markers:
            getNextLowest  = lambda seq,x: min([(x-i,i) for i in seq if x>=i] or [(0,None)])
            newLowest = getNextLowest(list(timeline_markers.keys()), playtime)
            if newLowest[1] != None:
                nextLowestColor = timeline_markers[newLowest[1]]
                self.change_virtual_color( nextLowestColor )
                self.change_real_color( nextLowestColor)
                self.currentColor = nextLowestColor

    # def update_rects(self):
    #     self.canvas.delete("all")
    #     previous_markers_right_value = 0
    #     for index, marker in enumerate(self.marker_data):        
    #         previous_markers_right_pixel = self.get_pixel_from_value(previous_markers_right_value)
    #         this_markers_right_pixel = previous_markers_right_pixel + self.get_pixel_from_value(marker[0])            
    #         self.canvas.create_rectangle(this_markers_right_pixel-previous_markers_right_pixel, 0, 1920, 30, fill=marker[1], outline = "")
    #         self.canvas.pack()
    #         previous_markers_right_value =+ marker[0]

#use ip to send color change to real balls


#e = Entry(root, textvariable=sv, validate="focusout", validatecommand=callback)


    def create_Widgets ( self ):
        def OnSpinBoxChange(event):
            self.ip=self.sv.get().strip()
            print('Text has changed ? ', self.ip)
            self.focus()
        def editbutton_clicked():
            print('editbutton_clicked')
            test = TextEditBox(self, "testing").show()
            #test.bind("<Destroy>",testtest())
            print('test.result444', test.result)
        TextEditBox = texteditbox.TextEditBox
        TextEditBox.root = self
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
