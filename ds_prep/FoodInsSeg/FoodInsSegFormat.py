import json
import os 
import numpy as np
PATH = "/home/porpita/CalEst/datasets/FoodInsSeg"
Clean_PATH = "/home/porpita/CalEst/datasets/FoodInsSeg/CleanAnnotations"
annotations = os.path.join(PATH, 'annotations')


for set in ['Test.json','Train.json']:

    setpath = os.path.join(annotations,set)
    save_path = os.path.join(Clean_PATH,set.replace('.json',''))
    os.mkdir(save_path)
    with open(setpath, 'r') as f:
        data = json.load(f)
    for image in data['images']:
        print(image) 
        txt_name = image['file_name'].replace('jpg', 'txt')
        x_max = image['width']
        print(f"==>> x_max: {x_max}")
        y_max = image['height']
        print(f"==>> y_max: {y_max}")
        id_target = image['id']
        print(f"==>> id_target: {id_target}")
        matches = [ann for ann in data['annotations'] if ann['image_id'] == id_target]
        print(len(matches))
        txt_file_path = os.path.join(save_path,txt_name)
        rows = []
        for m in matches:
            category_id = int(m['category_id'])
            coords = m['segmentation'][0]
            normalized = [
                val
                for x, y in zip(coords[::2], coords[1::2])
                for val in (x / x_max, y / y_max)
            ]
            row = [category_id] + normalized
            row_str = f"{row[0]} " + ' '.join(f"{v:.6f}" for v in row[1:])
            rows.append(row_str)


        with open(txt_file_path, "w") as f:
            for row in rows:
                f.write(row + "\n")