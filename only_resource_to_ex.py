import json
import pandas as pd

# JSON 파일 경로 설정
json_file = './resources_only.json'

# JSON 파일 읽기
with open(json_file, 'r') as f:
    data_list = json.load(f)

# 빈 리스트 생성
result_list = []

# 각 딕셔너리를 순회하며 데이터 추출
for data in data_list:
    cloud_partition = data.get('cloud_partition', '')
    region = data.get('region', '')
    name = data.get('name', '')
    group_name = data.get('group', {}).get('name', '')
    uid = data.get('uid', '')
    detail = data.get('data', '').get('details', '')
    ttype = data.get('type', '')

    # 데이터를 딕셔너리로 정리
    result_dict = {
        'Cloud Partition': cloud_partition,
        'Region': region,
        'detail' : detail,
        'Name': name,
        'Group Name': group_name,
        'type' : ttype,
        'UID': uid
    }

    # 결과 리스트에 추가
    result_list.append(result_dict)

# 결과 리스트를 데이터프레임으로 변환
df = pd.DataFrame(result_list)

# 엑셀 파일로 저장
excel_file = './only_resources.xlsx'
df.to_excel(excel_file, index=False)

print(f'엑셀 파일이 생성되었습니다: {excel_file}')
