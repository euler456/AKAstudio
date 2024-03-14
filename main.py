import tkinter as tk
from home_page import HomePage
from color_gear_page import ColorGearPage
from color_converter_page import ColorConverterPage
from color_grab_page import ColorGrabPage

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Set up the window
        self.title("Multi-page Tkinter GUI")
        self.geometry("800x600")
        
        # Create a container to hold the pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Create dictionary to hold frames for different pages
        self.frames = {}
        
        # Define and add frames for different pages
        for F in (HomePage, ColorGearPage, ColorConverterPage, ColorGrabPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show the Home page initially
        self.show_frame(HomePage)
    
    def show_frame(self, cont):
        print(cont,type(cont))
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
