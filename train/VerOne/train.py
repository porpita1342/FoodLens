from ultralytics import YOLO
model = YOLO("yolo11n-seg.pt") 


results = model.train(data='dataset.yaml',epochs=3, imgsz=640, batch=0.70, device=[0,1,2,3])
