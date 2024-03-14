import tkinter as tk
from color_gear_page import ColorGearPage
from color_converter_page import ColorConverterPage
from color_grab_page import ColorGrabPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page")
        label.pack(pady=10, padx=10)
        
        # Button to navigate to Color Grab page
        color_grab_button = tk.Button(self, text="Go to Color Grab", command=lambda: controller.show_frame(ColorGrabPage))
        color_grab_button.pack()

        color_gear_button = tk.Button(self, text="Go to Color Gear", command=lambda: controller.show_frame(ColorGearPage))
        color_gear_button.pack()

        color_converter_button = tk.Button(self, text="Go to Color Converter", command=lambda: controller.show_frame(ColorConverterPage))
        color_converter_button.pack()