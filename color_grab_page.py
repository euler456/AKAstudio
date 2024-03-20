from customtkinter import CTkFrame, CTkCanvas, CTkLabel, CTkButton
import cv2
import tkinter
from PIL import Image, ImageTk

class ColorGrabPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Create a canvas to display the video feed
        self.canvas = CTkCanvas(self, width=400, height=400)
        self.canvas.pack(pady=10, padx=10)

        # Button to navigate to Home page
        self.home_button = CTkButton(self, text="Go to Home", command=self.parent.open_home_page)
        self.home_button.place(relx = 0.5, rely=0.8, anchor=tkinter.CENTER)

        # Button to start capturing video
        self.start_button = CTkButton(self, text="Start Camera", command=self.start_camera)
        self.start_button.pack()

        # Button to stop capturing video
        self.stop_button = CTkButton(self, text="Stop Camera", command=self.stop_camera)
        self.stop_button.pack()

        # Button to close the camera
        self.close_button = CTkButton(self, text="Close App", command=self.close_app)
        self.close_button.pack()

        # Capture video flag
        self.capture_video_flag = False

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

    def close_app(self):
        # Close the camera
        self.stop_camera()
        self.parent.destroy()

    def capture_video(self):
        if self.capture_video_flag:
            # Read and display video frames until the user closes the window
            ret, frame = self.cap.read()
            if ret:
                # OpenCV uses BGR color order, we need to convert it to RGB for displaying with Tkinter
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame to fit the canvas
                frame_resized = cv2.resize(frame_rgb, (400, 400))

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
