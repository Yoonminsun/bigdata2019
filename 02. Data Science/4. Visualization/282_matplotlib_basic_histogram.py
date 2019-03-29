# 히스토그램
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot') # ggplot 스타일 사용

mu1,mu2,sigma = 100,130,15
# randn(10000) : -1~1 사이의 정규 분포를 갖는 값을 10000개 생성
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# hist함수 인자
# bins: 수치가 클수록 세로축이 정교해짐
# normed: False 일 경우 빈도로 표시, True는 확률로 표시
# alpha: 투명도
n,bins,patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
# n,bins,patches = ax1.hist(x1, bins=50, color='darkgreen') # normed 의 default : False
n,bins,patches = ax1.hist(x2, bins=50, normed=False, color='orange',alpha=0.5)
# x축 눈금 위치를 아래쪽
ax1.xaxis.set_ticks_position('bottom')
# y축 눈금 위치를 왼쪽
ax1.yaxis.set_ticks_position('left')
# default 값도 x:bottom, y:left 인 것 같음

plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('Histograms',fontsize=14,fontweight='bold')
ax1.set_title('Two Frequency Distributions')

plt.savefig('histogram.png',dpi=400,bbox_inches='tight')
plt.show()