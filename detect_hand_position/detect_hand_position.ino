// Circuit Playground Bike Glove - Hand Position Detection
//
// Adapted by: Julian Kosanovic
// Original author: Carter Nelson
//

#include <Adafruit_CircuitPlayground.h>
// Resting hand is X, Y = 0, Z = 9
// Left turn is X = 9, Y, Z = 0
// Right turn is X = 0, Y = 9, Z = 0
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
