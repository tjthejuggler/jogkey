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
        self.most_recent_marker_time = 0
        self.create_Widgets()

    def set_marker_data(self, data):
        self.marker_data = data
        if self.marker_data:
            self.update_rects()

    def get_total_marker_width(self):
        total_marker_width = 0
        if len(self.marker_data) > 0:
            for marker_key in list(self.marker_data.keys()):
                total_marker_width += marker_key
        return total_marker_width

    def get_pixel_from_value(self, value):
        pixel = ((float(value)*float(self.screen_width))/self.track_length)
        return pixel

    def update_rects(self):
        self.canvas.delete("all")
        print('type1', type(self.marker_data))
        previous_markers_right_value = 0
        print('isin', isinstance(self.marker_data, str))
        if isinstance(self.marker_data, str):
            print('was a string')
            self.marker_data = json.loads(self.marker_data)
        print('type2', type(self.marker_data))
        for marker_key in list(self.marker_data.keys()):  
            previous_markers_right_pixel = self.get_pixel_from_value(previous_markers_right_value)
            this_markers_right_pixel = previous_markers_right_pixel + self.get_pixel_from_value(marker_key)            
            self.canvas.create_rectangle(this_markers_right_pixel-previous_markers_right_pixel, 0, 1920, 30, fill=self.marker_data[marker_key], outline = "")
            self.canvas.pack()
            previous_markers_right_value =+ float(marker_key)

    def add_marker(self, cur_slider_time, key_color, screen_width):
        print('self.marker_data', self.marker_data)
        if len(self.marker_data) == 0:
            self.marker_data[cur_slider_time] = key_color
        elif len(self.marker_data) > 0:
            #print('cur_slider_time', cur_slider_time)
            for key in list(self.marker_data.items()):
            #for key, value in self.marker_data.items():
                if cur_slider_time < float(key[0]):
                    del self.marker_data[key[0]]
            self.marker_data[cur_slider_time] = key_color
        self.update_rects()    
        self.most_recent_marker_time = cur_slider_time

    def create_Widgets ( self ):
        print( '\ndef create_Widgets ( self ):' )
        self.canvas = tk.Canvas(self, width=self.screen_width, height=30)
        self.canvas.pack(padx=15)
