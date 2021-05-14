#!/usr/bin/python3
# -*- coding: utf-8 -*-
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from ball import *
from pathlib import Path
import os
from os import path

class MusicPlayer( tk.Frame ):



    def __init__(self, master, tracktype='ogg', *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()

        self.master = master     # Tk window
        self.track = None        # Audio file
        self.trackLength = None  # Audio file length
        self.chosen_file = 'glitches.ogg'
        self.player = None       # Music player
        self.playBut = None      # Play Button
        self.stopBut = None      # Stop Button
        self.slider = None       # Progress Bar
        self.slider_value = None # Progress Bar value
        self.slider_width = None
        self.my_balls = [None]*4
        self.timeline_markers = [None]*4
        self.get_AudioFile_MetaData( tracktype )
        self.load_AudioFile()
        self.create_Widgets()

    def update_timeline_markers(self, marker, index):
        #print('music update timeline markers', marker, index)
        self.timeline_markers[index] = marker
        self.my_balls[index].set_timeline_markers(self.timeline_markers[index])
        self.my_balls[index].update_color(self.timeline_markers[index], self.slider_value.get())

    def test_print(self):
        print("crazy test")

    def get_AudioFile_MetaData( self, tracktype ):
        if self.chosen_file:
            try:
                audiofile='glitches.ogg' # In current directory
                f = OggVorbis( audiofile )
            except MutagenError:
                print( "Fail to load audio file ({}) metadata".format(audiofile) )
            else:
                trackLength = f.info.length
            self.track = self.chosen_file
            self.trackLength = trackLength; print( 'self.trackLength',type(self.trackLength),self.trackLength,' sec' )

    def get_edited_markers_from_balls( self ):
        markers = [None]*4
        for index, ball in enumerate(self.my_balls):
            markers[index] = self.my_balls[index].timeline_markers
        return markers

    def load_AudioFile( self ):
        print( '\ndef load_AudioFile( self, audiofile ):' )
        player = mixer
        player.init()
        player.music.load( self.chosen_file ) #self.track is probably normally filled automatically, but now it needs to wait for chosen
        player.music.set_volume( .25 )
        self.player = player
        print('self.player ', self.player)

    def create_Widgets ( self ):
        self.slider_value = tk.DoubleVar()
        self.slider = tk.Scale( self, to=self.trackLength, orient=tk.HORIZONTAL, length=self.winfo_screenwidth(),
                                resolution=0.01, showvalue=True, tickinterval=5, digit=5,
                                variable=self.slider_value, command=self.UpdateSlider )
        self.slider.pack(side=tk.TOP)

        def browseSongs():
            home = str(Path.home())
            cwd = os.getcwd()
            filename = tk.filedialog.askopenfilename(initialdir = cwd, title = "Select a File",
                                                  filetypes = (("Text files", "*.ogg*"),
                                                               ("all files", "*.*")))
            label_file_explorer.configure(text="File Opened: "+os.path.basename(filename))
            self.chosen_file = filename
            self.load_AudioFile()                 

        label_file_explorer = tk.Label(self, text = "File Explorer using Tkinter",
                                    width = 100, height = 4, fg = "blue")              
        button_explore = tk.Button(self, text = "Browse Files", command = browseSongs)
        label_file_explorer.pack()
        button_explore.pack()
        self.playBut = tk.Button( self, text='Play', command=self.Play, width = 50, height = 20, compound="c" )
        self.playBut.pack(side=tk.LEFT)
        self.stopBut = tk.Button( self, text='Stop', command=self.Stop, width = 50, height = 20, compound="c" )
        self.stopBut.pack(side=tk.LEFT,padx=10)
        for i in range(4):
            self.my_balls[i] = Ball( self )
            self.my_balls[i].pack()
            self.my_balls[i].set_IP('11')
        button_widths = self.playBut.winfo_width() + self.stopBut.winfo_width() + 10
        self.slider_width = self.slider.winfo_screenwidth()

    def Play( self ):
        if self.chosen_file:
            playtime = self.slider_value.get();       #print( type(playtime),'playtime = ',playtime,'sec' )
            self.player.music.play( start=playtime ); #print( 'Play Started' )
            self.TrackPlay( playtime )

    def TrackPlay( self, playtime ):
        for index, ball in enumerate(self.my_balls):
            ball.update_color(self.timeline_markers[index], playtime)
        if self.player.music.get_busy():
            self.slider_value.set( playtime ); #print( type(self.slider_value.get()),'slider_value = ',self.slider_value.get() )
            playtime += .01 
            self.loopID = self.after(10, lambda:self.TrackPlay( playtime ) )
        else:
            print('Track Ended')

    def getCurrentBallColor( self, index ):
        return self.my_balls[index].currentColor

    def UpdateSlider( self, value ):
        if self.player.music.get_busy():
            self.after_cancel( self.loopID ) #Cancel PlayTrack loop    
            self.slider_value.set( value )   #Move slider to new position
            self.Play( )                     #Play track from new postion
        else:
            self.slider_value.set( value )   #Move slider to new position

    def Stop( self ):
        print('\ndef Stop():')
        if self.player.music.get_busy():
            self.player.music.stop()
            print('Play Stopped')

def ask_quit():
    if tkMessageBox.askokcancel("Quit", "Exit MusicPlayer"):
        app.Stop()         #Stop playing track 
        app.player.quit()  #Quit pygame.mixer
        root.destroy()     #Destroy the Tk Window instance.