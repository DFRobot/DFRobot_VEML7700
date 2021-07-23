# -*- coding: utf-8 -*-
'''
  # @file get_data.py
  # @brief Get measurement data of the sensor 
  # @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @licence     The MIT License (MIT)
  # @author      [qsj](qsj.huang@dfrobot.com)
  # @version  V0.1
  # @date  2021-05-06
  # @get from https://www.dfrobot.com
  # @url https://github.com/DFRobot/DFRobot_VEML7700
'''
import time
import sys
sys.path.append('../')
from DFRobot_VEML7700 import *

veml7700 = DFRobot_VEML7700_I2C(bus_num = 1)

while (veml7700.begin() == False):
  print ('Please check that the veml7700 sensor is properly connected')
  time.sleep(3)
print("sensor begin successfully!!!")

while True:
  ''' 直接读取当前测量的数据，单位勒克斯（lx） '''
  lux = veml7700.get_ALS_lux()
  print('ALS_LUX :', lux, 'lx')
