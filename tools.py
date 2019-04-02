import cv2
import numpy as np
from collections import defaultdict
import pytesseract
import threading

class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img

def ocr_find(filePath):
    global height, width
    img = cv_imread(filePath)
    height, width, _ = img.shape
    imgry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgcanny = cv2.Canny(img, 50, 255)
    ret, thresh1 = cv2.threshold(imgry, 141, 255, 0)
    ret, thresh2 = cv2.threshold(imgry, 180, 255, 1)
    ret, thresh3 = cv2.threshold(imgry, 220, 255, 0)
    ret, thresh4 = cv2.threshold(imgry, 200, 255, 0)

    def code(x):
        code = pytesseract.image_to_boxes \
            (imgry, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code
    def code1(x):
        code1 = pytesseract.image_to_boxes \
            (imgcanny, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code1
    def code2(x):
        code2 = pytesseract.image_to_boxes \
            (thresh1, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code2
    def code3(x):
        code3 = pytesseract.image_to_boxes \
            (thresh2, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code3
    def code4(x):
        code4 = pytesseract.image_to_boxes \
            (thresh3, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code4
    def code5(x):
        code5 = pytesseract.image_to_boxes \
            (thresh4, lang='chi_sim', config='', nice=1, output_type=pytesseract.Output.STRING)
        return code5
    t1 = MyThread(code,range(1))
    t2 = MyThread(code1,range(1))
    t3 = MyThread(code2,range(1))
    t4 = MyThread(code3,range(1))
    t5 = MyThread(code4,range(1))
    t6 = MyThread(code5,range(1))
    t1.start(),t2.start(),t3.start(),t4.start(),t5.start(),t6.start()
    t1.join(),t2.join(),t3.join(),t4.join(),t5.join(),t6.join()
    z = t1.get_result()+'\n'+t2.get_result()+'\n'+t3.get_result()+'\n'\
        +t4.get_result()+'\n'+t5.get_result()+'\n'+t6.get_result()

    f = open('C:/log.txt', 'w', encoding='utf-8')
    f.writelines(z)
    f.close()
    return z

def pixel_find(input,filePath=None,temp=None):
    if filePath == None:
        temp = temp
    else:
        temp = ocr_find(filePath).split('\n')
    temp1 = []
    for i in range(len(temp)):
        temp1.append(temp[i][0])
    d = defaultdict(list)
    for k,va in [(v,i) for i,v in enumerate(temp1)]:
        d[k].append(va)
    index = []
    for i in range(len(input)):
        li = d[input[i]]
        index.append(li)
    midindex = []
    lastindex = []
    for i in range(len(index[0])):
        for j in range(len(index)):
            try:
                a = index[j][i]
                midindex.append(a)
            except:
                break
        lastindex.append(midindex)
        midindex = []
    for i in range(len(lastindex)):
        for i in range(len(lastindex)):
            if len(lastindex[i]) != len(input):
                del  lastindex[i]
                break
    firstlist = []
    lastlist = []
    for i in range(len(lastindex)):
        for j in range(1):
            firstlist.append(temp[lastindex[i][0]])
            firstlist.append(temp[lastindex[i][-1]])
        lastlist.append(firstlist)
        firstlist = []
    pixel = []
    for i in range(len(lastlist)):
        xdistance = int(lastlist[i][1].split(' ')[3])-int(lastlist[i][0].split(' ')[1])
        ydistance = int(lastlist[i][1].split(' ')[4])-int(lastlist[i][0].split(' ')[2])
        x = int(lastlist[i][0].split(' ')[1]) + (xdistance//2)
        y = int(lastlist[i][0].split(' ')[2]) + (ydistance//2)
        y = height - y
        pixel.append((x,y))
    return pixel, temp

# if __name__ == '__main__':
#     img_path = 'F:/随行付/机器学习/ai自动化/plus/airtest/case/log_20190115_155319/荐者有红包_分享/1547538822749.jpg'
#     # ocr_find(img_path)
#     a = pixel_find('登录',img_path)
#     print(a)