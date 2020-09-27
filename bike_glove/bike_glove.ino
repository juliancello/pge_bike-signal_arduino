// Circuit Playground Bike Glove - Right Turn Animation
// 
// Original author: Carter Nelson
// MIT License (https://opensource.org/lincenses/MIT)

#include <Adafruit_CircuitPlayground.h>

#define BRIGHTNESS      255
#define TURN_COLOR      0xFF7E00
#define TURN_OFF        0x000000
#define ANIM_DELAY      100
#define THRESHOLD       -5
#define REST_THRESHOLD  5
// threshold for both turns and resting position
// TURN_COLOR is SAE/ECE Amber
// arrays are zero indexed
// lights chase and remain on, then chase off

const int right_order[] = {7, 8, 6, 9, 5, 0, 4, 3, 1, 2}; // start to end window = 1, 2, 2, 2, 2, 1
const int left_order[] = {0, 9, 1, 8, 2, 7, 3, 6, 4, 5}; // s.t.e.w. = 5 2s

void rightTurnAnimation() {
  // start clean with neopixels off
  CircuitPlayground.clearPixels();

  // turn on NeoPixels in a chase pattern
  for (int i = 0; i < 10; i++) { // should only run 6 times
    if (i == 0 || i == 9) {
      CircuitPlayground.setPixelColor(right_order[i], TURN_COLOR);
    } else {
      CircuitPlayground.setPixelColor(right_order[i], TURN_COLOR);
      CircuitPlayground.setPixelColor(right_order[i+1], TURN_COLOR);
      i++;
    }
    delay(ANIM_DELAY);
  }
  for (int i = 0; i < 10; i++) { // should only run 6 times
    if (i == 0 || i == 9) {
      CircuitPlayground.setPixelColor(right_order[i], TURN_OFF);
    } else {
      CircuitPlayground.setPixelColor(right_order[i], TURN_OFF);
      CircuitPlayground.setPixelColor(right_order[i+1], TURN_OFF);
      i++;
    }
    delay(ANIM_DELAY);
  }
}

void leftTurnAnimation(){
  // start clean with neopixels off
  CircuitPlayground.clearPixels();

  // turn on NeoPixels in a chase pattern
  for (int i = 0; i < 10; i++) { // should only run 5 times
    CircuitPlayground.setPixelColor(left_order[i], TURN_COLOR);
    CircuitPlayground.setPixelColor(left_order[i+1], TURN_COLOR);
    delay(ANIM_DELAY);
    i++;
  }
  for (int i = 0; i < 10; i++) { // should only run 5 times
    CircuitPlayground.setPixelColor(left_order[i], TURN_OFF);
    CircuitPlayground.setPixelColor(left_order[i+1], TURN_OFF);
    delay(ANIM_DELAY);
    i++;
  }

}

void setup() {
  CircuitPlayground.begin(); // removed BRIGHTNESS as an argument
}

void loop() {
  // check slide switch position
  if (CircuitPlayground.slideSwitch()) {
    // check for hand up or down 
    if (CircuitPlayground.motionZ() > REST_THRESHOLD) {
      // do nothing
    } else {
    
      // check for right turn
      if (CircuitPlayground.motionY() < THRESHOLD) {
        rightTurnAnimation();
      // check for left turn
      } else if (CircuitPlayground.motionX() < THRESHOLD) {
        leftTurnAnimation();
      }
    }
    delay(500);
  }
}
