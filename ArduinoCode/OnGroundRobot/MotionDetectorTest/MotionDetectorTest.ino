
const int digitalPin = 5;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    Serial.println("k");

    pinMode(digitalPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
   
   Serial.println(digitalRead(digitalPin));
   delay(100);
}
