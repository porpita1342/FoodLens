import json
foodinsseg_path = "/app/datasets/FoodInsSeg/annotations/Test.json"
with open(foodinsseg_path, 'r') as f:
    data = json.load(f)


categories = {each['id']: each['name'] for each in data['categories']}
print(f"==>> categories: {categories}")
