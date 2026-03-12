from getopt import gnu_getopt

import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.geometry("500x600")
        self.title("Main Screen")
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky='nsw')
        self.CheckBox1 = ctk.CTkCheckBox(self.frame, text="cool")
        self.CheckBox1.grid(row=1,column=0, padx=10, pady=(10,0), sticky='w')
        self.CheckBox2 = ctk.CTkCheckBox(self.frame, text="cool")
        self.CheckBox2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')


app = App()
app.mainloop()
