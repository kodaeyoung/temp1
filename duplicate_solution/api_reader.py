import json
import ssl
import requests
from collections import defaultdict



# API URL (예시 URL, 실제 URL로 교체 필요)
api_url = "https://apis.data.go.kr/B500001/dam/sluicePresentCondition/hourlist?serviceKey=SIUur%2BOiMwCpJ0MLF4G7ZPqn5MDLjsJs47dNh6Os3fBj%2F823gaocBiSkZjtGclEOazC1hSguty0g6DKzD6EQ4w%3D%3D&pageNo=1&numOfRows=300&damcode=1003110&stdt=2024-11-11&eddt=2024-11-12&_type=json"

# API 호출
response = requests.get(api_url, verify=True)  # SSL 검증 비활성화

# 응답이 정상적인지 확인
if response.status_code == 200:
    # JSON 데이터 파싱
    data = response.json()

    # 중복을 체크할 사전 (주소+구분+이름을 키로 하고 해당 아이템을 값으로 저장)
    address_combinations = defaultdict(list)

    # 중복 확인 로직
    for idx, entry in enumerate(data):
        key = f"{entry['gubun']}:{entry['stdDay']}:{entry['defCnt']}"
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
else:
    print(f"API 호출에 실패했습니다. 상태 코드: {response.status_code}")
