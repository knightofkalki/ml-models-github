# Emotion-Based Greeting Application

Welcome to the **Emotion-Based Greeting Application**! This project leverages cutting-edge computer vision and emotion detection technologies to provide personalized greetings based on the user's facial expressions and hand gestures.

## Features
- **Emotion Detection:** Detects emotions such as happiness, sadness, anger, surprise, neutrality, fear, and disgust using DeepFace.
- **Hand Gesture Recognition:** Identifies if the user shows an open palm to trigger emotion analysis.
- **Text-to-Speech Greetings:** Delivers personalized greetings based on detected emotions using `pyttsx3`.
- **User-Friendly Interface:** Built with `Tkinter` for an intuitive and interactive user experience.

## Demo
The application displays a live video feed and recognizes emotions when an open palm is detected. It provides visual and auditory feedback with an emotion-specific greeting.

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - `OpenCV`: For real-time video processing
  - `Mediapipe`: For hand gesture detection
  - `DeepFace`: For facial emotion analysis
  - `Tkinter`: For the graphical user interface (GUI)
  - `PIL`: For handling video frames in the GUI
  - `pyttsx3`: For text-to-speech functionality

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

Install the required libraries by running the requirements.txt file:
```bash
pip install -r requirements.txt
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/NerdyBirdy69/stall-greeter-based-on-facial-emotions/
   cd emotion-greeting-app
   ```
2. Run the application:
   ```bash
   python emotion_greeter.py
   ```
3. Allow access to your webcam when prompted.
4. Show your palm to trigger emotion detection and enjoy personalized greetings!

## Code Overview
### `EmotionGreeter` Class
- **Initialization:**
  - Sets up the GUI, video capture, and text-to-speech engine.
  - Initializes Mediapipe for hand gesture detection.
- **Key Methods:**
  - `detect_palm`: Detects open palms using Mediapipe landmarks.
  - `update_video`: Updates the live video feed and triggers emotion detection.
  - `display_greeting`: Displays and speaks the greeting based on detected emotion.
  - `quit_app`: Releases resources and closes the application.

## Greetings Mapping
The application provides unique greetings based on the detected emotion, for example lets take a shop called "kalkini":
- **Happy:** "Welcome to Kalkini! We're thrilled to see your happiness!"
- **Sad:** "Welcome to Kalkini! Let us brighten your day with our innovations!"
- **Angry:** "Welcome to Kalkini! Let's find calmness together through technology!"
- **Surprise:** "Welcome to Kalkini! Our technology is full of surprises, isn't it?"
- **Neutral:** "Welcome to Kalkini! Discover the future of smart A.I. cameras!"
- **Fear:** "Welcome to Kalkini! Rest assured, you're in safe hands with us!"
- **Disgust:** "Welcome to Kalkini! Let us change that expression with our amazing products!"

## Future Enhancements
- Add support for multiple hands and multiple faces.
- Enhance emotion detection accuracy.
- Add multi-language support for greetings.

## Contribution
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
Special thanks to the creators of OpenCV, Mediapipe, and DeepFace for providing powerful tools that make this project possible.

---

Enjoy using the **Emotion-Based Greeting Application** and experience the power of AI-driven interactions!

