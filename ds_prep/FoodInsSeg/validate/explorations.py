import json
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
foodinsseg_path = "/app/datasets/FoodInsSeg/annotations/Test.json"

with open(foodinsseg_path, 'r') as f:
    data = json.load(f)

cat = set([n for n in range(1,104)])
categories = {each['id']: each['name'] for each in data['categories']}

complete = False
path = []
coords = []
n = -1
while len(cat) != 0:
    n += 1 
    sample = data['images'][n]
    path.append((sample['id'],sample['file_name']))
    
    for ann in data['annotations']:
        if ann['image_id'] == sample['id']:
            cat_present = ann['category_id']
            if cat_present in cat:
                print(cat,len(cat),len(coords)) 
                
                cat.remove(cat_present)
            # breakpoint()
            coords.append((ann['image_id'],ann['category_id'],ann['segmentation'][0]))

save_path = "/app/ds_prep/validate/validate_labels"
read_path = "/app/datasets/FoodInsSeg/images/val"
for image_id, image_fname in path:
    img_path = os.path.join(read_path,image_fname)
    # print(f"==>> img_path: {img_path}")
    img = cv2.imread(img_path)
    # print(f"==>> img: {img}")
    overlay = img.copy()
    for seg in coords:
        if seg[0] == image_id: 
            points = np.array(seg[2], dtype=np.int32).reshape((-1, 2))
            cv2.polylines(img, [points], isClosed=True, color=(255, 0, 0), thickness=2)  # Outline on original
            cv2.fillPoly(overlay, [points], color=(0, 0, 255)) 
            name = f"{seg[1]}:{categories[seg[1]]}"
            cv2.putText(img=img,text=name,org=points[0],
                        fontFace=cv2.FONT_HERSHEY_PLAIN,
                        fontScale=1.0, color=[0,0,255])   
    alpha = 0.5
    result = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
    fname = os.path.join(save_path,str(random.randint(1,90)))
    fname = fname + '.png'
    cv2.imwrite(fname,img)





"""
CAT_ID = [1:104] OF INTEG
"""