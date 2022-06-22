import numpy as np
import cv2 as cv
from drawCircle import drawCircle
from drawLineCircle import drawLineCircle

img = np.zeros([500, 700], dtype=np.uint8)


drawCircle(cx=100, xy=100, red=50, img=img)
drawCircle(cx=430, xy=650, red=100, img=img)
drawLineCircle(cx=250, xy=350, red=150, borderSize=5, img=img)
drawLineCircle(cx=250, xy=350, red=100, borderSize=1, img=img)
drawLineCircle(cx=250, xy=350, red=50, borderSize=1, img=img)

cv.imshow("Drawing", img)
cv.waitKey(0)
cv.destroyWindow