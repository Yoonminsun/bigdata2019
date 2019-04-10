import numpy as np
import cv2
import math

# 좌표사이의 거리 계산 함수 작성
def calc_dist(list1,list2):
    a = list2[0] - list1[0]
    b = list2[1] - list1[1]
    return math.sqrt((a*a)+(b*b))

# Grayscale 형태로 이미지 read
# card = cv2.imread('card.png',cv2.IMREAD_GRAYSCALE)
card = cv2.imread('card9.png',cv2.IMREAD_GRAYSCALE)
card_4 = cv2.imread('4_card.png')
card_4_gray = cv2.cvtColor(card_4,cv2.COLOR_BGR2GRAY)
cv2.imshow("find",card)

# Bilateral Filtering : 에지를 보존하면서 노이즈를 감소시키는 필터링 방법
# card_4_gray = cv2.bilateralFilter(card_4_gray,9,75,75)
# cv2.imshow("blur",card_4_gray)

# 적절한 임계값 속성을 찾아 이진화 함
# theta에는 각 임계값, th_~ 에는 각 이진화된 이미지

theta, th_card_4= cv2.threshold(card_4_gray,150,255,cv2.THRESH_BINARY)

# 템플릿 매칭
w,h = card.shape

res = cv2.matchTemplate(card_4_gray,card,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
left_top = max_loc
right_bottm = (left_top[0]+h, left_top[1]+w)

# 경계선 검출

tv_lt = list(left_top)
tv_rb = list(right_bottm)

# 템플릿 매칭 부분 사각형 그리기
# cv2.rectangle(card_4,left_top,right_bottm,(255,0,0))

contour, hier = cv2.findContours(th_card_4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contour = sorted(contour,key=cv2.contourArea,reverse=True)

vector_distance = []
contour_list=[]
min_count = [len(contour[i]) for i in range(len(contour))]
min_count = min(min_count)

for num in range(len(contour)):
    dist_sum = 0
    contour_list=[]
    for ct in range(min_count):
        contour_list.append(contour[num][ct][0])
    for i in contour_list:
        dist = calc_dist(tv_lt,i) + calc_dist(tv_rb,i)
        dist_sum += dist
    vector_distance.append(dist_sum)


print(vector_distance)
match_index = np.argmin(vector_distance)

# card9 = 3 // card = 0
cv2.drawContours(card_4,[contour[match_index]],-1,(0,255,0),3)

cv2.imshow("found_result",card_4)

cv2.waitKey(0)
cv2.destroyAllWindows()


