#include <ESP8266WiFi.h>

const char* ssid = "Karan's Phone";
const char* password = "madhu007shi";
const char* serverAddress = "192.168.66.132"; // Change this to your local server's IP address
const int serverPort = 8000; // Change this to your local server's port

void setup() {
  Serial.begin(115200);
  delay(100);
  // Connect to Wi-Fi
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
}

void loop() {
  // Example data to send
  String dataToSend = "pH=7&Turbidity=100&Temperature=25";
  // Send HTTP POST request to server
  WiFiClient client;
  if (client.connect(serverAddress, serverPort)){
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
    Serial.println(dataToSend);
  } 
  else {
    Serial.println("Connection to server failed");
  }
  delay(5000);
}
