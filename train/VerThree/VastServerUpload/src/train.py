from ultralytics import YOLO

# Load a pretrained segmentation model
model = YOLO('yolo11l-seg.pt')

# Train the model with your specified configurations
results = model.train(
    # --- Core Task and Data ---
    data='dataset.yaml',
    epochs=500,
    imgsz=896,
    batch=0.70,
    patience=100,
    device=[0,1,2,3],


    # --- Most Effective Augmentation Settings for Segmentation ---
    augment=True,         # Master switch to enable manual augmentation
    mosaic=1.0,           # Recommended: combines 4 images
    copy_paste=0.5,       # Highly Recommended: copies objects to new backgrounds
    degrees=180,         # Rotation range
    translate=0.1,        # Translation range
    scale=0.5,            # Scale/zoom range
    flipud=0.5,          
    hsv_h=0.015,          # Color hue variation
    hsv_s=0.7,        
    hsv_v=0.4,      

)


