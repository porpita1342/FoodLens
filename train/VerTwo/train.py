from ultralytics import YOLO
model = YOLO("yolo11l-seg.pt") 

results = model.train(data='dataset.yaml',epochs=3, imgsz=896, batch=2, device=0)
