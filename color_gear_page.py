import tkinter as tk
from tkinter import colorchooser

class ColorGearPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Create GUI elements
        self.color_label = tk.Label(self, text="Select Color:")
        self.color_button = tk.Button(self, text="Choose Color", command=self.choose_color)
        self.palette_canvas = tk.Canvas(self, width=300, height=150, bg='white')
        
        # Layout GUI elements
        self.color_label.pack()
        self.color_button.pack()
        self.palette_canvas.pack()

    def choose_color(self):
        color = colorchooser.askcolor()[1]  # Get the hexadecimal color code
        self.display_palette(color)

    def display_palette(self, color):
        # Clear previous palette
        self.palette_canvas.delete("all")
        
        # Display color palette
        self.palette_canvas.create_rectangle(50, 50, 250, 100, fill=color)

         # Button to navigate to Home page
        from home_page import HomePage
        home_button = tk.Button(self, text="Go to Home", command=lambda: controller.show_frame(HomePage))
        home_button.pack()


# Main application window
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Color Gear")
        self.geometry("400x300")

        # Create ColorGearPage instance and display it
        color_gear_page = ColorGearPage(self, self)
        color_gear_page.pack(fill="both", expand=True)

    def show_frame(self, frame_class):
        # Show the specified frame (not implemented in this example)
        pass

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
