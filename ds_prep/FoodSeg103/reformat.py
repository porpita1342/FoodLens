from ultralytics.data.converter import convert_segment_masks_to_yolo_seg
import os

# Define the path to your directory of mask images
PATH = "/app/CalEst/datasets/foodseg103/FoodSeg103/Images/ann_dir"
total_classes = 104

for ds in ['test_ori','train_ori']:
    save_ds = ds.split('_')[0]
    masks_directory =os.path.join(PATH, ds)
    output_directory = os.path.join(PATH,save_ds)
    os.makedirs(output_directory)
    convert_segment_masks_to_yolo_seg(
        masks_dir=masks_directory,
        output_dir=output_directory,
        classes=total_classes
    )
