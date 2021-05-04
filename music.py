#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen import MutagenError
from pygame import mixer
import tkinter as tk
import tkinter.messagebox as tkMessageBox


class MusicPlayer( tk.Frame ):

    def __init__(self, master, tracktype='ogg', *args, **kwargs):

        super().__init__(master) #initilizes self, which is a tk.Frame
        self.pack()

        # MusicPlayer's Atrributes
        self.master = master     # Tk window
        self.track = None        # Audio file
        self.trackLength = None  # Audio file length
        self.player = None       # Music player
        self.playBut = None      # Play Button
        self.stopBut = None      # Stop Button
        self.slider = None       # Progress Bar
        self.slider_value = None # Progress Bar value
        self.slider_width = None

        # Call these methods
        self.get_AudioFile_MetaData( tracktype )
        self.load_AudioFile()
        self.create_Widgets()

    def test_print(self):
        print("crazy test")

    def get_AudioFile_MetaData( self, tracktype ):
        '''Get audio file and it's meta data (e.g. tracklength).'''
        #print( '\ndef get_AudioFileMetaData( self, audiofile ):' )

        try:
            if tracktype == 'mp3':
                audiofile='roses.mp3' # In current directory
                f = MP3( audiofile )
            elif tracktype == 'ogg':
                audiofile='output.ogg' # In current directory
                f = OggVorbis( audiofile )
            else:
                raise print( 'Track type not supported.' )
        except MutagenError:
            print( "Fail to load audio file ({}) metadata".format(audiofile) )
        else:
            trackLength = f.info.length
        self.track = audiofile
        self.trackLength = trackLength; print( 'self.trackLength',type(self.trackLength),self.trackLength,' sec' )


    def load_AudioFile( self ):
        '''Initialise pygame mixer, load audio file and set volume.'''
        print( '\ndef load_AudioFile( self, audiofile ):' )
        player = mixer
        player.init()
        player.music.load( self.track )
        player.music.set_volume( .25 )

        self.player = player
        print('self.player ', self.player)


    def create_Widgets ( self ):
        '''Create Buttons (e.g. Start & Stop ) and Progress Bar.''' 
        print( '\ndef create_Widgets ( self ):' )


        #pixel = tk.PhotoImage(width=1, height=1)
            #button = tk.Button(root, text="", image=pixel, width=100, height=100, compound="c")
        #self.markers[len(self.markers)-1] = tk.Button( self, text='sm', image=pixel, width=new_width, height=20, compound="c")
            
        self.slider_value = tk.DoubleVar()
        self.slider = tk.Scale( self, to=self.trackLength, orient=tk.HORIZONTAL, length=self.winfo_screenwidth(),
                                resolution=0.01, showvalue=True, tickinterval=5, digit=5,
                                variable=self.slider_value, command=self.UpdateSlider )
        self.slider.pack(side=tk.TOP)

        self.playBut = tk.Button( self, text='Play', command=self.Play, width = 50, height = 20, compound="c" )
        self.playBut.pack(side=tk.LEFT)
        #key_button_frame.pack(side=tkinter.BOTTOM)

        self.stopBut = tk.Button( self, text='Stop', command=self.Stop, width = 50, height = 20, compound="c" )
        self.stopBut.pack(side=tk.LEFT,padx=10)

        button_widths = self.playBut.winfo_width() + self.stopBut.winfo_width() + 10
        #print('self.butFrame.winfo_width()', self.butFrame.winfo_width())



        self.slider_width = self.slider.winfo_screenwidth()


    def Play( self ):
        print('play')
        '''Play track from slider location.'''
        print('\ndef Play():')
        #1. Get slider location.
        #2. Play music from slider location.
        #3. Update slider location (use tk's .after loop)
        playtime = self.slider_value.get();       print( type(playtime),'playtime = ',playtime,'sec' )
        self.player.music.play( start=playtime ); print( 'Play Started' )
        self.TrackPlay( playtime )


    def TrackPlay( self, playtime ):
        #print('trackplay')
        '''Slider to track the playing of the track.'''
        #print('\ndef TrackPlay():')
        #1.When track is playing
        #   1. Set slider position to playtime
        #   2. Increase playtime by interval (1 sec)
        #   3. start TrackPlay loop
        #2.When track is not playing
        #   1. Print 'Track Ended'
        if self.player.music.get_busy():
            self.slider_value.set( playtime ); #print( type(self.slider_value.get()),'slider_value = ',self.slider_value.get() )
            playtime += .01 
            self.loopID = self.after(10, lambda:self.TrackPlay( playtime ) );\
                                               #print( 'self.loopID = ', self.loopID ) 
        else:
            print('Track Ended')


    def UpdateSlider( self, value ):
        '''Move slider position when tk.Scale's trough is clicked or when slider is clicked.'''
        #print( '\ndef UpdateSlider():' );       print(type(value),'value = ',value,' sec')
        if self.player.music.get_busy():
            #print("Track Playing")
            self.after_cancel( self.loopID ) #Cancel PlayTrack loop    
            self.slider_value.set( value )   #Move slider to new position
            self.Play( )                     #Play track from new postion
        else:
            #print("Track Not Playing")
            self.slider_value.set( value )   #Move slider to new position


    def Stop( self ):
        '''Stop the playing of the track.'''
        print('\ndef Stop():')
        if self.player.music.get_busy():
            self.player.music.stop()
            print('Play Stopped')


def ask_quit():
    '''Confirmation to quit application.'''
    if tkMessageBox.askokcancel("Quit", "Exit MusicPlayer"):
        app.Stop()         #Stop playing track 
        app.player.quit()  #Quit pygame.mixer
        root.destroy()     #Destroy the Tk Window instance.

        # Note: After initialzing pygame.mixer, it will preoccupy an entire CPU core.
        #       Before destroying the Tk Window, ensure pygame.mixer is quitted too else
        #       pygame.mixer will still be running in the background despite destroying the 
        #       Tk Window instance.


# if __name__ == "__main__":
#     root = tk.Tk()                              #Initialize an instance of Tk window.
#     app = MusicPlayer( root, tracktype='ogg' )  #Initialize an instance of MusicPlayer object and passing Tk window instance into it as it's master.
#     root.protocol("WM_DELETE_WINDOW", ask_quit) #Tell Tk window instance what to do before it is destroyed.
#     root.mainloop()                             #Start Tk window instance's mainloop.