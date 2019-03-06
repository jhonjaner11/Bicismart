
int sensorValue;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
void setup()
{
  Serial.begin(9600);

 

}
 
void loop()
{
  delay(500);//3 segundos
  sensorValue = analogRead(0); // read analog input pin 0
  //Serial.print("AirQua=");
  Serial.print(sensorValue, DEC);
  Serial.println();// prints the value read
  //Serial.println(" PPM");
  //EthernetClient client = server.available(); 
  Serial.flush();
}
