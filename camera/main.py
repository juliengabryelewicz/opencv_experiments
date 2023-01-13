import cv2

camera= cv2.VideoCapture(0)
cv2.namedWindow('Camera')

success, frame = camera.read()
print("appuyez sur q pour arrêter la caméra")
while success and cv2.waitKey(1) == -1:
    cv2.imshow('Camera', frame)
    success, frame = camera.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyWindow('Camera')