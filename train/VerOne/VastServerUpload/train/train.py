from ultralytics import YOLO
model = YOLO("yolo11n-seg.pt") 

results = model.train(data='dataset.yaml',epochs=500, imgsz=760, batch=64, device=[0,1,2,3])
