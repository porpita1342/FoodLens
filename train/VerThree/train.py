from ultralytics import YOLO
model = YOLO("yolo11n-seg.pt") 

results = model.train(data='dataset.yaml',epochs=500, imgsz=896, batch=0.70, device=[0,1,2,3], degrees=180)
