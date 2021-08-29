
"""
import methods cv2 and numpy.
cv2 installs: pip install opencv
numpy install: pip install numpy
"""
import cv2 as cv
import numpy as np

img = np.zeros((540,540,3), np.uint8)

cv.rectangle(img, (30, 30), (510, 510), (255, 255, 255), 2)

x0 = 30
y0 = 30
x1 = 90
y1 = 90

for i in range(8):
    for j in range(8):

        cv.rectangle(img, (x0, y0), (x1, y1), (255, 255, 255), 5,-1)
        if (j % 2==0 and i % 2==0) or (j % 2==1 and i % 2 ==1):
            cv.circle(img, (x0+30, y0+30), 33, (255,255,255), -2)

        y0 += 60
        y1 += 60

    x0 += 60
    x1 += 60
    y0 = 30
    y1 = 90


while True:
    cv.imshow('img', img)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("chess_board.png", img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()

