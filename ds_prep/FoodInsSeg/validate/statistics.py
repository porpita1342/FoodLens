import matplotlib as plt
import json
import os

# foodinsseg_path = "/app/datasets/FoodInsSeg/annotations/Val.filtered.json"


# with open(foodinsseg_path, 'r') as f:
#     data = json.load(f)

# count = 0
# for image in data['images']:
#     if image['width'] < 500 and image['height']<500:
#         count += 1
# print(count)
# print(count/len(data['images'])) 
for path in ['train','val']:
    anno_path = "/app/datasets/FoodInsSeg/annotations"
    dir_path = "/app/datasets/FoodInsSeg/images"
    original_path = os.path.join(anno_path,f'{path.capitalize()}.json')
    filter_path = os.path.join(anno_path,f'{path.capitalize()}.filtered.json')
    with open(original_path, 'r') as f:
        ori_data = json.load(f)
    with open(filter_path, 'r') as f:
        fil_data = json.load(f)
    if path == 'test':
        dir_path = os.path.join(dir_path,'val')
    else:
        dir_path = os.path.join(dir_path,path)
    file_count = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
    print(f"Number of original images in the {path} set: {len(ori_data['images'])}")
    print(f"Number of filtered images in the {path} set: {len(fil_data['images'])}")
    print(f"Number of files in the {path} set: {file_count}")
