import customtkinter as ctk
from customtkinter import CTkFrame, CTkCanvas, CTkLabel, CTkButton
import cv2
from PIL import Image, ImageTk
import tkinter as tk


class ColorGrabPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        ctk.set_appearance_mode("system")
        ctk.set_appearance_mode("dark")
        # Create a canvas to display the video feed
        self.canvas = CTkCanvas(self, width=640, height=470)
        self.canvas.pack(pady=10, padx=10)

        # Create a frame to hold color information
        color_info_frame = CTkFrame(self)
        color_info_frame.pack(pady=10)

        # Create labels to display color information
        self.color_label = CTkLabel(color_info_frame, text="Click on the canvas to grab color", font=("Helvetica", 14, "bold"))
        self.color_label.pack()

        self.rgb_label = CTkLabel(color_info_frame, text="RGB: ", font=("Helvetica", 12))
        self.rgb_label.pack()

        self.hex_label = CTkLabel(color_info_frame, text="HEX: ", font=("Helvetica", 12))
        self.hex_label.pack()

        self.cmyk_label = CTkLabel(color_info_frame, text="CMYK: ", font=("Helvetica", 12))
        self.cmyk_label.pack()

        self.hsl_label = CTkLabel(color_info_frame, text="HSL: ", font=("Helvetica", 12))
        self.hsl_label.pack()

        self.hsv_label = CTkLabel(color_info_frame, text="HSV: ", font=("Helvetica", 12))
        self.hsv_label.pack()

        # Bind mouse click event to canvas
        self.canvas.bind("<Button-1>", self.get_color)

        # Create a frame to hold control buttons
        control_frame = CTkFrame(self)
        control_frame.pack(pady=10)

        # Button to navigate to Home page
        self.home_button = CTkButton(control_frame, text="Go to Home", command=self.parent.open_home_page, font=("Helvetica", 12))
        self.home_button.pack(side="left", padx=10)

        # Button to start capturing video
        self.start_button = CTkButton(control_frame, text="Start Camera", command=self.start_camera, font=("Helvetica", 12))
        self.start_button.pack(side="left", padx=10)

        # Button to stop capturing video
        self.stop_button = CTkButton(control_frame, text="Stop Camera", command=self.stop_camera, font=("Helvetica", 12))
        self.stop_button.pack(side="left", padx=10)

        # Capture video flag
        self.capture_video_flag = False

    def get_color(self, event):
        x, y = event.x, event.y
        # Get the color at the clicked point
        color = self.get_pixel_color(x, y)
        if color is not None:
            # Update the color label with the color information
            self.color_label.configure(text=f"The color at ({x}, {y}) is ")
            
            # Calculate and display other color representations
            rgb = color
            hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
            cmyk = self.rgb_to_cmyk(rgb)
            hsl = self.rgb_to_hsl(rgb)
            hsv = self.rgb_to_hsv(rgb)
            
            self.rgb_label.configure(text=f"RGB: {rgb}")
            self.hex_label.configure(text=f"HEX: {hex_color}")
            self.cmyk_label.configure(text=f"CMYK: {cmyk}")
            self.hsl_label.configure(text=f"HSL: {hsl}")
            self.hsv_label.configure(text=f"HSV: {hsv}")

    def rgb_to_hsl(self, rgb):
        r, g, b = [x / 255.0 for x in rgb]
        max_color = max(r, g, b)
        min_color = min(r, g, b)
        delta = max_color - min_color

        # Calculate hue
        if delta == 0:
            h = 0
        elif max_color == r:
            h = 60 * (((g - b) / delta) % 6)
        elif max_color == g:
            h = 60 * (((b - r) / delta) + 2)
        else:
            h = 60 * (((r - g) / delta) + 4)

        # Calculate lightness
        l = (max_color + min_color) / 2

        # Calculate saturation
        if delta == 0:
            s = 0
        else:
            s = delta / (1 - abs(2 * l - 1))

        return round(h), round(s * 100), round(l * 100)

    def rgb_to_hsv(self, rgb):
        r, g, b = [x / 255.0 for x in rgb]
        max_color = max(r, g, b)
        min_color = min(r, g, b)
        delta = max_color - min_color

        # Calculate hue
        if delta == 0:
            h = 0
        elif max_color == r:
            h = 60 * (((g - b) / delta) % 6)
        elif max_color == g:
            h = 60 * (((b - r) / delta) + 2)
        else:
            h = 60 * (((r - g) / delta) + 4)

        # Calculate saturation
        if max_color == 0:
            s = 0
        else:
            s = delta / max_color

        # Calculate value
        v = max_color

        return round(h), round(s * 100), round(v * 100)

    def get_pixel_color(self, x, y):
        if hasattr(self, 'cap'):
            ret, frame = self.cap.read()
            if ret:
                # Convert frame to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Get dimensions of the frame
                frame_height, frame_width, _ = frame_rgb.shape
                # Check if coordinates are within bounds
                if 0 <= x < frame_width and 0 <= y < frame_height:
                    # Get color of the pixel at (x, y)
                    color = frame_rgb[y, x]
                    return color
        return None

    def start_camera(self):
        if not self.capture_video_flag:
            # Start capturing video
            self.capture_video_flag = True
            self.initialize_camera()
            self.capture_video()

    def stop_camera(self):
        if self.capture_video_flag:
            # Stop capturing video
            self.capture_video_flag = False
            self.release_camera()

    def capture_video(self):
        if self.capture_video_flag:
            # Read and display video frames until the user closes the window
            ret, frame = self.cap.read()
            if ret:
                # OpenCV uses BGR color order, we need to convert it to RGB for displaying with Tkinter
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit the canvas
                frame_resized = cv2.resize(frame_rgb, (640, 470))

                # Convert the frame to a format suitable for displaying in a Tkinter Canvas
                img = Image.fromarray(frame_resized)
                img = ImageTk.PhotoImage(image=img)

                # Update the canvas with the new frame
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

                # Hold a reference to the image to prevent it from being garbage collected
                self.canvas.img = img

                # Schedule the next frame capture
                self.after(10, self.capture_video)

    def initialize_camera(self):
        # Initialize camera
        self.cap = cv2.VideoCapture(0)

    def release_camera(self):
        # Release the camera
        if hasattr(self, 'cap'):
            self.cap.release()

    def cleanup(self):
        # Call cleanup when leaving the page
        self.release_camera()
    
    def rgb_to_cmyk(self, rgb):
        r, g, b = rgb
        c = 1 - (r / 255)
        m = 1 - (g / 255)
        y = 1 - (b / 255)
        k = min(c, m, y)
        if k == 1:
            return 0, 0, 0, 1
        c = (c - k) / (1 - k)
        m = (m - k) / (1 - k)
        y = (y - k) / (1 - k)
        return round(c, 2), round(m, 2), round(y, 2), round(k, 2)
