# home_page.py
from customtkinter import CTkFrame, CTkLabel, CTkButton

class HomePage(CTkFrame):
    def __init__(self, parent, show_page2_callback):
        super().__init__(parent)
        
        self.label = CTkLabel(self, text="Home Page")
        self.label.pack(pady=10)
        
        self.button = CTkButton(self, text="Go to Color Gear", command=show_page2_callback)
        self.button.pack()