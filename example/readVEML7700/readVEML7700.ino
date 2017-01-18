 /*!
  * file readVEML7700.ino
  * brief DFRobot's VEML7700 ambient light sensor
  * @n [Get the module here](等上架后添加商品购买链接)
  * @n This example Set the volume size and play music snippet.
  * @n [Connection and Diagram](等上架后添加wiki链接)
  *
  * Copyright	[DFRobot](http://www.dfrobot.com), 2016
  * Copyright	GNU Lesser General Public License
  *
  * @author [yangyang](971326313@qq.com)
  * version  V1.0
  * date  2016-12-8
  */
  
#include <Wire.h>
#include "DFRobot_VEML7700.h"

DFRobot_VEML7700 als;

void setup()
{
  Serial.begin(9600);
  als.begin();
}

void loop()
{
  float lux;
  
  als.getALSLux(lux);
  Serial.print("Lux:");
  Serial.print(lux);
  Serial.println(" lx");
  
  delay(200);
}
