import tkinter

class Mbox(object):

    root = None

    def __init__(self, msg, dict_key=None):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        tki = tkinter
        self.top = tki.Toplevel(Mbox.root)

        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        label = tki.Label(frm, text=msg)
        label.pack(padx=4, pady=4)

        caller_wants_an_entry = dict_key is not None

        #if caller_wants_an_entry:
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
            #d, key = dict_key
            #d[key] = data
            #self.top.destroy()
            self.result = data

    def show( self ):
        #self.wm_deiconify()
        self.entry.focus_force()
        self.top.wait_window()
        return self

        #put this into texteditor
        #make apply close the window too, make cancel not pass anything
        #change this into a mini editor
        #change this name
        #rename other things