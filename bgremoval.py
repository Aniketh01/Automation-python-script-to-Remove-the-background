import cv2
file_name = "testm1.jpg"

src = cv2.imread("/home/aniketh/KStars: SoK/testm1.jpg", 1)
tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,150,255,cv2.THRESH_OTSU)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("testm1.png", dst)
