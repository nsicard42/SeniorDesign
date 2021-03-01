#include <SPI.h>
#include <mcp2515.h>

#define sensor A0 // Sharp IR GP2Y0A41SK0F (4-30cm, analog)

struct can_frame canMsg1;
MCP2515 mcp2515(10);


void setup() {
  canMsg1.can_id  = 0x010;
  canMsg1.can_dlc = 8;
  
  while (!Serial);
  Serial.begin(115200);
  
  mcp2515.reset();
  mcp2515.setBitrate(CAN_500KBPS,MCP_8MHZ);
  mcp2515.setNormalMode();
  
  Serial.println("Example: Write to CAN");
}

void loop() {
  
  // 5v
  float volts = analogRead(sensor)*0.0048828125;  // value from sensor * (5/1024)
  int distance = 13*pow(volts, -1); // worked out from datasheet graph
  delay(1000); // slow down serial port

  if (distance<6){
    Serial.print(distance);
    Serial.print("cm");
    Serial.println("Full Tank");
  }
  else if (distance >=6 && distance <10){
    Serial.print(distance);
    Serial.print("cm");
    Serial.println(" Half Tank");
  }
  else if (distance >=10 && distance < 14){
    Serial.print(distance);
    Serial.print("cm");
    Serial.println(" Quarter Tank");
  }
  else if (distance >=14 && distance < 18) {
    Serial.print(distance);
    Serial.print("cm");
    Serial.println(" Low Gas");
  }
  else {
    Serial.print(distance);
    Serial.print("cm");
    Serial.println(" Empty Tank");
  }
  
  canMsg1.data[0] = distance; 
  canMsg1.data[1] = 0x68;
  canMsg1.data[2] = 0x92;
  canMsg1.data[3] = 0xD5;
  canMsg1.data[4] = 0x00;
  canMsg1.data[5] = 0xEE;
  canMsg1.data[6] = 0xBB;
  canMsg1.data[7] = 0x88;

  mcp2515.sendMessage(&canMsg1);

  Serial.println("Messages sent");
  
  delay(1000);
}
