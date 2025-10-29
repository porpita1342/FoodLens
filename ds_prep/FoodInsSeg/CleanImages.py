import json
import os

dataset = "/app/datasets/FoodInsSeg"

for ds in ["Train.json", "Val.json"]:
    ann_path = os.path.join(dataset, "annotations", ds)
    with open(ann_path, "r") as f:
        data = json.load(f)

    # derive subset name: "train" / "test"
    dset = os.path.splitext(ds.lower())[0]

    image_dir = os.path.join(dataset, "images", dset)
    label_dir = os.path.join(dataset, "labels", dset)

    # collect deletions using direct indexing
    deleted_images = []
    count = 0
    for image in data["images"]:
        if image["width"] < 500 and image["height"] < 500:
            deleted_images.append(image["file_name"])
            count += 1

    print(f"{count} images to be deleted in {dset}")

    # 1. Filter JSON: remove images and their annotations
    to_delete = set(deleted_images)
    keep_images = [im for im in data["images"] if im["file_name"] not in to_delete]
    keep_ids = {im["id"] for im in keep_images}
    keep_annotations = [ann for ann in data["annotations"] if ann["image_id"] in keep_ids]

    # Update data
    data["images"] = keep_images
    data["annotations"] = keep_annotations

    out_name = os.path.splitext(ds)[0] + ".filtered.json"
    out_path = os.path.join(dataset, "annotations", out_name)
    with open(out_path, "w") as f:
        json.dump(data, f)
    print(f"Filtered JSON saved to {out_path} (images: {len(keep_images)}, annotations: {len(keep_annotations)})")

    for filename in deleted_images:
        rel = filename.lstrip("/")
        subdir = os.path.dirname(rel)
        stem, _ = os.path.splitext(os.path.basename(rel))

        if os.path.sep in rel:
            img_path = os.path.normpath(os.path.join(dataset, "images", rel))
        else:
            img_path = os.path.join(image_dir, rel)

        if os.path.exists(img_path):
            os.remove(img_path)
            print(f"Image {filename} removed")
        else:
            print(f"Image {filename} not found, skipping")

        lbl_dir = os.path.join(label_dir, subdir) if subdir else label_dir
        lbl_path = os.path.join(lbl_dir, f"{stem}.txt")

        if os.path.exists(lbl_path):
            os.remove(lbl_path)
            print(f"Label {stem}.txt removed")
        else:
            print(f"Label {stem}.txt not found, skipping")
