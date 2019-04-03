import PIL.Image as pilimg
import numpy as np

im = pilimg.open('zero.jpg')
im.show()
pix = np.array(im)
print(pix) # 437*626 >> pix[0]은 1열의 437행의 r,g,b 값들을 가진다

