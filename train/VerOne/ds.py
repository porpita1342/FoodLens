import json
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
foodinsseg_path = "/app/datasets/FoodInsSeg/annotations/Train.json"


with open(foodinsseg_path, 'r') as f:
    data = json.load(f)


# print(data['categories'])

for cat in data['categories']:
    print(f"{cat['id']}: {cat['name']}")