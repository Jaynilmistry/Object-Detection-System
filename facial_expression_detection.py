import cv2
import numpy as np
from deepface import DeepFace

# Load the pre-trained face detection model (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_facial_expression(image):
    """
    Detects facial expressions in an image.
    
    Parameters:
    - image (numpy array): The input image.
    
    Returns:
    - image (numpy array): The image with detected expressions drawn on it.
    - detected_expressions (list): A list of detected expressions with confidence scores.
    """
    detected_expressions = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face_roi = image[y:y + h, x:x + w]  # Extract the face region

        try:
            # Use DeepFace to analyze the face for emotion
            analysis = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            confidence = analysis[0]['emotion'][emotion]

            detected_expressions.append(f"{emotion.capitalize()} ({confidence:.2f}%)")

            color = (0, 255, 0)  # Green box
            # Increase box thickness from 2 to 3
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
            # Increase font scale from 0.6 to 1.0 and thickness from 2 to 3
            cv2.putText(image, f"{emotion.capitalize()} ({confidence:.2f}%)", 
                       (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)
        
        except Exception as e:
            detected_expressions.append("Error detecting expression")
    
    return image, detected_expressions
