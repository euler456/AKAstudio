import tkinter as tk
from customtkinter import CTkFrame, CTkCanvas ,CTkLabel, CTkButton

class ColorConverterPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # Label for the page title
        label = tk.Label(self, text="Color Converter Page")
        label.pack(pady=10, padx=10)
        
        # Dropdown menu to select color value type
        self.color_types = ["RGB", "HEX", "CMYK", "HSL", "HSV"]
        self.selected_color_type = tk.StringVar()
        self.selected_color_type.set(self.color_types[0])  # Default to RGB
        type_selector = tk.OptionMenu(self, self.selected_color_type, *self.color_types, command=self.update_inputs)
        type_selector.pack(pady=5)
        
        # Container frame for input fields
        self.input_container = tk.Frame(self)
        self.input_container.pack(pady=10)
        
        # Button to navigate to Home page
        from home_page import HomePage
        home_button = tk.Button(self, text="Go to Home", command=self.parent.open_home_page)
        home_button.pack()
        
        # Update input fields based on the selected color type
        self.update_inputs()
    
    def update_inputs(self, *args):
        # Clear existing input fields
        for widget in self.input_container.winfo_children():
            widget.destroy()
        
        # Add input fields based on the selected color type
        color_type = self.selected_color_type.get()
        if color_type == "RGB":
            self.add_rgb_inputs()
        elif color_type == "HEX":
            self.add_hex_input()
        elif color_type == "CMYK":
            self.add_cmyk_inputs()
        elif color_type == "HSL":
            self.add_hsl_inputs()
        elif color_type == "HSV":
            self.add_hsv_inputs()
    
    def add_rgb_inputs(self):
        # Add 3 input fields for RGB values
        for label_text in ["R:", "G:", "B:"]:
            label = tk.Label(self.input_container, text=label_text)
            label.pack(side="left")
            entry = tk.Entry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hex_input(self):
        # Add 1 input field for HEX value
        label = tk.Label(self.input_container, text="HEX:")
        label.pack(side="left")
        entry = tk.Entry(self.input_container)
        entry.pack(side="left", padx=5)
    
    def add_cmyk_inputs(self):
        # Add 4 input fields for CMYK values
        for label_text in ["C:", "M:", "Y:", "K:"]:
            label = tk.Label(self.input_container, text=label_text)
            label.pack(side="left")
            entry = tk.Entry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hsl_inputs(self):
        # Add 3 input fields for HSL values
        for label_text in ["H:", "S:", "L:"]:
            label = tk.Label(self.input_container, text=label_text)
            label.pack(side="left")
            entry = tk.Entry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hsv_inputs(self):
        # Add 3 input fields for HSV values
        for label_text in ["H:", "S:", "V:"]:
            label = tk.Label(self.input_container, text=label_text)
            label.pack(side="left")
            entry = tk.Entry(self.input_container)
            entry.pack(side="left", padx=5)
