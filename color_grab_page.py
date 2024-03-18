import customtkinter as tk
from customtkinter import CTkFrame, CTkCanvas ,CTkLabel, CTkButton

import cv2
from PIL import Image, ImageTk

class ColorGrabPage(CTkFrame):
    def __init__(self, parent, show_page1_callback):
        super().__init__(parent)

        # Create a canvas to display the video feed
        self.canvas = CTkCanvas(self, width=200, height=200)
        self.canvas.pack(pady=10, padx=10)

        # Button to navigate to Home page
        self.home_button = CTkButton(self, text="Go to Home", command=show_page1_callback)
        self.home_button.pack()

        # Button to start capturing video
        start_button = CTkButton(self, text="Start Camera", command=self.start_camera)
        start_button.pack()

        # Capture video flag
        self.capture_video_flag = False

    def start_camera(self):
        # Start capturing video
        self.capture_video_flag = True
        self.initialize_camera()
        self.capture_video()

    def capture_video(self):
        if self.capture_video_flag:
            # Read and display video frames until the user closes the window
            ret, frame = self.cap.read()
            if ret:
                # OpenCV uses BGR color order, we need to convert it to RGB for displaying with Tkinter
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit the canvas
                frame_resized = cv2.resize(frame_rgb, (200, 200))

                # Convert the frame to a format suitable for displaying in a Tkinter Canvas
                img = Image.fromarray(frame_resized)
                img = ImageTk.PhotoImage(image=img)

                # Update the canvas with the new frame
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

                # Hold a reference to the image to prevent it from being garbage collected
                self.canvas.img = img

                # Schedule the next frame capture
                self.after(10, self.capture_video)

    def go_to_home(self):
        # Stop capturing video and go to the Home page
        from home_page import HomePage
        self.capture_video_flag = False
        self.release_camera()
        self.controller.show_frame(HomePage)

    def initialize_camera(self):
        # Initialize camera
        self.cap = cv2.VideoCapture(0)

    def release_camera(self):
        # Release the camera
        if hasattr(self, 'cap'):
            self.cap.release()

    def setup(self):
        # Call setup when the page is shown
        self.start_camera()

    def cleanup(self):
        # Call cleanup when leaving the page
        self.release_camera()
