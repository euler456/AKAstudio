# main.py
import customtkinter as tk
from tkinter import Tk

from home_page import HomePage
from color_gear_page import ColorGearPage
from color_converter_page import ColorConverterPage
from color_grab_page import ColorGrabPage

class SampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Switching Example")
        
        self.page1 = HomePage(self.root, self.show_page1)
        self.page2 = ColorGrabPage(self.root, self.show_page2)
        self.show_page1()

    def show_page1(self):
        self.page2.pack_forget()
        self.page1.pack()

    def show_page2(self):
        self.page1.pack_forget()
        self.page2.pack()

if __name__ == "__main__":
    root = Tk()
    app = SampleApp(root)
    root.mainloop()
