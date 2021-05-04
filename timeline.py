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

        # MusicPlayer's Atrributes
        self.master = master     # Tk window
        self.index = index
        self.markers = []
        self.marker_data = []
        self.track_length = track_length
        self.screen_width = screen_width*.95
        self.label_pixel_width = None
        self.canvas = None


        # x                cur_num
        # slider_width     track_len



        # Call these methods

        self.create_Widgets()

    def get_total_marker_width(self):
        total_marker_width = 0
        if len(self.marker_data) > 0:
            for marker in self.marker_data :
                total_marker_width += marker[0]
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
        #for marker in self.marker_data:   
        for index, marker in enumerate(self.marker_data):        
            #w = tk.Canvas(self, width=1250, height=1200)
            print('marker[0]', marker[0])
            #previous_marker_end = self.get_total_marker_width(index)
            #print('previous_marker_end', previous_marker_end)
            previous_markers_right_pixel = self.get_pixel_from_value(previous_markers_right_value)
            this_markers_right_pixel = previous_markers_right_pixel + self.get_pixel_from_value(marker[0])
            
            self.canvas.create_rectangle(previous_markers_right_pixel, 0, this_markers_right_pixel-previous_markers_right_pixel, 30, fill=marker[1], outline = "")
            #w.create_rectangle(50, 50, 100, 1000, fill="red", outline = 'blue') 
            self.canvas.pack()
            previous_markers_right_value =+ marker[0]

    def add_marker(self, cur_slider_time, key_color, screen_width):
        if len(self.marker_data) == 0:
            self.marker_data.append([cur_slider_time, key_color])
        elif len(self.marker_data) > 0:
            print('cur_slider_time', cur_slider_time)
            print('self.marker_data[0]', self.marker_data[len(self.marker_data)-1][0])
            while cur_slider_time < self.marker_data[len(self.marker_data)-1][0]:
                self.marker_data.pop()
            self.marker_data.append([cur_slider_time, key_color])    
        print('self.marker_data', self.marker_data)
        self.update_rects()


    def set_marker(self, i, j, slider_value, screen_width, color):
        print("xxx", i, j, slider_value)
        self.screen_width = screen_width-60
        total_marker_width = self.get_total_marker_width()

        print('total_marker_width', total_marker_width)
        print('track_length', self.track_length)
        print('screen_width', self.screen_width)
        print('guess', int(self.screen_width*slider_value/self.track_length))
        print('self.label_pixel_width', self.label_pixel_width)
        
        new_width = int(((self.screen_width*slider_value)/self.track_length) - total_marker_width)
        print('new_width', new_width)
        while new_width < 0:           
            print('forget')
            self.markers[len(self.markers)-1].pack_forget()
            self.markers.pop()
            total_marker_width = self.get_total_marker_width()
            new_width = int((((self.screen_width*slider_value)/self.track_length)) - total_marker_width)
        if new_width > 0:
            self.markers.append(None)
            print('slider_value',slider_value)
            #print(previous_marker_width)
            print('---')
            pixel = tk.PhotoImage(width=1, height=1)

            #button = tk.Button(root, text="", image=pixel, width=100, height=100, compound="c")
            self.markers[len(self.markers)-1] = tk.Button( self, text='', image=pixel, width=new_width, height=20, compound="c")
            self.markers[len(self.markers)-1].config(bg=color, highlightthickness = 0)
            self.markers[len(self.markers)-1].pack(side = tk.LEFT)


#try creating rects instead of buttons, save times to external variable, even back it up text file
            w = tk.Canvas(self, width=1920, height=1200)
            w.create_rectangle(0, 0, 100, 1000, fill="blue", outline = 'blue')
            w.create_rectangle(50, 50, 100, 1000, fill="red", outline = 'blue') 
            w.pack()
      

    def create_Widgets ( self ):
        '''Create Buttons (e.g. Start & Stop ) and Progress Bar.''' 
        print( '\ndef create_Widgets ( self ):' )
        self.canvas = tk.Canvas(self, width=self.screen_width, height=30)
        self.canvas.pack(padx=15)
        #pixel = tk.PhotoImage(width=1, height=1)

        #self.line_label = tk.Button( self, text='line'+str(self.index), image=pixel, width=160, height=20, compound="c")

        #self.line_label.config(width = 140, height = 20)
        #self.line_label.pack(side=tk.LEFT, anchor='w')
        #self.label_pixel_width = self.line_label.winfo_width()
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