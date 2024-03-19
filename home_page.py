import customtkinter
import tkinter

class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)  # Set the width and height of the frame
        self.parent = parent

        self.home_frame = customtkinter.CTkFrame(master=self, width=300, height=200)
        self.home_frame.place(relx=0.5,rely=0.5, anchor=tkinter.CENTER)

        self.label = customtkinter.CTkLabel(self, text="Home Page", font=("Arial", 24))  # Increase font size
        self.label.pack(pady=50)  # Add more vertical padding
        
        self.button = customtkinter.CTkButton(master=self.home_frame, text="Color Grab", font=("Arial", 14), command=self.parent.open_color_grab) 
        self.button.pack(pady=20, padx = 40)  # Add vertical padding to the button

        self.button = customtkinter.CTkButton(master=self.home_frame, text="Color Gear", font=("Arial", 14), command=self.parent.open_color_gear) 
        self.button.pack(pady=20, padx = 40)  # Add vertical padding to the button

        self.button = customtkinter.CTkButton(master=self.home_frame, text="Color Converter", font=("Arial", 14), command=self.parent.open_color_converter) 
        self.button.pack(pady=20, padx = 40)  # Add vertical padding to the button
