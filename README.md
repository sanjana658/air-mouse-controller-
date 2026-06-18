# Air Mouse 🖱️✋

A real-time Computer Vision application that enables touch-free mouse control using hand gestures.

The system uses OpenCV and MediaPipe to detect and track hand landmarks through a webcam. The index finger controls cursor movement, while a pinch gesture between the thumb and index finger performs mouse clicks. Cursor smoothing is implemented to provide a more stable and natural user experience.

## Features

* Real-time hand tracking
* Cursor movement using index finger
* Pinch gesture for mouse click
* Cursor smoothing for stability
* Touch-free Human Computer Interaction (HCI)
* Real-time webcam processing

## Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* PyAutoGUI

## How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Index finger tip (Landmark 8) is tracked.
4. Finger coordinates are mapped to screen coordinates.
5. Cursor moves according to finger movement.
6. Thumb and index finger distance is monitored.
7. A pinch gesture triggers a mouse click.

## Project Workflow

Webcam
↓
OpenCV
↓
MediaPipe Hand Tracking
↓
Landmark Detection
↓
Coordinate Mapping
↓
Cursor Movement
↓
Gesture Recognition
↓
Mouse Click Actions

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/air-mouse.git
```

Navigate to the project folder:

```bash
cd air-mouse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python air_mouse.py
```

## Controls

| Gesture                    | Action           |
| -------------------------- | ---------------- |
| Move Index Finger          | Move Cursor      |
| Touch Thumb + Index Finger | Left Click       |
| Press Q                    | Exit Application |

## Learning Outcomes

This project demonstrates:

* Computer Vision
* Hand Landmark Detection
* Coordinate Transformation
* Gesture Recognition
* Real-Time Video Processing
* Human Computer Interaction (HCI)
* System Automation

## Future Enhancements

* Right Click Gesture
* Double Click Gesture
* Scroll Gesture
* Drag and Drop Support
* Gesture-Based Shortcuts
* Multi-Hand Tracking

## Author

Sanjana Thanabalan

Artificial Intelligence & Data Science Student
