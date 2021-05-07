import tkinter

class Mbox(object):

    root = None


    def __init__(self, msg, dict_key=None):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        root = tkinter.Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        #self.top = tkinter.Toplevel(Mbox.tki)
        #root.grab_set()
        frm = tkinter.Frame(root, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        label = tkinter.Label(frm, text=msg)
        label.pack(padx=4, pady=4)


        self.entry = tkinter.Entry(frm)
        self.entry.pack(pady=4)

        b_submit = tkinter.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict(dict_key)
        b_submit.pack()

        b_cancel = tkinter.Button(frm, text='Cancel')
        b_cancel['command'] = root.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self, dict_key):
        data = self.entry.get()
        if data:
            d, key = dict_key
            d[key] = data
            root.destroy()