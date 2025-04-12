import cv2
import mediapipe as mp
from deepface import DeepFace
import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3

class EmotionGreeter:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

        # Video capture
        self.vid = cv2.VideoCapture(0)

        # Mediapipe hand detection
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)

        # Canvas for video
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), 
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Emotion label
        self.emotion_label = tk.Label(window, text="Show your palm", 
                                      font=("Arial", 16))
        self.emotion_label.pack()

        # Greeting label
        self.greeting_label = tk.Label(window, text="", font=("Arial", 16), fg="blue")
        self.greeting_label.pack()

        self.current_emotion = "Waiting..."

        # Update video frames
        self.delay = 15
        self.update_video()

        # Quit button
        self.btn_quit = tk.Button(window, text="Quit", width=10, 
                                  command=self.quit_app)
        self.btn_quit.pack()

    def detect_palm(self, frame):
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame for hand detection
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Check if palm is open (all fingers extended)
                if self.is_palm_open(hand_landmarks):
                    return True
        return False

    def is_palm_open(self, hand_landmarks):
        # Simple palm detection by checking finger tip y-coordinates
        tips = [
            hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP],
            hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP],
            hand_landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
            hand_landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP],
            hand_landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP]
        ]

        # Check if tips are spread out
        return all(tip.y < hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].y for tip in tips)

    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            # Detect palm
            if self.detect_palm(frame):
                try:
                    # Predict emotion when palm is open
                    result = DeepFace.analyze(
                        frame, 
                        actions=['emotion'], 
                        enforce_detection=False
                    )
                    self.current_emotion = result[0]['dominant_emotion']
                    self.display_greeting(self.current_emotion)
                except Exception as e:
                    self.current_emotion = "Detection Error"

            # Update emotion label
            self.emotion_label.config(text=f"Emotion: {self.current_emotion}")

            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update_video)

    def display_greeting(self, emotion):
        greetings = {
            "happy": "Welcome to Kalkini! We're thrilled to see your happiness!",
            "sad": "Welcome to Kalkini! Let us brighten your day with our innovations!",
            "angry": "Welcome to Kalkini! Let's find calmness together through technology!",
            "surprise": "Welcome to Kalkini! Our technology is full of surprises, isn't it?",
            "neutral": "Welcome to Kalkini! Discover the future of smart A.I. cameras!",
            "fear": "Welcome to Kalkini! Rest assured, you're in safe hands with us!",
            "disgust": "Welcome to Kalkini! Let us change that expression with our amazing products!"
        }
        
        greeting = greetings.get(emotion.lower(), "Hello there! Show your palm to see a greeting.")
        self.greeting_label.config(text=greeting)
        self.speak_greeting(greeting)

    def speak_greeting(self, greeting):
        self.tts_engine.say(greeting)
        self.tts_engine.runAndWait()

    def quit_app(self):
        self.vid.release()
        self.window.destroy()

# Create a window and pass it to EmotionGreeter
root = tk.Tk()
app = EmotionGreeter(root, "Emotion-Based Greeting")
root.mainloop()
