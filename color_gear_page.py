import tkinter as tk

class ColorGearPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Color Gear Page")
        label.pack(pady=10, padx=10)
        
        # Button to navigate to Home page
        home_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame(HomePage))
        home_button.pack()
