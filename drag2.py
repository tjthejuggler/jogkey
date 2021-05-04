import tkinter
import tkinter.colorchooser
from mutagen.oggvorbis import OggVorbis
from music import *
from timeline import *

def main():
    canvas_width = 300
    canvas_height =300
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    #quit_button = tkinter.Button(root, command=root.quit, text="Quit").pack()
    #track_length = info.length()

    track_length = OggVorbis('output.ogg').info.length
    timelines = [None]*4
    for i in range(4):        
        timelines[i] = TimeLine( root, i, track_length)
        timelines[i].pack(anchor='w')
    music = MusicPlayer( root, tracktype='ogg' )
    keys = [[None]*10]*4
    key_labels = [['1','2','3','4','5','6','7','8','9','0'],
                  ['Q','W','E','R','T','Y','U','I','O','P'],
                  ['A','S','D','F','G','H','J','K','L',';'],
                  ['Z','X','C','V','B','N','M',',','.','/']]

    def choose_color(i, j):
        color_code = tkinter.colorchooser.askcolor()
        #print(i, j, color_code, music.slider_value.get())
        music.test_print()
        timelines[i].set_marker(i, j, music.slider.get(), music.slider_width)

    key_button_frame = tkinter.Frame(root, 
               width=canvas_width, 
               height=canvas_height)
    key_button_frame.pack()
    key_button_frame.pack(side=tkinter.BOTTOM)

    for i in range(4):
        for j in range(10):
            print(i,j, key_labels[i][j])
            keys[i][j] = tkinter.Button(key_button_frame, command = lambda i=i, j=j : choose_color(i, j))
            keys[i][j].config(text = key_labels[i][j], width = 3, height = 3)
            keys[i][j].grid(row=i,column=j)

    root.mainloop()


if __name__ == '__main__':
    main()