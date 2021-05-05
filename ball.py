#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox

class Ball( tk.Frame ):

    def __init__(self, master, *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()
        self.master = master     # Tk window
        self.track_length = None
        self.canvas = None
        self.virtual_ball = None
        self.create_Widgets()

    # def get_total_marker_width(self):
    #     total_marker_width = 0
    #     if len(self.marker_data) > 0:
    #         for marker in self.marker_data :
    #             total_marker_width += marker[0]
    #     return total_marker_width

    # def get_pixel_from_value(self, value):
    #     print('value', value)
    #     print('self.screen_width', self.screen_width)
    #     print('self.track_length', self.track_length)
    #     pixel = ((value*self.screen_width)/self.track_length)
    #     print('pixel', pixel)
    #     return pixel

    def get_color_from_playtime(self, playtime, timeline_markers):
        for marker in timeline_markers:
            if marker[0] == playtime:
                return marker[1]

    def change_color(self, color):
        self.canvas.delete("all")
        self.canvas.pack(padx=15, anchor = 'w')
        self.canvas.create_oval(0, 0, 50, 50, fill = color)

    def update_color(self, timeline_markers, playtime):
        #print('timeline_markers', timeline_markers)
        if timeline_markers:
            getNextLowest  = lambda seq,x: min([(x-i,i) for i in seq if x>=i] or [(0,None)])
            newLowest = getNextLowest([i[0] for i in timeline_markers], playtime)
            print('timeline_markers', timeline_markers)
            print('newLowest',newLowest)
            nextLowestColor = self.get_color_from_playtime(newLowest[1], timeline_markers)
            self.change_color( nextLowestColor)

    def update_rects(self):
        self.canvas.delete("all")
        previous_markers_right_value = 0
        for index, marker in enumerate(self.marker_data):        
            print('marker[0]', marker[0])
            previous_markers_right_pixel = self.get_pixel_from_value(previous_markers_right_value)
            this_markers_right_pixel = previous_markers_right_pixel + self.get_pixel_from_value(marker[0])            
            self.canvas.create_rectangle(this_markers_right_pixel-previous_markers_right_pixel, 0, 1920, 30, fill=marker[1], outline = "")
            self.canvas.pack()
            previous_markers_right_value =+ marker[0]

    # def add_marker(self, cur_slider_time, key_color, screen_width):
    #     if len(self.marker_data) == 0:
    #         self.marker_data.append([cur_slider_time, key_color])
    #     elif len(self.marker_data) > 0:
    #         print('cur_slider_time', cur_slider_time)
    #         print('self.marker_data[0]', self.marker_data[len(self.marker_data)-1][0])
    #         while cur_slider_time < self.marker_data[len(self.marker_data)-1][0]:
    #             self.marker_data.pop()
    #         self.marker_data.append([cur_slider_time, key_color])    
    #     print('self.marker_data', self.marker_data)
    #     self.update_rects()    

    def create_Widgets ( self ):
        print( '\ndef create_Widgets ( self ):' )
        self.canvas = tk.Canvas(self, width=50, height=50)
        self.canvas.pack(padx=15, anchor = 'w')
        self.canvas.create_oval(0, 0, 50, 50, fill = "black")



