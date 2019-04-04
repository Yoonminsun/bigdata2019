import numpy as np
import cv2
# Grayscale 형태로 이미지 read
card = cv2.imread('card.png',cv2.IMREAD_GRAYSCALE)
card_4 = cv2.imread('4_card.png')
card_4_gray = cv2.cvtColor(card_4,cv2.COLOR_BGR2GRAY)
# 적절한 임계값 속성을 찾아 이진화 함
# theta에는 각 임계값, th_~ 에는 각 이진화된 이미지
# theta, th_card = cv2.threshold(card,150,255,cv2.THRESH_TRUNC)

# theta, th_card_4= cv2.threshold(card_4_gray,110,255,cv2.THRESH_BINARY)
theta, th_card_4 = cv2.adaptiveThreshold(card_4_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# cv2.imshow('card',th_card)
# cv2.imshow('img',card_4)
# cv2.imshow('template',card)
# cv2.imshow('imageshow',card_4)
# cv2.waitKey(0) # 이미지가 show 된 상태로 wait
# cv2.destroyAllWindows()
# 픽셀 접근
# h,w = card.shape
# pixel=[]
# for y in range(h):
#     for x in range(w):
#         pixel.append(card.item(y,x))
#
# print(pixel)

# 경계선 검출
contour, hier = cv2.findContours(th_card_4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contour = sorted(contour,key=cv2.contourArea,reverse=True)

for i in contour[0]:
    cv2.drawContours(card_4,[i],0,(0,255,0),3)

cv2.imshow("result",card_4)

# 템플릿 매칭
# w,h = card.shape
#
# res = cv2.matchTemplate(card_4_gray,card,cv2.TM_CCOEFF)
# min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
# left_top = max_loc
# right_bottm = (left_top[0]+h, left_top[1]+w)
# cv2.rectangle(card_4,left_top,right_bottm,255,2)
# cv2.imshow('detected',card_4)

cv2.waitKey(0)
cv2.destroyAllWindows()


