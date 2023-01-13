import numpy as np
import cv2

image = cv2.imread('mannequin.jpg')
mask = np.zeros(image.shape[:2], np.uint8)

backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

rect = (45, 45, 408, 612)
cv2.grabCut(image, mask, rect, backgroundModel, foregroundModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
image = image*mask2[:,:,np.newaxis]

cv2.imshow("Grabcut", image)
cv2.waitKey()
cv2.destroyAllWindows()