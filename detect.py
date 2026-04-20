import cv2
from ultralytics import YOLO

model = YOLO('runs/detect/train4/weights/best.pt')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Camera read failed')
        break

    results = model(frame, conf=0.4)
    annotated = results[0].plot()

    cv2.imshow('YOLOv8 Real-Time Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
