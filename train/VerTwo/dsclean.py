path = "/app/CalEst/datasets/foodseg103/FoodSeg103/category_id.txt"
final = []
with open(path,'r') as f:
    content = f.readlines()
    for line in content:
        line = line.strip().split(maxsplit=1)
        line[0] = str(int(line[0]) - 1 )
        final.append(": ".join(line))

final = final[1:]
with open('temp.txt','w') as f:
    for line in final:
        f.write(f'{line}\n')
