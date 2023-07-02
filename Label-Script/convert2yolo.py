import os
import json

def convert_to_yolo_format(annotations_file, dataset_folder):
    with open(annotations_file, 'r') as f:
        data = json.load(f)

    categories = {category['id']: category['name'] for category in data['categories']}

    class_ids = {
        'tower': 0,
        'insulator': 1,
        'spacer': 2,
        'damper': 3,
        'plate': 5
    }

    output_folder = 'Labels_YOLO'
    os.makedirs(output_folder, exist_ok=True)

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        annotation_lines = []
        for annotation in data['annotations']:
            if annotation['image_id'] == image_id:
                category_id = annotation['category_id']
                class_name = categories[category_id]
                class_id = class_ids.get(class_name)

                if class_id is not None:
                    bbox = annotation['bbox']

                    # Convert pixel-based coordinates to normalized coordinates
                    x = bbox[0] / width
                    y = bbox[1] / height
                    w = bbox[2] / width
                    h = bbox[3] / height

                    # Format the annotation line in YOLO format
                    annotation_line = f"{class_id} {x} {y} {w} {h}"
                    annotation_lines.append(annotation_line)

        # Save the annotations in a text file with the same name as the image
        image_path = os.path.join(dataset_folder, file_name)
        image_folder = os.path.dirname(image_path)
        image_name = os.path.basename(image_path)

        relative_folder_path = os.path.relpath(image_folder, dataset_folder)
        output_folder_path = os.path.join(output_folder, relative_folder_path)
        os.makedirs(output_folder_path, exist_ok=True)

        output_file = os.path.join(output_folder_path, os.path.splitext(image_name)[0] + '.txt')
        with open(output_file, 'w') as f_out:
            for line in annotation_lines:
                f_out.write(line + '\n')

        print(f"Annotations saved for {file_name}")

# Provide the path to your annotations JSON file
annotations_file = 'annotations.json'

# Provide the path to your dataset folder
dataset_folder = 'Dataset'

convert_to_yolo_format(annotations_file, dataset_folder)
