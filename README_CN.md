# DFRobot_VEML7700
* [English Version](./README.md)

VEML7700是一个高精度环境光数字16位分辨率传感器在微型透明6.8 mm x
2.35毫米x 3.0毫米包装。它包括一个高灵敏度的光电二极管，一个低噪声放大器，一个16位a /D转换器，并支持一个易于使用的I2C总线通信接口。
环境光结果作为数字值可用。

![产品实物图](./resources/images/VEML7700.png)


## 产品链接 (https://www.dfrobot.com.cn/goods-1430.html)
    SKU: SEN0228


## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性)
* [历史](#历史)
* [创作者](#创作者)


## 概述

* 滤液tm技术适配:接近真实人眼反应
* O-TrimTM技术采用:ALS输出公差
≤10%
* 16位动态范围的环境光检测
0 lx至120 KLX，分辨率为0.0036 lx/ct，支持低透光率(暗)镜头设计
* 100hz和120hz闪烁噪声抑制
* 良好的温度补偿
* 高动态检测分辨率
软件关机模式控制


## 库安装

要使用这个库，首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开示例文件夹并在文件夹中运行演示。


## 方法

```C++

  /**
   * @fn setGain
   * @brief 设置ALS增益系数
   * @param gain Gain selection:
   * @n     ALS_GAIN_x1, ALS_GAIN_x2, ALS_GAIN_d8, ALS_GAIN_d4
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setGain(eAlsGain_t gain);

  /**
   * @fn getGain
   * @brief 获取当前ALS增益系数
   * @param gain 当前ALS增益系数:
   * @n     ALS_GAIN_x1, ALS_GAIN_x2, ALS_GAIN_d8, ALS_GAIN_d4
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getGain(eAlsGain_t& gain);

  /**
   * @fn setIntegrationTime
   * @brief 设置ALS积分时间
   * @param itime ALS integration time setting:
   * @n       ALS_INTEGRATION_25ms, ALS_INTEGRATION_50ms, ALS_INTEGRATION_100ms, 
   * @n       ALS_INTEGRATION_200ms, ALS_INTEGRATION_400ms, ALS_INTEGRATION_800ms
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setIntegrationTime(eAlsItime_t itime);

  /**
   * @fn getIntegrationTime
   * @brief 获取ALS积分时间
   * @param itime 当前ALS积分时间:
   * @n       ALS_INTEGRATION_25ms, ALS_INTEGRATION_50ms, ALS_INTEGRATION_100ms, 
   * @n       ALS_INTEGRATION_200ms, ALS_INTEGRATION_400ms, ALS_INTEGRATION_800ms
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getIntegrationTime(eAlsItime_t& itime);

  /**
   * @fn setPersistence
   * @brief persistence protect number setting
   * @param persist persistence protect number setting:
   * @n       ALS_PERSISTENCE_1, ALS_PERSISTENCE_2, ALS_PERSISTENCE_4, ALS_PERSISTENCE_8
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setPersistence(eAlsPersist_t persist);

  /**
   * @fn setPowerSavingMode
   * @brief Power saving mode setting
   * @param powerMode Power saving mode:
   * @n       ALS_POWER_MODE_1, ALS_POWER_MODE_2, ALS_POWER_MODE_3, ALS_POWER_MODE_4
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setPowerSavingMode(eAlsPowerMode_t powerMode);

  /**
   * @fn setPowerSaving
   * @brief Power saving mode enable
   * @param enabled :
   * @n       0 失能
   * @n       1 使能
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setPowerSaving(uint8_t enabled);

  /**
   * @fn setInterrupts
   * @brief ALS interrupt enable setting
   * @param enabled :
   * @n       0 失能
   * @n       1 使能
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setInterrupts(uint8_t enabled);

  /**
   * @fn setPower
   * @brief ALS shut down setting
   * @param on :
   * @n       0 power on
   * @n       1 shut down
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setPower(uint8_t on);

  /**
   * @fn setALSHighThreshold
   * @brief 设置中断阈值上限
   * @param thresh 16位阈值上限设定值
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setALSHighThreshold(uint32_t thresh);

  /**
   * @fn setALSLowThreshold
   * @brief 设置中断阈值下限
   * @param thresh 16位阈值下限设定值
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t setALSLowThreshold(uint32_t thresh);

  /**
   * @fn getALS
   * @brief get high resolution ALS output
   * @param als 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getALS(uint32_t& als);

  /**
   * @fn getWhite
   * @brief get WHITE output
   * @param white 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getWhite(uint32_t& white);

  /**
   * @fn getHighThresholdEvent
   * @brief 获取阈值上限触发中断事件
   * @param event :
   * @n       0 未检测到阈值上限中断事件
   * @n       1 检测到阈值上限中断事件
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getHighThresholdEvent(uint8_t& event);

  /**
   * @fn getLowThresholdEvent
   * @brief 获取阈值下限触发中断事件
   * @param event :
   * @n       0 未检测到阈值下限中断事件
   * @n       1 检测到阈值下限中断事件
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getLowThresholdEvent(uint8_t& event);

  /**
   * @fn begin
   * @brief 初始化函数
   * @return None
   */
  void begin();

  /**
   * @fn begin
   * @brief 初始化函数
   * @param als_gain 设置ALS增益系数
   * @return None
   */
  void begin(uint8_t als_gain);

  /**
   * @fn getALSLux
   * @brief 获取ALS光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getALSLux(float& lux);

  /**
   * @fn getWhiteLux
   * @brief 获取White光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getWhiteLux(float& lux);

  /**
   * @fn getAutoALSLux
   * @brief 获取AutoALS光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getAutoALSLux(float& lux);

  /**
   * @fn getAutoWhiteLux
   * @brief 获取AutoWhite光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getAutoWhiteLux(float& lux);

  /**
   * @fn getAutoALSLux
   * @brief 获取AutoALS光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @param auto_gain Gain selection
   * @param auto_itime ALS integration time setting
   * @param raw_counts 未处理的原始数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getAutoALSLux(float& lux,
                        DFRobot_VEML7700::eAlsGain_t& auto_gain,
                        DFRobot_VEML7700::eAlsItime_t& auto_itime,
                        uint32_t& raw_counts);

  /**
   * @fn getAutoWhiteLux
   * @brief 获取AutoWhite光照强度测量值
   * @param lux 缓存获取数据的变量, 16bit数据
   * @param auto_gain Gain selection
   * @param auto_itime ALS integration time setting
   * @param raw_counts 未处理的原始数据
   * @return 返回操作结果
   * @retval STATUS_OK 操作成功, 没有异常
   * @retval STATUS_ERROR 操作失败
   */
  uint8_t getAutoWhiteLux(float& lux,
                          DFRobot_VEML7700::eAlsGain_t& auto_gain,
                          DFRobot_VEML7700::eAlsItime_t& auto_itime,
                          uint32_t& raw_counts);

  /**
   * @fn sampleDelay
   * @brief 数据采样及处理延时
   */
  void sampleDelay(void);

```


## 兼容性

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | :----:
Arduino Uno        |      √       |              |             |
Arduino MEGA2560   |      √       |              |             |
Arduino Leonardo   |      √       |              |             |
FireBeetle-ESP8266 |      √       |              |             |
FireBeetle-ESP32   |      √       |              |             |
FireBeetle-M0      |      √       |              |             |
Micro:bit          |      √       |              |             |


## 历史

- 2021/10/15 - 1.0.0 版本


## 创作者

Written by qsjhyy(yihuan.huang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))

