import json5
import json

# Open with json5 due to some trailing commas
with open('data/dataset.json', 'r', encoding="utf8") as f:
    data = json5.load(f)

flattened_data = []

for item in data:
    if isinstance(item, dict):
        flattened_data.append(item)
    elif isinstance(item, list):
        flattened_data.extend(item)

with open('data/dataset_flat.json', 'w', encoding='utf-8') as f:
    json.dump(flattened_data, f, ensure_ascii=False, indent=4)