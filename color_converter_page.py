import tkinter
import customtkinter

class ColorConverterPage(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Label for the page title
        label = customtkinter.CTkLabel(self, text="Color Converter Page")
        label.pack(pady=10, padx=10)
        
        # Dropdown menu to select color value type
        self.color_types = ["RGB", "HEX", "CMYK", "HSL", "HSV"]
        self.selected_color_type = customtkinter.StringVar(value=self.color_types[0])
        type_selector = customtkinter.CTkOptionMenu(self, variable=self.selected_color_type,values=self.color_types, command=self.update_inputs)
        type_selector.pack(pady=5)
        
        # Container frame for input fields
        self.input_container = customtkinter.CTkFrame(self)
        self.input_container.pack(pady=10)
        
        # Button to navigate to Home page
        from home_page import HomePage
        self.home_button = customtkinter.CTkButton(self, text="Go to Home", command=self.parent.open_home_page)
        self.home_button.place(relx = 0.5, rely=0.8, anchor=tkinter.CENTER)
        
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
            label = customtkinter.CTkLabel(self.input_container, text=label_text)
            label.pack(side="left")
            entry = customtkinter.CTkEntry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hex_input(self):
        # Add 1 input field for HEX value
        label = customtkinter.CTkLabel(self.input_container, text="HEX:")
        label.pack(side="left")
        entry = customtkinter.CTkEntry(self.input_container)
        entry.pack(side="left", padx=5)
    
    def add_cmyk_inputs(self):
        # Add 4 input fields for CMYK values
        for label_text in ["C:", "M:", "Y:", "K:"]:
            label = customtkinter.CTkLabel(self.input_container, text=label_text)
            label.pack(side="left")
            entry = customtkinter.CTkEntry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hsl_inputs(self):
        # Add 3 input fields for HSL values
        for label_text in ["H:", "S:", "L:"]:
            label = customtkinter.CTkLabel(self.input_container, text=label_text)
            label.pack(side="left")
            entry = customtkinter.CTkEntry(self.input_container)
            entry.pack(side="left", padx=5)
    
    def add_hsv_inputs(self):
        # Add 3 input fields for HSV values
        for label_text in ["H:", "S:", "V:"]:
            label = customtkinter.CTkLabel(self.input_container, text=label_text)
            label.pack(side="left")
            entry = customtkinter.CTkEntry(self.input_container)
            entry.pack(side="left", padx=5)
