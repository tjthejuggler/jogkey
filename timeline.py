#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox


class TimeLine( tk.Frame ):

    def __init__(self, master, index, track_length, screen_width, *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()

        self.master = master     # Tk window
        self.index = index
        self.marker_data = {}
        self.track_length = track_length
        self.screen_width = screen_width*.95
        self.label_pixel_width = None
        self.canvas = None
        self.create_Widgets()

    def get_total_marker_width(self):
        total_marker_width = 0
        if len(self.marker_data) > 0:
            for marker_key in list(self.marker_data.keys()):
                total_marker_width += marker_key
        return total_marker_width

    def get_pixel_from_value(self, value):
        print('value', value)
        print('self.screen_width', self.screen_width)
        print('self.track_length', self.track_length)
        pixel = ((value*self.screen_width)/self.track_length)
        print('pixel', pixel)
        return pixel

    def update_rects(self):
        self.canvas.delete("all")
        previous_markers_right_value = 0
        for index, marker_key in enumerate(list(self.marker_data.keys())):        
            print('marker_key', marker_key)
            previous_markers_right_pixel = self.get_pixel_from_value(previous_markers_right_value)
            this_markers_right_pixel = previous_markers_right_pixel + self.get_pixel_from_value(marker_key)            
            self.canvas.create_rectangle(this_markers_right_pixel-previous_markers_right_pixel, 0, 1920, 30, fill=self.marker_data[marker_key], outline = "")
            self.canvas.pack()
            previous_markers_right_value =+ marker_key

    def add_marker(self, cur_slider_time, key_color, screen_width):
        if len(self.marker_data) == 0:
            self.marker_data[cur_slider_time] = key_color
        elif len(self.marker_data) > 0:
            print('cur_slider_time', cur_slider_time)
            #print('self.marker_data[0]', self.marker_data[len(self.marker_data)-1][0])
            for key, value in self.marker_data.items():
                if cur_slider_time < key:
                    del self.marker_data[key]
            # while cur_slider_time < self.marker_data[len(self.marker_data)-1].key():
            #     self.marker_data.pop()
            self.marker_data[cur_slider_time] = key_color
        print('self.marker_data', self.marker_data)
        self.update_rects()    

    def create_Widgets ( self ):
        print( '\ndef create_Widgets ( self ):' )
        self.canvas = tk.Canvas(self, width=self.screen_width, height=30)
        self.canvas.pack(padx=15)
