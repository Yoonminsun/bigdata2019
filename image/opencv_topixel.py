import numpy as np
import cv2
img = cv2.imread('test.png')
cv2.imshow('imageshow',img)
cv2.waitKey(0) # 이미지가 show 된 상태로 wait
cv2.destroyAllWindows()

pixel = []

h,w,cha = img.shape
for y in range(0,h):
    for x in range(0,w):
        r = img.item(y,x,2)
        g = img.item(y,x,1)
        b = img.item(y,x,0)
        pixel.append([r,g,b])

print(pixel)