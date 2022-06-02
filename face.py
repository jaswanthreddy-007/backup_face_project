from typing import Any
import cv2 as cv
import array as arr
from array import *
import numpy as np
import dlib


img =cv.imread("so1.jpeg")
xposi = []
yposi = []
gr=1.61803

cv.namedWindow("output", cv.WINDOW_NORMAL)
cv.resizeWindow("output", 471, 960)
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks_GTX.dat")

gray = cv.cvtColor(img,cv.COLOR_BGR2RGB)
faces = hog_face_detector(gray)

for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)
        for n in range(0,68):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            xposi.append(x)
            yposi.append(y)
            #print(n,xposi[n],yposi[n])
            cv.circle(img, (x, y), 2, (0, 0, 255), 2)
            cv.putText(img,str(n),(x,y),cv.FONT_HERSHEY_TRIPLEX,0.4,(0,0,0))

#func to make lines on image
def Addline(image,x1,y1,x2,y2): 
    cv.line(image,(x1,y1),(x2,y2),(0,0,0),1)


#required lines to make facemask

Addline(img,xposi[27],yposi[27],xposi[59],yposi[31])
Addline(img,xposi[27],yposi[27],xposi[55],yposi[35])
Addline(img,xposi[59],yposi[31],xposi[55],yposi[35])
Addline(img,xposi[36],yposi[36],xposi[48],yposi[48])
Addline(img,xposi[45],yposi[45],xposi[54],yposi[54])
Addline(img,xposi[48],yposi[48],xposi[35],yposi[35])
Addline(img,xposi[31],yposi[31],xposi[54],yposi[54])
Addline(img,xposi[48],yposi[48],xposi[51],yposi[51])
Addline(img,xposi[51],yposi[51],xposi[54],yposi[54])
Addline(img,xposi[48],yposi[48],xposi[57],yposi[57])
Addline(img,xposi[57],yposi[57],xposi[54],yposi[54])
Addline(img,xposi[22],yposi[22],xposi[25],yposi[25])
Addline(img,xposi[21],yposi[21],xposi[18],yposi[18])
Addline(img,xposi[36],yposi[36],xposi[45],yposi[45])
Addline(img,xposi[36],yposi[36],xposi[39],yposi[39])
Addline(img,xposi[42],yposi[42],xposi[45],yposi[45])
Addline(img,xposi[39],yposi[39],xposi[42],yposi[42])
Addline(img,xposi[4],yposi[4],xposi[57],yposi[57])
Addline(img,xposi[57],yposi[57],xposi[12],yposi[12])
Addline(img,xposi[22],yposi[22],xposi[26],yposi[26])
Addline(img,xposi[21],yposi[21],xposi[17],yposi[17])


#lengths

xmid_lip=(xposi[62]+xposi[66])/2
ymid_lip=(yposi[62]+yposi[66])/2
ymid_lip_chin=abs(ymid_lip-yposi[8])
ynose_midlip=abs(yposi[27]-ymid_lip)
uplip_thickness=abs(yposi[51]-yposi[62])
lowlip_thhickness=abs(yposi[66]-yposi[57])
nose_length=abs(yposi[27]-yposi[30])
nose_width=abs(xposi[59]-xposi[55 ])
nose_chin=abs(yposi[33]-yposi[8])
lip_width=abs(xposi[48]-xposi[54])
eye_width=abs(xposi[42]-xposi[45])
dist_eyes=abs(xposi[42]-xposi[39])
noselength_2 = abs(yposi[27]-yposi[33])
nose_end_chin=abs(yposi[33]-yposi[8])
nose_end_midlip=abs(ymid_lip-yposi[33])
#parameters of golden ratio
raw=ynose_midlip/ymid_lip_chin
if raw > gr: 
    para1=(gr/raw)*100
else:
    para1=(raw/gr)*100

raw2=nose_end_chin/ymid_lip_chin
if raw2 > gr: 
    para6=(gr/raw2)*100
else:
    para6=(raw2/gr)*100

raw3=nose_width/nose_end_midlip
if raw3 > gr: 
    para7=(gr/raw3)*100
else:
    para7=(raw3/gr)*100

#parameters of ratio 1:1

para2=(min(nose_width,lip_width)/max(nose_width,lip_width))*100
para3=(min(noselength_2,nose_chin)/max(noselength_2,nose_chin))*100
para4=(min(eye_width,dist_eyes)/max(eye_width,dist_eyes))*100
para5=(min(nose_length,nose_width)/max(nose_length,nose_width))*100

#computing avg golden ratio percentage
gr_comp_avg=(para1+para2+para3+para4+para5+para6+para7)/7

print(gr_comp_avg)
print("\n\n")

print(para1)
print(para2)
print(para3)

print(para4)
print(para5)
print(para6)
print(para7)

print("\n\n")
#print(nose_length)
#print(nose_width)
gr_comp_avg = round(gr_comp_avg,3)

cv.putText(img,str(gr_comp_avg),(10,60),cv.FONT_HERSHEY_TRIPLEX,1.3,(0,0,0))

cv.imwrite("jasprocess.jpg",img)
cv.imshow("output",img)
cv.waitKey(0)
cv.destroyAllWindows()

