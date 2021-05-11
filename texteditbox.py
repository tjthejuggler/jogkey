import tkinter
from tkinter.scrolledtext import ScrolledText
class TextEditBox(object):

    root = None

    def __init__(self, msg):
        tki = tkinter
        print('msg', msg)
        self.top = tki.Toplevel(TextEditBox.root)
        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)
        label = tki.Label(frm, text=msg)
        label.pack(padx=4, pady=4)
        self.entry = ScrolledText(frm)
        self.entry.insert(tki.END, msg)
        self.entry.pack(pady=4)
        self.result = None
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict()
        b_submit.pack()
        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self):
        #print('dict_key', dict_key)
        data = self.entry.get('1.0', tkinter.END)
        print('data', data)
        if data:
            self.result = data
            self.top.destroy()

    def show( self ):
        self.entry.focus_force()
        self.top.wait_window()
        return self

#hook up get_edited_markers_from_balls in music.py
    #it needs to be called when focus returns, and it needs to get the edited markers from each ball and plug them in, and reload timelines with the new ones
        #change this into a mini editor
            #it needs to be bigger
            #needs all key buttons
            #music timeline hooked to size indicated by an antry    
                #timeline numbers could be in % so it doesn't matter if it gets the entry time
            #load/save
        #change this name
        #rename other things