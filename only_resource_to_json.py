import json

json_file_path = "C:/Users/eggra/Downloads/prowler_aws/prowler-output-553153918398-20240610071217.ocsf.json"

with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

resource_data = []
for item in data:
    if 'resources' in item:
        resource_data.extend(item['resources'])

output_file_path = "resources_only.json"
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    json.dump(resource_data, outfile, ensure_ascii=False, indent=4)

print(f"리소스 데이터가 성공적으로 저장되었습니다: {output_file_path}")
