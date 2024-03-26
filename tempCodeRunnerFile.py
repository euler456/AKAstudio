import customtkinter
import tkinter

from home_page import HomePage
from color_gear_page import ColorGearPage
from color_grab_page import ColorGrabPage
from color_converter_page import ColorConverterPage

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("NCM App")
        self.geometry("800x600")

        self.home_page = HomePage(self)
        self.home_page.pack(expand=True, fill="both")
        self.frames = {}

    def change_geometry(self, new_geometry):
        # Change the window geometry
        self.geometry(new_geometry)

    def change_title(self, new_title):
        # Change the window geometry
        self.title(new_title)

    def open_color_converter(self):
        self.home_page.destroy()
        self.converter_page = ColorConverterPage(self)
        self.frames["converter_page"] = self.converter_page
        self.converter_page.pack(expand=True, fill="both")
    
    def open_color_grab(self):
        self.home_page.destroy()
        self.grab_page = ColorGrabPage(self)
        self.frames["grab_page"] = self.grab_page
        self.grab_page.pack(expand=True, fill="both")
    
    def open_color_gear(self):
        self.home_page.destroy()
        self.gear_page = ColorGearPage(self)
        self.frames["gear_page"] = self.gear_page
        self.gear_page.pack(expand=True, fill="both")

    def open_home_page(self):
        self.destroy_all_frames()
        self.change_title("NCM App")
        self.home_page = HomePage(self)
        self.home_page.pack(expand=True, fill="both")

    def destroy_all_frames(self):
        # Destroy all frames in the dictionary
        for frame_name, frame in self.frames.items():
            frame.destroy()
        self.frames = {}  # Clear the dictionary

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
