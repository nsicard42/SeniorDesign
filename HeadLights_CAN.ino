#include <SPI.h>
#include <mcp2515.h>

#define lightSensor A5

struct can_frame canMsg1;
MCP2515 mcp2515(10);


void setup() {
  canMsg1.can_id  = 0x767;
  canMsg1.can_dlc = 8;
  
  while (!Serial);
  Serial.begin(115200);
  
  mcp2515.reset();
  mcp2515.setBitrate(CAN_500KBPS,MCP_8MHZ);
  mcp2515.setNormalMode();
  
  Serial.println("Example: Write to CAN");
}

void loop() {
   int lightLevel = analogRead(lightSensor);
    if (lightLevel == 0) {
      digitalWrite (8,HIGH);
      digitalWrite (7,LOW);
      digitalWrite (6,LOW);
      }
   else if (lightLevel < 20 && lightLevel > 0) {
      digitalWrite (8,LOW);
      digitalWrite (7,HIGH);
      digitalWrite (6,LOW);
      }
   else {
      digitalWrite (8,LOW);
      digitalWrite (7,LOW);
      digitalWrite (6,HIGH);
      }
    Serial.println(lightLevel);
    delay(1000);
    
  canMsg1.data[0] = lightLevel; 
  canMsg1.data[1] = 0x87;
  canMsg1.data[2] = 0x32;
  canMsg1.data[3] = 0xFA;
  canMsg1.data[4] = 0x26;
  canMsg1.data[5] = 0x8E;
  canMsg1.data[6] = 0xBE;
  canMsg1.data[7] = 0x86;

  mcp2515.sendMessage(&canMsg1);

  Serial.println("Messages sent");
  
  delay(1000);
}
