#include <SPI.h>
#include <mcp2515.h>

unsigned long startMillis;
unsigned long currentMillis;
const unsigned long period=1;
int magnetsense=0;
int laststate=1;

int sensPin=2;
int counter=0;

float vecichlespeed;
float radius=0.2;
float pi=3.14;
float circumference=2*radius*pi;

struct can_frame canMsg1;
MCP2515 mcp2515(10);


void setup() {

  startMillis=millis();
  pinMode(sensPin, INPUT);
  
  canMsg1.can_id  = 0x080;
  canMsg1.can_dlc = 8;
  
  while (!Serial);
  Serial.begin(115200);
  
  mcp2515.reset();
  mcp2515.setBitrate(CAN_500KBPS,MCP_8MHZ);
  mcp2515.setNormalMode();
  
  Serial.println("Example: Write to CAN");
}

void loop() {
    currentMillis=millis();
    magnetsense=digitalRead(sensPin);
     
      if(magnetsense==0 && laststate==1){
           laststate=0;
           
        if(currentMillis-startMillis>=period && laststate==0){
        vecichlespeed=circumference/(currentMillis-startMillis)*1000;
        startMillis=currentMillis;
     counter++;
       Serial.println(String(vecichlespeed)+"m/s");
                                                             }
                                        }
    
    
    else{
      if(currentMillis-startMillis>=period && laststate==0){
        startMillis=currentMillis;
      laststate=1;
                                                           } 
        }
        
  
  canMsg1.data[0] = vecichlespeed; 
  canMsg1.data[1] = 0x99;
  canMsg1.data[2] = 0x16;
  canMsg1.data[3] = 0x50;
  canMsg1.data[4] = 0x07;
  canMsg1.data[5] = 0x38;
  canMsg1.data[6] = 0x23;
  canMsg1.data[7] = 0x45;

  mcp2515.sendMessage(&canMsg1);

  Serial.println("Messages sent");
  
  delay(600);
}
