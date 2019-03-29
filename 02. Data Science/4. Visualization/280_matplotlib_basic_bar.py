# 막대 그래프
import matplotlib.pyplot as plt
plt.style.use('ggplot') # ggplot 스타일 사용

customers = ['ABC','DEF','GHI','JKL','MNO']
customers_index = range(len(customers))
sale_amounts = [127,90,201,111,232]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index,sale_amounts,align='center',color='darkblue')
# ax1.bar(customers_index,sale_amounts)

# x축 눈금 위치를 아래쪽
ax1.xaxis.set_ticks_position('bottom')
# y축 눈금 위치를 왼쪽
ax1.yaxis.set_ticks_position('left')

# xticks (ticks, [labels], **kwargs)
# ticks : array_like
# A list of positions at which ticks should be placed.
# You can pass an empty list to disable xticks.

# labels : array_like, optional
# A list of explicit labels to place at the given locs.

# **kwargs
# Text properties can be used to control the appearance of the labels.

# plt.xticks(customers_index,customers)
# plt.xticks(customers_index,customers,color='red')
plt.xticks(customers_index,customers,color='red',fontsize='large')

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

# dpi: The resolution in dots per inch ( 해상도 )
# bbox_inches: 'tight' 일 경우 마진이 거의 없이 tight 하게 그림 ( 바깥 여백 공간 조절 )
# plt.savefig('bar_plot.png', dpi=400)
plt.savefig('bar_plot_tight.png',dpi=400,bbox_inches='tight')
plt.show()