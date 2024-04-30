#define LED 2
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <WebSerial.h>
#include "TickTwo.h"
AsyncWebServer server(80);

void sendDataToWeb();
TickTwo dataDelay(sendDataToWeb, 5000); 
//Global Variable Declared here
String dataToSend = "pH=7&Turbidity=100&Temperature=25";


const char* ssid = "OPTIMUS";          // Your WiFi SSID
const char* password = "qqwweeaaaa";  // Your WiFi Password
const char* serverAddress = "192.168.110.154"; // Change this to your local server's IP address
const int serverPort = 3000; // Change this to your local server's port

String webSerialData,lastwebSerialData;
void recvMsg(uint8_t *data, size_t len){
  WebSerial.println("Received Data...");
  String d = "";
  for(int i=0; i < len; i++){
    d += char(data[i]);
  }
  WebSerial.println(d);
  webSerialData = d;
  if (d == "ON"){
    digitalWrite(LED, LOW);
  }
  if (d=="OFF"){
    digitalWrite(LED, HIGH);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, HIGH);
   // Connect to Wi-Fi
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.println("IP Address: ");
  Serial.println(WiFi.localIP());
  // WebSerial is accessible at "<IP Address>/webserial" in browser
  WebSerial.begin(&server);
  WebSerial.msgCallback(recvMsg);
  server.begin();
  dataDelay.start(); //start the ticker.
}

void loop() {
  String readSerial;
  WebSerial.println(webSerialData);
  lastwebSerialData = webSerialData;
  Serial.println(webSerialData);
  while(webSerialData == lastwebSerialData){
  readSerial = getCommands();
  readSerial = getCommands();
  WebSerial.println(readSerial);
  if(readSerial[0] == 'p' && readSerial[1] == 'H'){
    dataToSend = readSerial;
    Serial.println("Got New data to send.");
  }
dataDelay.update(); //it will check the Ticker and if necessary, it will run the callback function
  }
  
}

String getCommands() {
  if (Serial.available() > 0) {
    String receivedString = ""; // Create a string variable to store received data
    while (Serial.available() > 0) {
      char incomingChar = Serial.read(); // Read a character
      if (incomingChar == '\n' || incomingChar == '\r') {
        // If newline or carriage return is encountered, break the loop
        break;
      }
      receivedString += incomingChar; // Append the received character to the string
    }
    Serial.read(); 
    return receivedString;
  }
  else {
    return "SerialNotAvailable";
  }
}

void sendDataToWeb(){
  // Send HTTP POST request to server
  WiFiClient client;
  if (client.connect(serverAddress, serverPort)) {
    Serial.print("Connected to server: ");
    Serial.println(serverAddress);
    client.println("POST / HTTP/1.1");
    client.print("Host: ");
    client.println(serverAddress);
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.print("Content-Length: ");
    client.println(dataToSend.length());
    client.println();
    client.println(dataToSend);
    Serial.println("Data sent to server");
    }
   else {
    Serial.println("Connection to server failed");
  }
}
