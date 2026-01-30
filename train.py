from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train using built-in COCO128 dataset
model.train(
    data="coco128.yaml",
    epochs=10,
    imgsz=640,
    batch=8
)
