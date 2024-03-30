

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(trigPin, OUTPUT); // Set trigger pin as output
  pinMode(echoPin, INPUT); // Set echo pin as input
}

void loop() {
  long duration, distance;
  
  // Clear trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Set trigger pin high for 10 microseconds to trigger the ultrasonic sensor
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Measure the duration of the pulse received
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate distance using the speed of sound (343 meters/second)
  distance = duration * 0.0343 / 2; // Divide by 2 as the sound travels back and forth
  
  // Print only integer values of distance
  Serial.println(distance);
  
  delay(100); // Wait for 100 milliseconds before taking the next measurement
}
