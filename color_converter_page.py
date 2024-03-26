import tkinter as tk
import customtkinter
from color_conversion_functions import rgb_to_hex, hex_to_rgb, rgb_to_cmyk, cmyk_to_rgb, rgb_to_hsl, hsl_to_rgb, rgb_to_hsv, hsv_to_rgb

class ColorConverterPage(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.rgb_values = [0, 0, 0]  # Initialize RGB values
        self.hex_value = ""  # Initialize HEX value
        self.cmyk_values = [0, 0, 0, 0]  # Initialize CMYK values
        self.hsl_values = [0, 0, 0]  # Initialize HSL values
        self.hsv_values = [0, 0, 0]  # Initialize HSV values
        
        # Label for the page title
        label = customtkinter.CTkLabel(self, text="Color Converter Page")
        label.pack(pady=10, padx=10)

        self.input_container = customtkinter.CTkFrame(master=self, width=300, height=300)
        self.input_container.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.output_container = None
        
        # Dropdown menu to select color value type
        self.color_types = ["RGB", "HEX", "CMYK", "HSL", "HSV"]
        self.selected_color_type = customtkinter.StringVar(value=self.color_types[0])
        type_selector = customtkinter.CTkOptionMenu(self, variable=self.selected_color_type, values=self.color_types, command=self.update_inputs)
        type_selector.pack()
        
        # Button to navigate to Home page
        from home_page import HomePage
        self.home_button = customtkinter.CTkButton(self, text="Go to Home", command=self.parent.open_home_page)
        self.home_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        
        # Button to trigger conversion
        self.convert_button = customtkinter.CTkButton(self, text="Convert", command=self.convert_values)
        self.convert_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        # Update input fields based on the selected color type
        self.update_inputs()

    def create_label_and_entry(self, container, label_text):
        label = customtkinter.CTkLabel(container, text=label_text)
        label.pack(side="left")
        entry = customtkinter.CTkEntry(container)
        entry.pack(side="left", padx=10, pady=10)
        return entry
    
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

    def add_hex_input(self):
        # Add 1 input field for HEX value
        self.hex_entry = self.create_label_and_entry(self.input_container, "HEX: ")
    
    def add_rgb_inputs(self):
        # Add 3 input fields for RGB values
        self.rgb_entries = []
        for label_text in ["R:", "G:", "B:"]:
            entry = self.create_label_and_entry(self.input_container, label_text)
            self.rgb_entries.append(entry)
    
    def add_cmyk_inputs(self):
        # Add 4 input fields for CMYK values
        self.cmyk_entries = []
        for label_text in ["C:", "M:", "Y:", "K:"]:
            entry = self.create_label_and_entry(self.input_container, label_text)
            self.cmyk_entries.append(entry)
    
    def add_hsl_inputs(self):
        # Add 3 input fields for HSL values
        self.hsl_entries = []
        for label_text in ["H:", "S:", "L:"]:
            entry = self.create_label_and_entry(self.input_container, label_text)
            self.hsl_entries.append(entry)
    
    def add_hsv_inputs(self):
        # Add 3 input fields for HSV values
        self.hsv_entries = []
        for label_text in ["H:", "S:", "V:"]:
            entry = self.create_label_and_entry(self.input_container, label_text)
            self.hsv_entries.append(entry)

    def update_rgb_values(self):
        self.rgb_values = [int(entry.get()) for entry in self.rgb_entries]

    def update_cmyk_values(self):
        self.cmyk_values = [float(entry.get()) for entry in self.cmyk_entries]

    def update_hsl_values(self):
        self.hsl_values = [float(entry.get()) for entry in self.hsl_entries]

    def update_hsv_values(self):
        self.hsv_values = [float(entry.get()) for entry in self.hsv_entries]

    def convert_values(self):
        color_type = self.selected_color_type.get()
        if color_type == "RGB":
            self.update_rgb_values()
            self.convert_rgb_to_other_formats()
        elif color_type == "HEX":
            self.hex_value = self.hex_entry.get()
            self.convert_hex_to_other_formats()
        elif color_type == "CMYK":
            self.update_cmyk_values()
            self.convert_cmyk_to_other_formats()
        elif color_type == "HSL":
            self.update_hsl_values()
            self.convert_hsl_to_other_formats()
        elif color_type == "HSV":
            self.update_hsv_values()
            self.convert_hsv_to_other_formats()
        
        self.display_converted_values()

    def convert_rgb_to_other_formats(self):
        self.hex_value = rgb_to_hex(self.rgb_values) # Convert RGB to HEX
        self.cmyk_values = rgb_to_cmyk(self.rgb_values) # Convert RGB to CMYK
        self.hsl_values = rgb_to_hsl(self.rgb_values) # Convert RGB to HSL
        self.hsv_values = rgb_to_hsv(self.rgb_values) # Convert RGB to HSV

    def convert_hex_to_other_formats(self):
        self.rgb_values = hex_to_rgb(self.hex_value) # Convert HEX to RGB
        self.cmyk_values = rgb_to_cmyk(self.rgb_values) # Convert RGB to CMYK  
        self.hsl_values = rgb_to_hsl(self.rgb_values) # Convert RGB to HSL
        self.hsv_values = rgb_to_hsv(self.rgb_values) # Convert RGB to HSV
 
    def convert_cmyk_to_other_formats(self):
        self.rgb_values = cmyk_to_rgb(self.cmyk_values) # Convert CMYK to RGB
        self.hex_value = rgb_to_hex(self.rgb_values) # Convert RGB to HEX
        self.hsl_values = rgb_to_hsl(self.rgb_values) # Convert RGB to HSL
        self.hsv_values = rgb_to_hsv(self.rgb_values) # Convert RGB to HSV

    def convert_hsl_to_other_formats(self):
        self.rgb_values = hsl_to_rgb(self.hsl_values) # Convert HSL to RGB
        self.hex_value = rgb_to_hex(self.rgb_values) # Convert RGB to HEX
        self.cmyk_values = rgb_to_cmyk(self.rgb_values) # Convert RGB to CMYK
        self.hsv_values = rgb_to_hsv(self.rgb_values) # Convert RGB to HSV

    def convert_hsv_to_other_formats(self):
        self.rgb_values = hsv_to_rgb(self.hsv_values) # Convert HSV to RGB
        self.hex_value = rgb_to_hex(self.rgb_values) # Convert RGB to HEX
        self.cmyk_values = rgb_to_cmyk(self.rgb_values) # Convert RGB to CMYK
        self.hsl_values = rgb_to_hsl(self.rgb_values) # Convert RGB to HSL

    def display_converted_values(self):
        # Clear existing value labels
        for widget in self.input_container.winfo_children():
            if isinstance(widget, customtkinter.CTkLabel):
                widget.destroy()
        
        if self.output_container is not None: self.output_container.destroy()
        self.output_container = customtkinter.CTkFrame(master=self, width=300, height=300)
        self.output_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Iterate over color types and display converted values
        for color_type in self.color_types:
            if color_type == self.selected_color_type.get():
                continue  # Skip the selected color type
            
            converted_values = self.get_converted_values(color_type)
            label_text = self.get_label_text(color_type, converted_values)
            label = customtkinter.CTkLabel(self.output_container, text=label_text)
            label.pack(padx=10, pady=10)

    def get_converted_values(self, color_type):
        if color_type == "RGB":
            return self.rgb_values
        elif color_type == "HEX":
            return self.hex_value
        elif color_type == "CMYK":
            return self.cmyk_values
        elif color_type == "HSL":
            return self.hsl_values
        elif color_type == "HSV":
            return self.hsv_values

    def get_label_text(self, color_type, values):
        if color_type == "RGB":
            return f"{color_type}: {round(values[0])}, {round(values[1])}, {round(values[2])}"
        elif color_type == "HEX":
            return f"{color_type}: {values}"
        elif color_type == "CMYK":
            return f"{color_type}: {round(values[0]*100)}, {round(values[1]*100)}, {round(values[2]*100)}, {round(values[3]*100)}"
        elif color_type == "HSL":
            return f"{color_type}: {round(values[0])}, {round(values[1])}, {round(values[2])}"
        elif color_type == "HSV":
            return f"{color_type}: {round(values[0])}, {round(values[1])}, {round(values[2])}"