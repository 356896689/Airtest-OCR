# 环境需要：

## 1、下载anaconda 并安装

## 2、下载tesser-ocr安装并配置环境变量

## 3、在anaconda中安装pytesseract和airtest

## 4、在pytesseract安装包里找到pytesseract.py中修改tesseract_cmd 路径为tesser-ocr路径
![1.jpg] (https://github.com/356896689/Airtest-OCR/blob/master/image/1.jpg)

## 5、在airtest——选项——设置中配置python环境为本地anaconda的python.exe
![2.jpg] (https://github.com/356896689/Airtest-OCR/blob/master/image/2.jpg)

## 6、将拓展工具类复制到anaconda中airtest路径下的core文件夹内
![3.jpg] (https://github.com/356896689/Airtest-OCR/blob/master/image/3.jpg)

# 使用手册：

## 1、脚本示例：

```html
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.core.tools import *

snapshot('f:1.jpg')
a,b = pixel_find('云闪付','f:1.jpg')
print(a)
touch(a[0])
sleep(3)
a,b = pixel_find('资讯',None,b)
touch(a[0])
sleep(3)
a,b = pixel_find('我的',None,b)
touch(a[0])
sleep(3)
a,b = pixel_find('收款',None,b)
touch(a[0])
```
## 2、使用介绍

  1）引入工具类from airtest.core.tools import *
  
  2）在新的页面中执行操作需要先截图snapshot('f:1.jpg')，例子中保存图片在f盘下起名为1.jpg
  
  3）pixel_find(input,filePath=None,temp=None)函数为主函数
	input为在页面中查找的中文字符
	filePath为截图的路径
	temp为函数返回的值
	
  4）a,b = pixel_find('关注',None,b)
	touch(a[0])
	a,b = pixel_find('视频',None,b)
	touch(a[0])
	a为返回的坐标，用于touch点击操作，b为返回的所有查找到的汉字的坐标，在同一页面中再次做touch操作，不需要输入filePath，只需输入上一个pixel_find()返回的b，把filePath制为None，例如：pixel_find('关注',None,b)
	
  5）在C盘根目录路径下有log.txt文件，此文件中记载所有查询到的汉字，如果页面报错：list index out of range，可以去log.txt文件查看是否识别到了该汉字，可以根据文件内容适当调整输入内容。例如，输入为“任务管理”查询不到，可以输入“任务”或“管理”
  
  6）此方法可以和Airtest截图方法一起使用
  
  ![4.jpg] (https://github.com/356896689/Airtest-OCR/blob/master/image/4.jpg)
  
## 3、注意事项

  测试最好使用真机，因模拟机器分辨率问题，字体识别效果很差，我使用的是天天模拟器3.2.5，如果模拟器竖屏有很高的分辨率或在大屏目中执行脚本也许可以^_^，大屏的同学可以试一下。
