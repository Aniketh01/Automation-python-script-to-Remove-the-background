import numpy as np
import cv2
from matplotlib import pyplot as plt

file_name = "testm1.jpg"

src = cv2.imread("/home/aniketh/KStars: SoK/testm1.jpg", 1)

dst = cv2.fastNlMeansDenoisingColored(src,None,10,10,7,21)

plt.subplot(121),plt.imshow(src)
plt.subplot(122),plt.imshow(dst)


tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,150,255,cv2.THRESH_OTSU)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)

cv2.imwrite("testm1.png", dst)
