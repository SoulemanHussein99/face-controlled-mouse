# Face Controlled Mouse (Computer Vision)

A real-time human-computer interaction system that allows controlling the mouse using face movement and eye blinking.

---

## Features

- Move mouse using face position
- Left click using eye blink 
- Right click using eye blink 
- Real-time face tracking
- Eye landmark detection using dlib
- Smooth cursor control with screen mapping

---

## How It Works

1. Webcam captures live video  
2. Face position is detected  
3. Face coordinates are mapped to screen size  
4. Mouse moves according to face movement  
5. Eye landmarks are detected using dlib  
6. Eye blinking triggers mouse clicks  

---

## Technologies Used

- Python 
- OpenCV (cv2)
- dlib (facial landmarks)
- PyAutoGUI (mouse control)
