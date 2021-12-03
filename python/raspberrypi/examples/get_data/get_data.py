# -*- coding: utf-8 -*-
'''
  # @file  get_data.py
  # @brief  Get measurement data of the sensor
  # @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @license  The MIT License (MIT)
  # @author  [qsjhyy](yihuan.huang@dfrobot.com)
  # @version  V1.0
  # @date  2021-05-06
  # @url  https://github.com/DFRobot/DFRobot_VEML7700
'''
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from DFRobot_VEML7700 import *

veml7700 = DFRobot_VEML7700_I2C(bus_num = 1)

while (veml7700.begin() == False):
  print ('Please check that the veml7700 sensor is properly connected')
  time.sleep(3)
print("sensor begin successfully!!!")

while True:
  ''' Directly read the current measured data, unit Lx '''
  lux = veml7700.get_ALS_lux()
  print('ALS_LUX :', lux, 'lx')
