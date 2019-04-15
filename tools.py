import cv2
import numpy as np
from collections import defaultdict
import pytesseract
import threading

class MyThread(threading.Thread):

    def __init__(self,func,args=()):
        threading.Thread.__init__(self)
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
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(imgry)
    ret, thresh1 = cv2.threshold(cl, 0.66 * cl.mean(), cl.max(), 1)
    ret, thresh2 = cv2.threshold(cl, 0.66 * cl.mean(), cl.max(), 0)
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
    def code(x):
        code = pytesseract.image_to_boxes \
            (x, lang='chi_sim', config='', nice=0, output_type=pytesseract.Output.STRING)
        return code

    t1 = MyThread(code,args=(cl,))
    t2 = MyThread(code,args=(thresh1,))
    t3 = MyThread(code,args=(opening,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    z = t1.get_result()+'\n'+t2.get_result()+'\n'+t3.get_result()

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
#     img_path = 'F:1.jpg'
#     a,b = pixel_find('立即',img_path)
#     print(a)