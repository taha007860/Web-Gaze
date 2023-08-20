import cv2
import mediapipe as mp
import pygame
import pyautogui
import numpy as np

# Initialize MediaPipe and Pygame
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
pygame.init()

# Set magnification factor and band height
magnification = 3
band_height = pyautogui.size()[1] * 0.1
band_width = pyautogui.size()[0] * 0.1  # Added band_width for x-direction tracking

# Create Pygame window for magnified band
window = pygame.display.set_mode((band_width * magnification, band_height * magnification))  # Adjusted window size for 2D tracking

def magnify_screen(x_position, y_position):
    # Capture screenshot and magnify band at gaze position
    screenshot = pyautogui.screenshot()
    screenshot_pygame = pygame.image.fromstring(screenshot.tobytes(), screenshot.size, screenshot.mode)
    magnified = pygame.transform.scale(screenshot_pygame, (screenshot.size[0] * magnification, screenshot.size[1] * magnification))
    band = magnified.subsurface((x_position * magnification, y_position * magnification, band_width * magnification, band_height * magnification))  # Adjusted subsurface for 2D tracking
    return band

# Start webcam capture
cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.7, min_tracking_confidence=0.7) as face_mesh:  # Increased confidence values for more sensitivity
    initial_nose_position = None  # To hold the initial nose position
    while cap.isOpened():
        ret, frame = cap.read()

        # Define ROI
        height, width, _ = frame.shape
        roi_x = width // 4
        roi_y = height // 2
        roi_width = width // 2
        roi_height = height // 2
        roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # Convert the ROI to RGB before processing
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        # Flip the image horizontally for a later selfie-view display
        roi_rgb = cv2.flip(roi_rgb, 1)

        # Process the ROI and get the results
        results = face_mesh.process(roi_rgb)

        # Draw the face landmarks on the ROI
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(roi_rgb, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

                # Get nose position (nose tip)
                nose_tip = face_landmarks.landmark[4]
                if initial_nose_position is None:
                    initial_nose_position = (nose_tip.x, nose_tip.y)

                # Calculate distance moved from initial position
                distance_moved = ((nose_tip.x - initial_nose_position[0])**2 + (nose_tip.y - initial_nose_position[1])**2)**0.5

                # If distance moved is above a certain threshold, update gaze position
                if distance_moved > 0.02:  # Made it 5 times more sensitive to movement
                    gaze_position_x = (nose_tip.x * roi_width + roi_x) * pyautogui.size()[0] / width  # Adjusted for ROI
                    gaze_position_y = (nose_tip.y * roi_height + roi_y) * pyautogui.size()[1] / height  # Adjusted for ROI

                    # Magnify screen at gaze position
                    band = magnify_screen(gaze_position_x, gaze_position_y)
                    window.blit(band, (0, 0))
                    pygame.display.flip()

        # Display the ROI with landmarks and bounding box in a window
        cv2.imshow('ROI with landmarks', roi_rgb)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
