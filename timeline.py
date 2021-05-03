#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox


class TimeLine( tk.Frame ):

    def __init__(self, master, index, *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()

        # MusicPlayer's Atrributes
        self.master = master     # Tk window
        self.index = index
        self.markers = []


        # Call these methods

        self.create_Widgets()

    def set_marker(self, i, j, slider_value):
        print("xxx", i, j, slider_value)
        this_markers_index = len(self.markers)
        total_marker_width = 0

        if this_markers_index > 0:
            total_marker_width = 0
            for o in self.markers :
                total_marker_width += o['width']

            print('total_marker_width', total_marker_width)


        self.markers.append(None)
        new_width = int(slider_value+slider_value*.2) - int(total_marker_width*1.2)
        if newwidth is negative then we need to remove the previous marker and make a new shorter one
        make the clors and hook up to keyboard
        if new_width > 0:
            print(int(slider_value+slider_value*.2) - total_marker_width)
            print(slider_value)
            #print(previous_marker_width)
            print('---')
            self.markers[this_markers_index] = tk.Button( self, text='sm' )
            self.markers[this_markers_index].config(text = slider_value, width = new_width, height = 3)
            self.markers[this_markers_index].pack(side = tk.LEFT)

    def create_Widgets ( self ):
        '''Create Buttons (e.g. Start & Stop ) and Progress Bar.''' 
        print( '\ndef create_Widgets ( self ):' )

        self.line_label = tk.Label( self, text='line'+str(self.index) )
        self.line_label.config(width = 16, height = 3)
        self.line_label.pack(side=tk.LEFT, anchor='w')
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