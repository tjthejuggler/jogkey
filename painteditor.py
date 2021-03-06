import tkinter
from tkinter.scrolledtext import ScrolledText

from music import *
from timeline import *
from ball import *

class PaintEditor(object):

    root = None

    def __init__(self, msg):
        self.top = None
        self.entry = None
        self.result = None
        self.msg = msg
        self.create_Widgets()

    def entry_to_dict(self, dict_key):
        #print('dict_key', dict_key)
        data = self.entry.get('1.0', tkinter.END)
        print('data', data)
        if data:
            self.result = data
            self.top.destroy()

    def show( self ):
        #self.entry.focus_force()
        self.top.wait_window()
        return self

    def create_Widgets ( self ):
        tki = tkinter
        print('msg', self.msg)
        self.top = tki.Toplevel(PaintEditor.root)
        print('self.top',self.top)
        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)
        label = tki.Label(frm, text=self.msg)
        label.pack(padx=4, pady=4)
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict()
        b_submit.pack()
        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)
        painteditor_music = MusicPlayer( self.top, True, tracktype='ogg' )