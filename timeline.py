#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox


class TimeLine( tk.Frame ):

    def __init__(self, master, index, track_length, *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()

        # MusicPlayer's Atrributes
        self.master = master     # Tk window
        self.index = index
        self.markers = []
        self.track_length = track_length
        self.music_slider_width = None
        self.label_pixel_width = None


        # x                cur_num
        # slider_width     track_len



        # Call these methods

        self.create_Widgets()

    def get_total_marker_width(self):
        total_marker_width = 0
        if len(self.markers) > 0:
            for o in self.markers :
                total_marker_width += o['width']
        return total_marker_width

    def set_marker(self, i, j, slider_value, music_slider_width, color):
        print("xxx", i, j, slider_value)
        self.music_slider_width = music_slider_width
        total_marker_width = self.get_total_marker_width()

        print('total_marker_width', total_marker_width)
        print('track_length', self.track_length)
        print('music_slider_width', self.music_slider_width)
        print('guess', int(self.music_slider_width*slider_value/self.track_length))
        print('self.label_pixel_width', self.label_pixel_width)
        
        new_width = int((((self.music_slider_width*slider_value)/self.track_length)-100) - total_marker_width)
        print('new_width', new_width)
        while new_width < 0:           
            print('forget')
            self.markers[len(self.markers)-1].pack_forget()
            self.markers.pop()
            total_marker_width = self.get_total_marker_width()
            new_width = int((((self.music_slider_width*slider_value)/self.track_length)-100) - total_marker_width)
        if new_width > 0:
            self.markers.append(None)
            print('slider_value',slider_value)
            #print(previous_marker_width)
            print('---')
            pixel = tk.PhotoImage(width=1, height=1)
            #button = tk.Button(root, text="", image=pixel, width=100, height=100, compound="c")
            self.markers[len(self.markers)-1] = tk.Button( self, text='sm', image=pixel, width=new_width, height=20, compound="c")
            self.markers[len(self.markers)-1].config(text = slider_value, bg=color)
            self.markers[len(self.markers)-1].pack(side = tk.LEFT)




    def create_Widgets ( self ):
        '''Create Buttons (e.g. Start & Stop ) and Progress Bar.''' 
        print( '\ndef create_Widgets ( self ):' )

        pixel = tk.PhotoImage(width=1, height=1)

        self.line_label = tk.Button( self, text='line'+str(self.index), image=pixel, width=160, height=20, compound="c")

        self.line_label.config(width = 140, height = 20)
        self.line_label.pack(side=tk.LEFT, anchor='w')
        self.label_pixel_width = self.line_label.winfo_width()
        # self.playBut = tk.Button( self, text='WTF' )
        # self.playBut.pack(side=tk.LEFT, anchor='w')

        # #key_button_frame.pack(side=tkinter.BOTTOM)

        # self.stopBut = tk.Button( self, text='TOOOP' )
        # self.stopBut.pack(side=tk.LEFT,padx=10)





# if __name__ == "__main__":
#     root = tk.Tk()                              #Initialize an instance of Tk window.
#     app = MusicPlayer( root, tracktype='ogg' )  #Initialize an instance of MusicPlayer object and passing Tk window instance into it as it's master.
#     root.protocol("WM_DELETE_WINDOW", ask_quit) #Tell Tk window instance what to do before it is destroyed.
#     root.mainloop()                             #Start Tk window instance's mainloop.