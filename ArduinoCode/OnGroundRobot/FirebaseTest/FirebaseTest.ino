#include "FirebaseESP8266.h"
#include <ESP8266WiFi.h>

#define FIREBASE_HOST "https://synopsys2020-1.firebaseio.com/"  //Change to your Firebase RTDB project ID e.g. Your_Project_ID.firebaseio.com
#define FIREBASE_AUTH "AIzaSyBBFze3rkgjPBwEkno8ZFOuHZLCWhbXstk" //Change to your Firebase RTDB secret password
#define WIFI_SSID "NETGEAR45"
#define WIFI_PASSWORD "biggerbrother"

//Define Firebase Data objects
FirebaseData firebaseData1;
FirebaseData firebaseData2;

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

    if (!Firebase.beginStream(firebaseData1, path + "/" + nodeID))
    {
        Serial.println("Could not begin stream");
        Serial.println("REASON: " + firebaseData1.errorReason());
        Serial.println();
    }
    else {
      Serial.println("?");
    }
}

void loop()
{
    if (!Firebase.readStream(firebaseData1))
    {
        Serial.println();
        Serial.println("Can't read stream data");
        Serial.println("REASON: " + firebaseData1.errorReason());
        Serial.println();
    }

    if (firebaseData1.streamTimeout())
    {
        Serial.println();
        Serial.println("Stream timeout, resume streaming...");
        Serial.println();
    }

    if (firebaseData1.streamAvailable())
    {
        if (firebaseData1.dataType() == "boolean")
        {
            if (firebaseData1.boolData())
                Serial.println("Set " + nodeID + " to High");
            else
                Serial.println("Set " + nodeID + " to Low");
        }
    }

    
}
