from customtkinter import CTkFrame, CTkLabel, CTkButton

class HomePage(CTkFrame):
    def __init__(self, parent, show_page2_callback):
        super().__init__(parent)  # Set the width and height of the frame
        
        self.label = CTkLabel(self, text="Home Page", font=("Arial", 24))  # Increase font size
        self.label.pack(pady=50)  # Add more vertical padding
        
        self.button = CTkButton(self, text="Go to Color Gear", command=show_page2_callback, font=("Arial", 14)) 
        self.button.pack(pady=20)  # Add vertical padding to the button
