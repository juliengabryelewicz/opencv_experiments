import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)
success, frame = camera.read()
print("appuyez sur q pour arrêter la caméra")
while success and cv2.waitKey(1) == -1:
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('Détection de visage', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
