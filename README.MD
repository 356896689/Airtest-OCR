# ������Ҫ��

## 1������anaconda ����װ

## 2������tesser-ocr��װ�����û�������

## 3����anaconda�а�װpytesseract��airtest

## 4����pytesseract��װ�����ҵ�pytesseract.py���޸�tesseract_cmd ·��Ϊtesser-ocr·��
![] (image/1.jpg)
## 5����airtest����ѡ�������������python����Ϊ����anaconda��python.exe
![] (image/2.jpg)
## 6������չ�����ิ�Ƶ�anaconda��airtest·���µ�core�ļ�����
![] (image/3.jpg)

# ʹ���ֲ᣺
##1���ű�ʾ����

```html
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.core.tools import *

snapshot('f:1.jpg')
a,b = pixel_find('������','f:1.jpg')
print(a)
touch(a[0])
sleep(3)
a,b = pixel_find('��Ѷ',None,b)
touch(a[0])
sleep(3)
a,b = pixel_find('�ҵ�',None,b)
touch(a[0])
sleep(3)
a,b = pixel_find('�տ�',None,b)
touch(a[0])
```
##2��ʹ�ý���

  1�����빤����from airtest.core.tools import *
  2�����µ�ҳ����ִ�в�����Ҫ�Ƚ�ͼsnapshot('f:1.jpg')�������б���ͼƬ��f��������Ϊ1.jpg
  3��pixel_find(input,filePath=None,temp=None)����Ϊ������
	inputΪ��ҳ���в��ҵ������ַ�
	filePathΪ��ͼ��·��
	tempΪ�������ص�ֵ
  4��a,b = pixel_find('��ע',None,b)
	touch(a[0])
	a,b = pixel_find('��Ƶ',None,b)
	touch(a[0])
	aΪ���ص����꣬����touch���������bΪ���ص����в��ҵ��ĺ��ֵ����꣬��ͬһҳ�����ٴ���touch����������Ҫ����filePath��ֻ��������һ��pixel_find()���ص�b����filePath��ΪNone�����磺pixel_find('��ע',None,b)
  5����C�̸�Ŀ¼·������log.txt�ļ������ļ��м������в�ѯ���ĺ��֣����ҳ�汨����list index out of range������ȥlog.txt�ļ��鿴�Ƿ�ʶ���˸ú��֣����Ը����ļ������ʵ������������ݡ����磬����Ϊ�������������ѯ�������������롰���񡱻򡰹�����
  6���˷������Ժ�Airtest��ͼ����һ������
  ![] (image/4.jpg)
##3��ע������
  �������ʹ���������ģ������ֱ������⣬����ʶ��Ч���ܲ��ʹ�õ�������ģ����3.2.5�����ģ���������кܸߵķֱ��ʻ��ڴ���Ŀ��ִ�нű�Ҳ������^_^��������ͬѧ������һ�¡�