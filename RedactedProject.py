from getopt import gnu_getopt

import customtkinter as ctk
import json

with open("Saves.json", 'r') as f:
    Loaded_Data = json.load(f)



class App(ctk.CTk):
    #made a function to handle making a button for the first frame as it was very repetitive
    def MainButton(self, Text ,root):
        return ctk.CTkButton(root, text=Text, width=200, height=100, font=('times', 40, 'bold'), corner_radius=32)

    #Creates the main gui
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen', True)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.geometry("500x600")
        self.title("Main Screen")

        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=50, pady=(10,0), sticky='nsw')

        self.AddButton = self.MainButton("add", self.frame)
        self.AddButton.grid(row=1,column=0, padx=10, pady=(10,200), sticky='w')

        self.ClearButton = self.MainButton("Clear", self.frame)
        self.ClearButton.grid(row=3, column=0, padx=10, pady=(10, 200), sticky='w')

        self.PlayButton = self.MainButton("Play", self.frame)
        self.PlayButton.grid(row=4, column=0, padx=10, pady=(10, 200), sticky='w')

        self.frame2 = ctk.CTkScrollableFrame(self, width=800)
        self.frame2.grid(row=0, column=2, padx=10, pady=(10, 0), sticky='nsw')

        #Iterates through the array held in the dictionary to create a button for each value
        for e, i in enumerate(Loaded_Data["ToDo"]):
            self.Button = ctk.CTkButton(self.frame2, text=i, font=('times', 20), width=790)
            self.Button.grid(row=e,column=0)


app = App()
app.mainloop()
