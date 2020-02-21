#include <ESP8266WiFi.h>
#include "FirebaseESP8266.h"
FirebaseData firebaseData;

void setup() {
  Serial.begin(115200);
  connectWifi();
  Firebase.begin("https://synopsys2020-1.firebaseio.com/", "AIzaSyBBFze3rkgjPBwEkno8ZFOuHZLCWhbXstk");
  Serial.println("working");
}

void loop() {
  Serial.println("reading");
  if (Firebase.getBool(firebaseData, "/OnGroundRobot/Send/LightOn")) {
    Serial.println("reading");
      bool val = firebaseData.boolData();
      if (val) {
        Serial.println("Light On");
      }
      else {
        Serial.println("Light Off");
      
      }
  }

}

void connectWifi() {
  // Let us connect to WiFi
  WiFi.begin("NETGEAR45", "biggerbrother");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(".......");
  Serial.println("WiFi Connected....IP Address:");
  Serial.println(WiFi.localIP());
}
