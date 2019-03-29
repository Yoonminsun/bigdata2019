# 목적: 그래프에 문자 입력하기
from matplotlib import font_manager,rc
import matplotlib.pyplot as plt

font_location = "C:\Windows\Fonts\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)

plt.plot([1,2,3,4],[1,2,3,4],'y')
# plt.bar([1,2,3,4],[3,4,5,6])
plt.xlabel('X축')
plt.ylabel('Y축')
plt.title('matplotlib 활용')
plt.text(3.5,3.0,'평균:2.5') # 해당 좌표에 문자열 삽입
plt.grid(True) # 그래프에 격자 표시
plt.show()
