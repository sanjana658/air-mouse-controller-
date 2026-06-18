import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import time

# Screen size
screen_width, screen_height = pyautogui.size()

# Safety feature
pyautogui.FAILSAFE = True

# MediaPipe Hands
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Cursor smoothing
prev_x = 0
prev_y = 0
smoothening = 7

# Click control
last_click_time = 0
click_delay = 0.5  # seconds

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index Finger Tip (8)
            index_tip = hand_landmarks.landmark[8]

            index_x = int(index_tip.x * w)
            index_y = int(index_tip.y * h)

            # Thumb Tip (4)
            thumb_tip = hand_landmarks.landmark[4]

            thumb_x = int(thumb_tip.x * w)
            thumb_y = int(thumb_tip.y * h)

            # Draw circles
            cv2.circle(
                frame,
                (index_x, index_y),
                12,
                (0, 255, 0),
                cv2.FILLED
            )

            cv2.circle(
                frame,
                (thumb_x, thumb_y),
                12,
                (255, 0, 0),
                cv2.FILLED
            )

            # Draw line between thumb and index
            cv2.line(
                frame,
                (thumb_x, thumb_y),
                (index_x, index_y),
                (255, 255, 0),
                3
            )

            # Cursor movement
            screen_x = np.interp(
                index_x,
                [0, w],
                [0, screen_width]
            )

            screen_y = np.interp(
                index_y,
                [0, h],
                [0, screen_height]
            )

            # Smooth cursor movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)

            prev_x = curr_x
            prev_y = curr_y

            # Distance for click
            distance = math.hypot(
                thumb_x - index_x,
                thumb_y - index_y
            )

            # Display distance
            cv2.putText(
                frame,
                f"Distance: {int(distance)}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            # Click gesture
            current_time = time.time()

            if distance < 35:

                cv2.putText(
                    frame,
                    "CLICK",
                    (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                if current_time - last_click_time > click_delay:
                    pyautogui.click()
                    last_click_time = current_time

    cv2.imshow("Air Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()