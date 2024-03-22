import customtkinter as ctk
from customtkinter import CTkFrame, CTkCanvas, CTkLabel, CTkButton
import cv2
from PIL import Image, ImageTk
import tkinter as tk

class ColorGrabPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Create a canvas to display the video feed
        self.canvas = CTkCanvas(self, width=640, height=470)
        self.canvas.pack(pady=10, padx=10)

        # Create a label to display color information
        self.color_label = CTkLabel(self, text="Click on the canvas to grab color")
        self.color_label.pack()

        # Bind mouse click event to canvas
        self.canvas.bind("<Button-1>", self.get_color)

        # Button to navigate to Home page
        self.home_button = CTkButton(self, text="Go to Home", command=self.parent.open_home_page)
        self.home_button.pack()

        # Button to start capturing video
        self.start_button = CTkButton(self, text="Start Camera", command=self.start_camera)
        self.start_button.pack()

        # Button to stop capturing video
        self.stop_button = CTkButton(self, text="Stop Camera", command=self.stop_camera)
        self.stop_button.pack()

        # Capture video flag
        self.capture_video_flag = False

    def get_color(self, event):
        x, y = event.x, event.y
        # Get the color at the clicked point
        color = self.get_pixel_color(x, y)
        if color is not None:
            # Update the color label with the color information
            self.color_label.configure(text=f"The color at ({x}, {y}) is {color}")

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
