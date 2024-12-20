import json
from collections import defaultdict

# 각 페이지의 JSON 데이터를 입력받는다
page_1_data = '''
[
    {
        "sample1": "1",
        "sample2": 1,
        "sample3": "1",
        "sample4": "1"
    },
    {
        "sample1": "1",
        "sample2": 1,
        "sample3": "1",
        "sample4": "1"
    }
]
'''

page_2_data = '''
[
    {
        "sample1": "4",
        "sample2": 4,
        "sample3": "4",
        "sample4": "4"
    },{
        "sample1": "4",
        "sample2": 4,
        "sample3": "4",
        "sample4": "4"
    }
]
'''

page_3_data = '''
[
    {
        "sample1": "4",
        "sample2": 4,
        "sample3": "4",
        "sample4": "4"
    },
    {
        "sample1": "6",
        "sample2": 6,
        "sample3": "6",
        "sample4": "6"
    },
    {
        "sample1": "1",
        "sample2": 1,
        "sample3": "1",
        "sample4": "1"
    }
 
]
'''

# 각 페이지 데이터를 파싱
data_page_1 = json.loads(page_1_data)
data_page_2 = json.loads(page_2_data)
data_page_3 = json.loads(page_3_data)

# 여러 페이지 데이터를 병합
all_data = data_page_1 + data_page_2+data_page_3

# 중복을 체크할 사
address_combinations = defaultdict(list)

# 중복 확인 로직
for idx, entry in enumerate(all_data):
    # 여기에 키 값을 넣어 주세요.
    key = f"{entry['sample1']}:{entry['sample2']}"
    address_combinations[key].append(entry)

# 중복된 항목을 출력
duplicates = {k: v for k, v in address_combinations.items() if len(v) > 1}

# 중복된 항목 개수 카운트
duplicate_count = sum(len(v) for v in duplicates.values())

# 결과 출력
if duplicates:
    print(f"중복된 항목이 총 {duplicate_count}개 있습니다.")
    for key, entries in duplicates.items():
        print(f"중복된 키: {key} (총 {len(entries)} 개)")
        for entry in entries:
            print(entry)
else:
    print("중복된 항목이 없습니다.")
