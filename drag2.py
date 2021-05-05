import tkinter
import tkinter.colorchooser
import tkinter.filedialog
from mutagen.oggvorbis import OggVorbis
from music import *
from timeline import *
from ball import *
import numpy as np
import pygame

default_colors = ["#000000",
"#FFFFFF",
"#FF0000",
"#00FF00",
"#0000FF",
"#FFFF00",
"#00FFFF",
"#FF00FF",
"#00FFFF",
"#FF00FF"]

def main():
    canvas_width, canvas_height = 300, 300
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    track_length = OggVorbis('output.ogg').info.length
    #quit_button = tkinter.Button(root, command=root.quit, text="Quit").pack()
    key_labels = [['1','2','3','4','5','6','7','8','9','0'],
                  ['Q','W','E','R','T','Y','U','I','O','P'],
                  ['A','S','D','F','G','H','J','K','L',';'],
                  ['Z','X','C','V','B','N','M',',','.','/']]
    current_colors = default_colors

    def keypress_handler(event):
        print(event.char)
        array = np.array(key_labels)
        solutions = np.argwhere(array == event.char.upper())
        print('solutions1', solutions)
        music.test_print()
        key_row = solutions[0][0]
        key_column = solutions[0][1]
        cur_slider_time = music.slider.get()
        key_color = keys[key_row][key_column]['bg']
        print('key_row', key_row)
        timelines[key_row].add_marker(cur_slider_time, key_color, music.slider_width)
        music.update_timeline_markers(timelines[key_row].marker_data,key_row)

    def file_save():

        print('save',tkinter.filedialog.askdirectory())
        f = tkinter.filedialog.askdirectory()
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
#make a for loop here that makes 5 files in our directory, timelines and key config

        f.write(timelines)
        f.close() 

    def file_open():
        print('file_open',tkinter.filedialog.askopenfilename())

#maybe markers should be a dict

    save_button = tkinter.Button(root, command=file_save, text="Save").pack()
    save_button = tkinter.Button(root, command=file_open, text="Open").pack()


    event_sequence = '<KeyPress>'
    root.bind(event_sequence, keypress_handler)
    
    timelines = [None]*4
    for i in range(4):        
        timelines[i] = TimeLine( root, i, track_length, w)
        timelines[i].pack(anchor='w')
    music = MusicPlayer( root, tracktype='ogg' )
    keys = [[None for i in range(10)] for j in range(4)]

    def choose_color(i, j):
        color_code = tkinter.colorchooser.askcolor()
        print(i, j, color_code, music.slider_value.get())
        print(color_code[1],'color_code')
        print('i,j',i,j)
        keys[i][j].config(bg=color_code[1])
        ass = np.array(keys)
        print(keys[i])

    key_button_frame = tkinter.Frame(root, 
               width=canvas_width, 
               height=canvas_height)
    key_button_frame.pack()
    key_button_frame.pack(side=tkinter.BOTTOM)

    for i in range(4):
        for j in range(10):
            print(i,j, key_labels[i][j])
            keys[i][j] = tkinter.Button(key_button_frame, command = lambda i=i, j=j : choose_color(i, j), bg=current_colors[j])
            keys[i][j].config(text = key_labels[i][j], width = 3, height = 3)
            keys[i][j].grid(row=i,column=j)
    print('keys1',keys)

    root.mainloop()


if __name__ == '__main__':
    main()