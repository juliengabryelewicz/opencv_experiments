import cv2
import numpy as np

img = cv2.imread("statue.jpg",cv2.IMREAD_GRAYSCALE)
img_canny = cv2.Canny(img, 200, 300)
cv2.imshow("Filtre de Canny sur 'Le penseur' de Rodin", img_canny)
cv2.waitKey()
cv2.destroyAllWindows()
