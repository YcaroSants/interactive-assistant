void setup() {
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char comando = Serial.read();
    if (comando == 'L') {
      digitalWrite(10, HIGH); // Liga o LED
    } else if (comando == 'D') {
      digitalWrite(10, LOW); // Desliga o LED
    }
  }
}
