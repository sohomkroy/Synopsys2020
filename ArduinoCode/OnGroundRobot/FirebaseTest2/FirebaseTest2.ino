#include "FirebaseESP8266.h"
#include <ESP8266WiFi.h>

#define FIREBASE_HOST "https://synopsys2020-1.firebaseio.com/"  //Change to your Firebase RTDB project ID e.g. Your_Project_ID.firebaseio.com
#define FIREBASE_AUTH "GDexoGKOuxikUzvNUU0QW1m01KqfvWToNYCfEXp9" //Change to your Firebase RTDB secret password
#define WIFI_SSID "NETGEAR45"
#define WIFI_PASSWORD "biggerbrother"

FirebaseJson json;
FirebaseData receivedData;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

    Serial.println();
    Serial.println();

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("Connecting to Wi-Fi");
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(300);
    }
    Serial.println();
    Serial.print("Connected with IP: ");
    Serial.println(WiFi.localIP());
    Serial.println();

    Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
    Firebase.reconnectWiFi(true);

}

void loop() {
  // put your main code here, to run repeatedly:
  json.set("parent_001", "parent 001 text");
  json.set("parent_002", "parent 002 text");

  Firebase.setJSON(receivedData, "/test/append", json);

}
