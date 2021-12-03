/*!
 * @file readVEML7700.ino
 * @brief DFRobot's VEML7700 ambient light sensor
 * @n     High Accuracy Ambient Light Sensor
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license  The MIT License (MIT)
 * @author  [yangyang](971326313@qq.com)
 * @version  V1.0
 * @date  2016-12-08
 * @url  https://github.com/DFRobot/DFRobot_VEML7700
  */

#include "DFRobot_VEML7700.h"
#include <Wire.h>

/*
 * Instantiate an object to drive the sensor
 */
DFRobot_VEML7700 als;

void setup()
{
  Serial.begin(9600);
  als.begin();   // Init
}

void loop()
{
  float lux;
  
  als.getALSLux(lux);   // Get the measured ambient light value
  Serial.print("Lux:");
  Serial.print(lux);
  Serial.println(" lx");
  
  delay(200);
}
