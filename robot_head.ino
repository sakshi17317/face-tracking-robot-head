#include <Servo.h>

Servo pan;
Servo tilt;

int panAngle = 90;
int tiltAngle = 90;

void setup() {
  Serial.begin(9600);

  pan.attach(9);   // bottom servo
  tilt.attach(10); // top servo

  pan.write(panAngle);
  tilt.write(tiltAngle);
}

void loop() {

  if (Serial.available() > 0) {

    String data = Serial.readStringUntil('\n');

    int commaIndex = data.indexOf(',');

    if (commaIndex != -1) {

      panAngle = data.substring(0, commaIndex).toInt();
      tiltAngle = data.substring(commaIndex + 1).toInt();

      panAngle = constrain(panAngle, 0, 180);
      tiltAngle = constrain(tiltAngle, 0, 180);

      pan.write(panAngle);
      tilt.write(tiltAngle);
    }
  }
}



