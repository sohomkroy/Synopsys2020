#include "FirebaseESP8266.h"
#include <ESP8266WiFi.h>

#define FIREBASE_HOST "https://synopsys2020-1.firebaseio.com/"  //Change to your Firebase RTDB project ID e.g. Your_Project_ID.firebaseio.com
#define FIREBASE_AUTH "GDexoGKOuxikUzvNUU0QW1m01KqfvWToNYCfEXp9" //Change to your Firebase RTDB secret password
#define WIFI_SSID "NETGEAR45"
#define WIFI_PASSWORD "biggerbrother"

//Define Firebase Data objects
FirebaseData sent_data;

String path = "/Nodes";
String nodeID = "Node2";      //This is this node ID to receive control
String otherNodeID = "Node1"; //This is other node ID to control




void setup()
{

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

    if (!Firebase.beginStream(sent_data, "OnGroundRobot/Send"))
    {
        Serial.println("Could not begin stream");
        Serial.println("REASON: " + sent_data.errorReason());
        Serial.println();
    }
    else {
      Serial.println("Connected");
    }
    
    
}

void loop()
{
    if (!Firebase.readStream(sent_data))
    {
        Serial.println();
        Serial.println("Can't read stream data");
        Serial.println("REASON: " + sent_data.errorReason());
        Serial.println();
    }

    if (sent_data.streamTimeout())
    {
        Serial.println();
        Serial.println("Stream timeout, resume streaming...");
        Serial.println();
    }

    if (sent_data.streamAvailable())
    { 
      String data = sent_data.jsonString();
      data.remove(0, 20);
      String f = data.substring(0, data.indexOf(','));
      data.remove(0, data.indexOf(',')+1);

      String t= data.substring(0, data.indexOf(',')-1);
      data.remove(0, data.indexOf(',')+11);

      data.remove(data.length()-1, data.length());

      Serial.println(f+"  "+t);
      Serial.println(data);
      
    }
   
}
