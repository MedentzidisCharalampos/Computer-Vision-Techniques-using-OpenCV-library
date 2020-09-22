import numpy as np
import cv2 as cv

img = cv.imread('chessboard.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corner = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)

corners = np.int0(corner)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()


