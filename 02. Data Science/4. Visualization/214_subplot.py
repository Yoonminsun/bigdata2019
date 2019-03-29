# 목적: 여러 개의 그래프 그리기
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt

plt.figure()

# subplot(n_of_rows,n_of_cols,index)
plt.subplot(2,1,1) # 2행 1열 모양의 1번째는
plt.plot([1,2,3,4],[1,2,3,4],'ro') # 해당 plot을
plt.subplot(2,1,2) # 2행 1열 모양의 2번째는
plt.plot([5,6,7,8],[5,6,7,8],'b') # 해당 plot을 넣음
plt.show()