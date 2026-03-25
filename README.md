# 🤖 Face Tracking Robot Head

A real-time face tracking robot head built using **Arduino Uno, Python, OpenCV, and MediaPipe**.
This robot detects your face using a camera and moves a pan-tilt mechanism (servo motors) to follow your head movement.

---

## 🚀 Features

* 👀 Real-time face detection using MediaPipe
* 🔄 Pan (left/right) movement using servo motor
* ⬆️⬇️ Tilt (up/down) movement using servo motor
* ⚡ Fast communication between Python and Arduino
* 🎯 Smooth and responsive tracking

---

## 🧰 Components Used

* Arduino Uno
* 2x Servo Motors (SG90 / MG90S)
* Pan-Tilt Bracket
* USB Cable
* Computer / Laptop with Python
* Webcam (built-in or external)

---

## 💻 Technologies Used

* Python
* OpenCV
* MediaPipe
* PySerial
* Arduino IDE

---

## ⚙️ How It Works

1. 📷 Camera captures live video
2. 🧠 MediaPipe detects the face
3. 📍 Face position is converted into coordinates
4. 📡 Python sends angle data to Arduino via Serial
5. 🤖 Arduino moves the servo motors
6. 🎯 Robot head follows your face

---

## 🛠️ Setup Instructions

### 1️⃣ Install Python Libraries

```bash
pip install opencv-python mediapipe pyserial
```

---

### 2️⃣ Upload Arduino Code

Upload the Arduino `.ino` file to your Arduino Uno using Arduino IDE.

Make sure:

* Servo 1 → Pin 9 (Pan)
* Servo 2 → Pin 10 (Tilt)

---

### 3️⃣ Run Python Script

```bash
python face_to_arduino.py
```

---

## 🎮 How To Use

* Move your face left → robot turns left
* Move your face right → robot turns right
* Move your face up → robot looks up
* Move your face down → robot looks down

---

## 📁 Project Structure

```
face-tracking-robot-head/
│
├── face_to_arduino.py   # Python face tracking code
├── robot_head.ino       # Arduino servo control code
└── README.md            # Project documentation
```

---


## 🧠 Future Improvements

* Smoother servo movement (filtering)
* Better face tracking accuracy
* Wireless control (Bluetooth / WiFi)
* Add object tracking
* Mount camera on robot

---

## 🙌 Author

**Sakshi**

Made with ❤️ using Arduino and Python

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

