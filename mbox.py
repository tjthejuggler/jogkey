import tkinter

class Mbox(object):

    root = None

    def __init__(self, msg, dict_key=None):
        tki = tkinter
        self.top = tki.Toplevel(Mbox.root)
        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)
        label = tki.Label(frm, text=msg)
        label.pack(padx=4, pady=4)
        caller_wants_an_entry = dict_key is not None
        self.entry = tki.Entry(frm)
        self.entry.pack(pady=4)
        self.result = None
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict(dict_key)
        b_submit.pack()
        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self, dict_key):
        print('dict_key', dict_key)
        data = self.entry.get()
        print('data', data)
        if data:
            self.result = data
            self.top.destroy()

    def show( self ):
        self.entry.focus_force()
        self.top.wait_window()
        return self
