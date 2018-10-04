#include <mcp_can.h>
#include <SPI.h>
 long unsigned int rxId;
unsigned char len = 0;
unsigned char rxBuf[8];
char msgString[128];                        // Array to store serial string
 #define CAN0_INT 2                              // Set INT to pin 2
MCP_CAN CAN0(10);  


// Set CS to pin 10

//char a[40];
int stri[8];
void datahex(char str[40])
{
  int base=1;
  int sum=0;
  int i=0;
  for(int j=38;j>=0;j--)
      {
          if(j%5==3 || j%5==2)
          {
               if(str[j]>='0' && str[j]<='9')
                    {
                        sum+=(int(str[j])-48)*base;
                        base*=16;
                    }
                    else if(str[j]>='A' && str[j]<='F')
                    {
                        sum+=(int(str[j])-55)*base;
                        base*=16;
                    }
           }
            if(j%5 == 4 || j==1)
             {
                 stri[i]=sum;
                 sum=0;
                 base=1;
                 i++;
             }
        }
   for(int i=7;i>=0;i--)
       {
        Serial.print(stri[i]);
        Serial.print(",");
        if(i==0)
        {
          Serial.println(":");
        }
       }
            
} 
 
 
 void setup()
{
  Serial.begin(115200);
  
  // Initialize MCP2515 running at 16MHz with a baudrate of 500kb/s and the masks and filters disabled.
  if(CAN0.begin(MCP_ANY, CAN_1000KBPS, MCP_8MHZ) == CAN_OK)
    Serial.println("MCP2515 Initialized Successfully!");
  else
    Serial.println("Error Initializing MCP2515...");
  
  CAN0.setMode(MCP_NORMAL);                     // Set operation mode to normal so the MCP2515 sends acks to received data.
   pinMode(CAN0_INT, INPUT);                            // Configuring pin for /INT input
  
  Serial.println("MCP2515 Library Receive Example...");
}
 void loop()
{
  if(!digitalRead(CAN0_INT))                         // If CAN0_INT pin is low, read receive buffer
  {
    Serial.println("asdasdasD");
    CAN0.readMsgBuf(&rxId, &len, rxBuf);      // Read data: len = data length, buf = data byte(s)
    
    if((rxId & 0x80000000) == 0x80000000)     // Determine if ID is standard (11 bits) or extended (29 bits)
      sprintf(msgString, "Extended ID: 0x%.8lX  DLC: %1d  Data:", (rxId & 0x1FFFFFFF), len);
    else
      sprintf(msgString, "Standard ID: 0x%.3lX       DLC: %1d  Data:", rxId, len);
  
    Serial.print(msgString);
    datahex(msgString);
  
    if((rxId & 0x40000000) == 0x40000000){    // Determine if message is a remote request frame.
      sprintf(msgString, " REMOTE REQUEST FRAME");
      Serial.print(msgString);
    } else {
      for(byte i = 0; i<len; i++){
        sprintf(msgString, " 0x%.2X", rxBuf[i]);
        Serial.print(msgString);
        datahex(msgString);
      }
    }
        
    Serial.println();
  }
}
