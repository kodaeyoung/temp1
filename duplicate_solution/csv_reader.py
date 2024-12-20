import csv
from collections import defaultdict

# CSV 파일 경로
csv_file_path = r'C:\Users\고대영\Downloads\기상예보\long_term_temp.csv'

# 중복을 체크할 사전 (주소+구분+이름을 키로 하고 해당 아이템을 값으로 저장)
address_combinations = defaultdict(list)

# CSV 파일을 읽고 중복 확인 로직
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # CSV의 각 행을 처리
    for idx, entry in enumerate(reader):
        # 중복 확인을 위한 키 설정 (CSV의 각 열을 사용하여 키 생성)
        # 해당 예시는 one, two, three 열을 사용하여 키를 생성
        key = f"{entry['TM_FC']}:{entry['TM_EF']}"
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
