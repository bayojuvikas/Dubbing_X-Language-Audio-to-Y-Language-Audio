import cv2
from fer import FER
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

# Initialize the emotion detector
emotion_detector = FER(mtcnn=True)

# Function to map emotions to emoji image file paths
def get_emoji_image_path(emotion):
    emoji_dict = {
        "angry": r"C:\Users\umad3\emojis\angry.png",
        "sad": r"C:\Users\umad3\emojis\sad.png"
        # Add more emotions and paths as needed
    }
    return emoji_dict.get(emotion, r"C:\Users\umad3\emojis\neutral.png")

# Function to overlay emoji on frame
def overlay_emoji(frame, emoji_image_path, x, y, w, h):
    if not os.path.exists(emoji_image_path):
        print(f"Error: Emoji image not found at {emoji_image_path}")
        return

    emoji_img = cv2.imread(emoji_image_path, cv2.IMREAD_UNCHANGED)
    if emoji_img is None:
        print(f"Error: Could not load emoji image from path {emoji_image_path}")
        return

    emoji_img = cv2.resize(emoji_img, (w, h))
    
    # Ensure that the emoji image has an alpha channel (transparency)
    if emoji_img.shape[2] == 4:
        alpha_mask = emoji_img[:, :, 3] / 255.0
        for c in range(0, 3):
            frame[y:y+h, x:x+w, c] = (1 - alpha_mask) * frame[y:y+h, x:x+w, c] + alpha_mask * emoji_img[:, :, c]
    else:
        frame[y:y+h, x:x+w] = emoji_img

# Function to capture video frames and process emotions
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Detect emotions
        results = emotion_detector.detect_emotions(frame)

        # Draw bounding box and overlay emoji for each detected face
        for result in results:
            bounding_box = result["box"]
            emotions = result["emotions"]
            max_emotion = max(emotions, key=emotions.get)
            emoji_image_path = get_emoji_image_path(max_emotion)

            x, y, w, h = bounding_box
            overlay_emoji(frame, emoji_image_path, x, y, w, h)

        # Convert frame to image format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the image in the GUI
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    # Call update_frame again after 10 ms
    root.after(10, update_frame)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create the main window
root = tk.Tk()
root.title("Emotion Reader")

# Create a label to display the video frames
video_label = ttk.Label(root)
video_label.grid(row=0, column=0, padx=10, pady=10)

# Start capturing video frames
update_frame()

# Run the application
root.mainloop()

# Release the webcam
cap.release()
cv2.destroyAllWindows()
