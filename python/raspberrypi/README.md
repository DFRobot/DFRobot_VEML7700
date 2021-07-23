# DFRobot_VEML7700


## DFRobot_VEML7700 Library for RaspberryPi


## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Method_H3LIS200DL_LIS331HH](#Method_H3LIS200DL_LIS331HH)
* [Method_LIS2DW12_IIS2DLPC](#Method_LIS2DW12_IIS2DLPC)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary


## Installation


## Method_H3LIS200DL_LIS331HH
```python
  '''
    @brief Initialize the function
    @return return True(Succeed)/False(Failed)
  '''
  def begin(self):

  '''
    @brief get ALS lux
    @return ALS lux
  '''
  def get_ALS_lux(self):

  '''
    @brief get white lux
    @return white lux
  '''
  def get_white_lux(self):

  '''
    @brief get auto ALS lux 
    @return auto ALS lux 
  '''
  def get_auto_ALS_lux(self):
```
## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Raspberry Pi              |      √         |            |             | 



## History

- data 2021-1-26
- version V1.0


## Credits

Written by(li.feng@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))
