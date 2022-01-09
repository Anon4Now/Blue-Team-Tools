import tkinter as tk
from tkinter import *


class DecoderGUIInput:

    # Set the GUI Geometry during object instantiation
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x50")
        self.root.title("Pilot Decoder")
        self.root.configure(bg='#16325c')
        self.entry = tk.Entry(self.root, bd=1)
        self.entry.config(fg='grey')
        self.entry.pack(side="left")
        self.entry.pack()
        self.entry.grid(row=1,
                        column=0,
                        padx=7,
                        pady=10,
                        ipadx=130,
                        ipady=3)
        self.result = None

    # Event listeners for user text entry
    def on_entry_click(self, event):  # need event param due to tkinter program
        if self.entry.get() == 'Paste encoded URL and press <ENTER>...':
            self.entry.delete(0, "end")  # delete all the text in the entry
        self.entry.insert(0, '')  # Insert blank for user input
        self.entry.config(fg='black')

    # Event listeners for user text entry
    def on_focusout(self, event):  # need event param due to tkinter program
        if self.entry.get() == '':
            self.entry.insert(0, 'Paste encoded URL and press <ENTER>...')
            self.entry.config(fg='grey')

    # Event listeners for user text entry
    def callback(self, event):  # need event param due to tkinter program
        self.result = self.entry.get()
        self.root.destroy()

    # Call the methods and binds the GUI
    def binding(self):
        self.entry.insert(0, 'Paste encoded URL and press <ENTER>...')
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<FocusOut>', self.on_focusout)
        self.entry.bind("<Return>", self.callback)
        self.root.mainloop()
        return self.result


# Returns output to GUI
class DecoderGUIOutput:

    @staticmethod
    def displayResult(resultInput):
        root_out = Tk()
        root_out.geometry("400x50")
        root_out.title("Pilot Decoder Output")
        text = Text(root_out)
        text.pack()
        text.insert(END, resultInput)
        root_out.mainloop()
