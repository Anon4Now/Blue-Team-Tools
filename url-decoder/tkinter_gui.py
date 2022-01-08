import tkinter as tk
from tkinter import *
# from url_decoder import URLDefenseDecoder


class DecoderGUIInput:

    # Generate GUI for user input
    @staticmethod
    def tkinter_input():  # removed prompt="" parameter as it is not used
        root = tk.Tk()
        root.geometry("400x50")
        root.title("Pilot Decoder")
        root.configure(bg='#16325c')
        entry = tk.Entry(root, bd=1)
        entry.config(fg='grey')
        entry.pack(side="left")
        entry.pack()
        entry.grid(row=1,
                   column=0,
                   padx=7,
                   pady=10,
                   ipadx=130,
                   ipady=3)
        result = None

        # Event listeners for user text entry
        def on_entry_click():  # removed event from parameter
            if entry.get() == 'Paste encoded URL and press <ENTER>...':
                entry.delete(0, "end")  # delete all the text in the entry
            entry.insert(0, '')  # Insert blank for user input
            entry.config(fg='black')

        def on_focusout():
            if entry.get() == '':
                entry.insert(0, 'Paste encoded URL and press <ENTER>...')
                entry.config(fg='grey')

        def callback():
            nonlocal result
            result = entry.get()
            root.destroy()

        entry.insert(0, 'Paste encoded URL and press <ENTER>...')
        entry.bind('<FocusIn>', on_entry_click)
        entry.bind('<FocusOut>', on_focusout)
        entry.bind("<Return>", callback)
        root.mainloop()
        return result

    # result = tkinter_input()  # may need to remove this line


class DecoderGUIOutput:
    # Returns output to GUI
    # endresult = main()  # may need to remove this line

    @staticmethod
    def displayResult(resultInput):
        root_out = Tk()
        root_out.geometry("400x50")
        root_out.title("Pilot Decoder Output")
        text = Text(root_out)
        text.pack()
        text.insert(END, resultInput)
        root_out.mainloop()
