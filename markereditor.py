import tkinter
from tkinter.scrolledtext import ScrolledText

class MarkerEditor(object):

    root = None

    def __init__(self, msg):
        self.top = None
        self.entry = None
        self.result = None
        self.msg = msg
        self.create_Widgets()

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

    def create_Widgets ( self ):
        tki = tkinter
        print('msgz', self.msg)
        print('MarkerEditor.root', MarkerEditor.root)
        self.top = tki.Toplevel(MarkerEditor.root)
        print('m1')
        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        print('m2')
        frm.pack(fill='both', expand=True)
        print('m3')
        label = tki.Label(frm, text=self.msg)
        print('m4')
        label.pack(padx=4, pady=4)
        print('m5')
        self.entry = ScrolledText(frm)
        print('m6')
        self.entry.insert(tki.END, self.msg)
        print('m7')
        self.entry.pack(pady=4)
        self.result = None
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict()
        b_submit.pack()
        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)