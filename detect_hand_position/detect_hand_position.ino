// Circuit Playground Bike Glove - Hand Position Detection
//
// Adapted by: Julian Kosanovic
// Original author: Carter Nelson
//

#include <Adafruit_CircuitPlayground.h>
// Resting hand is X, Y = 0, Z = 9
// Left turn is X = 9, Y, Z = 0
// Right turn is X = 0, Y = 9, Z = 0
// xyz = brg
// drop rest 1: -7.5, -4, 5
// drop rest 2: -3, -2, 9
// left turn 1: -9, 0, 0
// left turn 2: -6, 6, 0
// test tolerance +/- 2
#define THRESHOLD 5 //threshold for both turns and resting position

void setup() {
  Serial.begin(9600);

  CircuitPlayground.begin();
}

void loop() {
  // check for hand up or down
  if (CircuitPlayground.motionZ() > THRESHOLD) {
    Serial.println("HAND DOWN");
  } else {

    // check for right turn
    if (CircuitPlayground.motionY() > THRESHOLD) {
      Serial.println("RIGHT TURN");
      
    } else if (CircuitPlayground.motionX() > THRESHOLD) {
      Serial.println("LEFT TURN");
    }
  }
  delay(500);
}
