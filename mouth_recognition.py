import cv2
import dlib
import numpy as np


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('C:/Users/asus/AppData/Local/Programs/Python/Python39/shape_predictor_68_face_landmarks_GTX.dat')

def distance(p1, p2):
    return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def apply_filter(frame, landmarks):
    left_point = (landmarks.part(48).x, landmarks.part(48).y)
    right_point = (landmarks.part(54).x, landmarks.part(54).y)

    mouth_width = distance(left_point, right_point)

    if mouth_width > 30: 
        cv2.circle(frame, left_point, 3, (0, 0, 255), -1)
        cv2.circle(frame, right_point, 3, (0, 0, 255), -1)

        frame = cv2.GaussianBlur(frame, (15, 15), 0)

    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)

            frame = apply_filter(frame, landmarks)

        cv2.imshow('Mouth Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
