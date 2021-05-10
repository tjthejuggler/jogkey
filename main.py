import tkinter
import tkinter.colorchooser
import tkinter.filedialog
from mutagen.oggvorbis import OggVorbis
import numpy as np
import os
from os import path
from pathlib import Path
import json
import colour
import mbox
import texteditbox

#root = tkinter.Tk()



from music import *
from timeline import *
from ball import *

home = str(Path.home())
cwd = os.getcwd()

default_colors = ["#000000","#FFFFFF","#FF0000","#00FF00","#0000FF","#FFFF00","#00FFFF","#FF00FF","#00FFFF","#FF00FF"]

def main():
    canvas_width, canvas_height = 300, 300
    root = tkinter.Tk()
    Mbox = mbox.Mbox
    Mbox.root = root
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    track_length = OggVorbis('output.ogg').info.length
    lower_key_labels = [['1','2','3','4','5','6','7','8','9','0'],
                  ['q','w','e','r','t','y','u','i','o','p'],
                  ['a','s','d','f','g','h','j','k','l',';'],
                  ['z','x','c','v','b','n','m',',','.','/']]
    upper_key_labels = [['!','@','#','$','%','^','&','*','(',')'],
                  ['Q','W','E','R','T','Y','U','I','O','P'],
                  ['A','S','D','F','G','H','J','K','L',':'],
                  ['Z','X','C','V','B','N','M','<','>','?']]
    current_colors = default_colors


    def handle_focus(event):
        if event.widget == root:
            print("I have gained the focus")
            #get the new dict from music and balls and give it to timeline
            #organize stuff in main so all functins are together at bottom or top   


    root.bind("<FocusIn>", handle_focus)



    def keypress_handler(event):
        if not 'spinbox' in str(root.focus_get()) and event.char:
            fade = False
            lower_array = np.array(lower_key_labels)
            lower_solutions = np.argwhere(lower_array == event.char)
            if lower_solutions.size > 0:
                solutions = lower_solutions
            upper_array = np.array(upper_key_labels)
            upper_solutions = np.argwhere(upper_array == event.char)
            if upper_solutions.size > 0:
                solutions = upper_solutions
                fade = True
            music.test_print()
            if solutions.size > 0:
                key_row = solutions[0][0]
                key_column = solutions[0][1]
                cur_slider_time = music.slider.get()
                key_color = keys[key_row][key_column]['bg']
                if fade:
                    previousColor = music.getCurrentBallColor( key_row )#i need a previous time as well to determine to fade timestamps
                    previousMarkerTime = timelines[key_row].most_recent_marker_time
                    fade_gap_length = cur_slider_time - previousMarkerTime
                    print('fade_gap_length', fade_gap_length)
                    fade_levels = max(int(fade_gap_length)*2, 50)
                    fade_colors = list(colour.Color(previousColor).range_to(colour.Color(key_color),fade_levels))
                    gap_increment = fade_gap_length / fade_levels
                    for index, fade_color in enumerate(fade_colors):
                        timelines[key_row].add_marker(previousMarkerTime + (index * gap_increment), fade_color.hex_l, music.slider_width)
                        music.update_timeline_markers(timelines[key_row].marker_data,key_row)
                else:
                    timelines[key_row].add_marker(cur_slider_time, key_color, music.slider_width)
                    music.update_timeline_markers(timelines[key_row].marker_data,key_row)

    def file_load():
        chosen_dir = tkinter.filedialog.askdirectory()
        if chosen_dir is None:
            return
        for i in range(4):
            if path.exists(chosen_dir+'/marker_data'+str(i)):         
                with open(chosen_dir+'/marker_data'+str(i)) as json_file:
                    new_dict = {}
                    loaded_dict = json.load(json_file)
                    for sub in loaded_dict.keys():
                        new_dict[float(sub)] = loaded_dict[sub]
                    timelines[i].set_marker_data(new_dict)
                    music.update_timeline_markers(timelines[i].marker_data,i)

    def file_save():
        chosen_dir = tkinter.filedialog.askdirectory()
        if chosen_dir is None:
            return
        for i in range(4):
            my_json = json.dumps(timelines[i].marker_data, ensure_ascii=False, indent=1, sort_keys=True)
            f = open(chosen_dir+'/marker_data'+str(i),"w")
            f.write(my_json)
            f.close()

    save_button = tkinter.Button(root, command=file_save, text="Save").pack()
    load_button = tkinter.Button(root, command=file_load, text="Load").pack()
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

    def testtest( self ):
        print('testtest')

    def right_click( self ):
        print('right_click')#this right click is where we show the mini editor
        #root.grab_set()

        D = {'user':'Bob'}

        print('D', D)
        # b_login = tkinter.Button(root, text='Log in')
        # b_login['command'] = lambda: Mbox('Name?', (D, 'user'))
        # b_login.pack()

        # b_loggedin = tkinter.Button(root, text='Current User')
        # b_loggedin['command'] = lambda: Mbox(D['user'])
        # b_loggedin.pack()
        test = Mbox(root, "testing").show()
        #test.bind("<Destroy>",testtest())
        print('test.result333', test.result)


        print('D2', D)      

    key_button_frame = tkinter.Frame(root, 
               width=canvas_width, 
               height=canvas_height)
    key_button_frame.pack()
    key_button_frame.pack(side=tkinter.BOTTOM)

    for i in range(4):
        for j in range(10):
            #print(i,j, lower_key_labels[i][j])
            keys[i][j] = tkinter.Button(key_button_frame, command = lambda i=i, j=j : choose_color(i, j), bg=current_colors[j])
            keys[i][j].config(text = lower_key_labels[i][j], width = 3, height = 3)
            keys[i][j].grid(row=i,column=j)
            #keys[i][j].bind("<Button-1>", left_click)
            keys[i][j].bind("<Button-3>", right_click)
    print('keys1',keys)




    root.mainloop()

if __name__ == '__main__':
    main()

    