import cv2
import mediapipe as mp
import serial
import time

# CHANGE THIS if needed
arduino = serial.Serial("COM3", 9600)
time.sleep(2)

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)

    h, w, _ = frame.shape

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box

            cx = int((bbox.xmin + bbox.width / 2) * w)
            cy = int((bbox.ymin + bbox.height / 2) * h)

            pan = int((cx / w) * 180)
            tilt = int((cy / h) * 180)

            print("Sending:", pan, tilt)

            arduino.write(f"{pan},{tilt}\n".encode())

    cv2.imshow("Face Tracking Robot Head", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

