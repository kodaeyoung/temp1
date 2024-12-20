import json
from collections import defaultdict

# 입력받을 JSON 데이터
json_data = '''
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
    },
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
    },{
        "sample1": "5",
        "sample2": 5,
        "sample3": "5",
        "sample4": "5"
    }
]
'''

# JSON 데이터를 파싱
data = json.loads(json_data)

# 중복을 체크할 사전 (주소+구분+이름을 키로 하고 해당 아이템을 값으로 저장)
address_combinations = defaultdict(list)

# 중복 확인 로직
for idx, entry in enumerate(data):
    # 여기에 키 값을 넣어 주세요.
    key = f"{entry['sample1']}:{entry['sample2']}:{entry['sample3']}"
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

