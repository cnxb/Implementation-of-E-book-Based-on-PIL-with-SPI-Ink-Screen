# Implementation-of-E-book-Based-on-PIL-with-SPI-Ink-Screen

这是一个借助RaspberryPi SPI接口通信，基于InkScreen墨水屏，PIL文字显示的类电子书方案程序设计
## 材料
### 硬件
1.可运行的RaspberryPi3B/4B
2.Spi墨水屏（可依靠SPI接口传输单色图像）（Waveshare）
3.按钮若干
### 软件
1.Python3
2.Raspbian
3.SPI驱动

## 用法
0.系统：RASPBIAN
1.装python3，处理依赖
2.插入墨水屏
3.按钮接到接口，一处接往GND
4.下载代码，运行，./book书籍放入
 
            
## 模块
松开延迟模块
激活按钮时，若由为高电平时判断，则会导致按下一瞬间输出多次。
如上述代码Line36-39，
当完成低电平—高电平—低电平时时才可输出一个状态信号。
需延迟，可调整，易封装。
 