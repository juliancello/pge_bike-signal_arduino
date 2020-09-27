// Circuit Playground Bike Glove - Plot Hand Position
//
// Adapted by: Julian Kosanovic
// Original author: Carter Nelson
//

#include <Adafruit_CircuitPlayground.h>
// xyz = brg
// drop rest 1: -7.5, -4, 5
// drop rest 2: -3, -2, 9
// left turn 1: -9, 0, 0
// left turn 2: -6, 6, 0
float X, Y, Z;

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();

}

void loop() {
  X = CircuitPlayground.motionX();
  Y = CircuitPlayground.motionY();
  Z = CircuitPlayground.motionZ();

  Serial.print(X);
  Serial.print(",");
  Serial.print(Y);
  Serial.print(",");
  Serial.println(Z);

  delay(100);

}
