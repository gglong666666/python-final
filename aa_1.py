import cv2
from PIL import Image
import ImageDraw,ImageFilter
from visual import *
import Image

#變數capture在一開始被宣告為cv2型態，利用VideoCapture(0)可以指定要從Webcam(攝影鏡頭)中擷取畫面，0是預設代號
capture=cv2.VideoCapture(0)

#將 capture 保存為 motion-jpeg,cv_fourcc 格式
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
	
#cvCreateVideoWriter("AVI檔名",AVI格式,每秒的播放速度,AVI大小);
video=cv2.VideoWriter("VideoTest.avi", cv2.cv.CV_FOURCC('I','4','2','1'), 30, size)

#isopened可以查看攝影鏡頭是否開啟
print capture.isOpened()

num=0

#設置一個迴圈讀取image
while (num<4):
    ret,img=capture.read()
	
    #視頻中的圖片一張張寫入
    video.write(img)
    cv2.imshow('Video',img)
	
	#間隔的時間，1000為1秒
    key=cv2.waitKey(2000)
	
	#我們把0的那張去掉，因為0跟1間隔太近
    if(num!=0):
     cv2.imwrite('%s.jpg'%(str(num)),img)
    num=num+1
	
	#拍照夠了就停
    if key==ord('q'):
	
        break
		
#用release方法儲存，等结束程序再等攝影鏡頭關了即顯示成功
video.release()

#把攝影鏡頭關閉
capture.release()

#關閉視窗
cv2.destroyAllWindows()

-----------------------------------------------------------------

im = Image.new( "RGB", (600,600) )
#draw = ImageDraw.Draw( im )
im01=Image.open("1.jpg")

im02=Image.open("2.jpg")

im03=Image.open("3.jpg")

im01=im01.resize((300,600),Image.BILINEAR)
im02=im02.resize((300,300),Image.BILINEAR)
im03=im03.resize((300,300),Image.BILINEAR)
im.paste(im01,(0,0))
im.paste(im02,(300,0))
im.paste(im03,(300,300))
im.save("fun.jpg")

im1=Image.open("fun.jpg")
im2=Image.open("zzz.jpg")
width=500
ratio=float(width)/im1.size[0]
height=int(im1.size[1]*ratio)
im1=im1.resize((width,height),Image.BILINEAR)
im1.save("11.jpg",quality=50)
im2=im2.resize((width,height),Image.BILINEAR)
im2.save("22.jpg",quality=50)
comb=Image.blend(im1,im2,0.7)

comb.save("4.jpg")

new=display(x=0,y=0,width=600,height=600,center=(0,0,0),forward=(1,-0.4,0))
new=display.get_selected()

name1="1"
name2="2"
name3="3"
name4="4"

width = 512 
height = 512 
im1 = Image.open(name1+".jpg")
im2 = Image.open(name2+".jpg")
im3 = Image.open(name3+".jpg")
im4 = Image.open(name4+".jpg")
#print(im.size) # optionally, see size of image
# Optional cropping:
#im = im.crop((x1,y1,x2,y2)) # (0,0) is upper left
im1=im1.resize((width,height), Image.ANTIALIAS)
im2=im2.resize((width,height), Image.ANTIALIAS)
im3=im3.resize((width,height), Image.ANTIALIAS)
im4=im4.resize((width,height), Image.ANTIALIAS)

materials.saveTGA(name1,im1)
materials.saveTGA(name2,im2)
materials.saveTGA(name3,im3)
materials.saveTGA(name4,im4)



r = 3
a1 = 0.0
a2 = 300
a3 = 600
a4 = 900
photo1= materials.texture(data=materials.loadTGA("1"),mapping="rectangular")
photo2= materials.texture(data=materials.loadTGA("2"),mapping="rectangular")
photo3= materials.texture(data=materials.loadTGA("3"),mapping="rectangular")
photo4= materials.texture(data=materials.loadTGA("4"),mapping="rectangular")

big=3

box1=box(length=3, height=3, width=3,pos=(r, 0, 0), color=color.white,material=photo1 )

box2=box(length=big, height=big, width=big,pos=(-r, 0, 0), color=color.white,material=photo2 )

box3=box(length=big, height=big, width=big,pos=(0, r, 0), color=color.white,material=photo3 )

box4=box(length=big, height=big, width=big,pos=(0, -r, 0), color=color.white,material=photo4 )

		
while True:
 rate(30)
 box1.pos = r*vector(cos(a1),sin(a1),box1.z)
 box2.pos = r*vector(cos(a2),sin(a2),box2.z)
 box3.pos = r*vector(cos(a3),sin(a3),box3.z)
 box4.pos = r*vector(cos(a4),sin(a4),box4.z)
 a1 += 0.02
 a2 += 0.02
 a3 += 0.02
 a4 += 0.02








