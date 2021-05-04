import tkinter
import tkinter.colorchooser
from mutagen.oggvorbis import OggVorbis
from music import *
from timeline import *
import numpy as np
import pygame

#default_colors = [['255','0','0'],['255','255','0'],['0','255','0'],
                    # ['0','255','255'],['0','0','255'],['255','0','255'],
                    # ['255','255','255'],['255','0','0'],['255','0','0'],['255','0','0']]

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
    canvas_width = 300
    canvas_height =300
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    #quit_button = tkinter.Button(root, command=root.quit, text="Quit").pack()
    #track_length = info.length()

    
    key_labels = [['1','2','3','4','5','6','7','8','9','0'],
                  ['Q','W','E','R','T','Y','U','I','O','P'],
                  ['A','S','D','F','G','H','J','K','L',';'],
                  ['Z','X','C','V','B','N','M',',','.','/']]

    current_colors = default_colors

    def event_handle(event):
        # Replace the window's title with event.type: input key
        print(event.char)

        array = np.array(key_labels)
        solutions = np.argwhere(array == event.char.upper())
        print(solutions)
        music.test_print()
        #print('sol00',solutions[0][0])
        timelines[solutions[0][0]].set_marker(solutions[0][0], solutions[0][1], music.slider.get(), music.slider_width)
        #print()

    event_sequence = '<KeyPress>'
    root.bind(event_sequence, event_handle)
    root.bind('<KeyRelease>', event_handle)


    track_length = OggVorbis('output.ogg').info.length
    timelines = [None]*4
    for i in range(4):        
        timelines[i] = TimeLine( root, i, track_length)
        timelines[i].pack(anchor='w')
    music = MusicPlayer( root, tracktype='ogg' )
    #keys = [[None]*10]*4
    keys = [[None for i in range(10)] for j in range(4)]


    def choose_color(i, j):
        color_code = tkinter.colorchooser.askcolor()
        print(i, j, color_code, music.slider_value.get())
        print(color_code[1],'color_code')
        print('i,j',i,j)
        keys[i][j].config(bg=color_code[1])
        #keys[1][0].config(bg='#FFFFFF')
        ass = np.array(keys)
        # print('shape',ass.shape)
        # print('keys[0][0]',keys[0][0])
        # print('keys2',keys)
        # for a in range(4):
        #     print('aCol',keys[a], a)
        #     for b in range(10):
        #         print('a,b',a,b)
        #         print('before',keys[a][b]['bg'])
        #         keys[a][b].config(bg='#FFFFFF')
        #         print('after',keys[a][b]['bg'])
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
            #keys[i][j].config(bg='#FFFFFF')
            # if i == 2:
            #     keys[i][j].config(bg='#FFFFFF')
            keys[i][j].grid(row=i,column=j)
    print('keys1',keys)

    # for a in range(4):
    #     print('aCol',keys[a])
    #     for b in range(10):
    #         print('a,b',a,b)
    #         print('before',keys[a][b]['bg'])
    #         keys[a][b].config(bg='#FFFFFF')
    #         print('after',keys[a][b]['bg'])

    root.mainloop()


if __name__ == '__main__':
    main()