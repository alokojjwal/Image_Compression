import numpy
from PIL import Image
im=Image.open('lena.png')
pixelmap=im.load()
I=numpy.asanyarray(Image.open('lena.png'))
img=Image.new(im.mode,im.size)
pixelnew=img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if(pixelmap[i,j]>=(0,0,0) and pixelmap[i,j]<=(31,31,31)):
            pixelnew[i,j]=(0,0,0)
        elif(pixelmap[i,j]>=(32,32,32) and pixelmap[i,j]<=(63,63,63)):
            pixelnew[i,j]=(4,4,4)
        elif(pixelmap[i,j]>=(64,64,64) and pixelmap[i,j]<=(95,95,95)):
            pixelnew[i,j]=(8,8,8)
        elif(pixelmap[i,j]>=(96,96,96) and pixelmap[i,j]<=(127,127,127)):
            pixelnew[i,j]=(12,12,12)
        elif(pixelmap[i,j]>=(128,128,128) and pixelmap[i,j]<=(159,159,159)):
            pixelnew[i,j]=(16,16,16)
        elif(pixelmap[i,j]>=(160,160,160) and pixelmap[i,j]<=(191,191,191)):
            pixelnew[i,j]=(20,20,20)
        elif(pixelmap[i,j]>=(192,192,192) and pixelmap[i,j]<=(223,223,223)):
            pixelnew[i,j]=(24,24,24)
        elif(pixelmap[i,j]>=(224,224,224) and pixelmap[i,j]<=(255,255,255)):
            pixelnew[i,j]=(28,28,28)
            
img.save('lena_1.png')
J=numpy.asanyarray(Image.open('lena_1.png'))
