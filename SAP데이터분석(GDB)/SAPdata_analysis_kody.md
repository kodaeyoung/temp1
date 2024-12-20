## GDB 에서 사용하는 용어

  - 라벨 : 각 노드의 유형을 구분하는 기본적인 방법. 주로 `테이블 명`이 `라벨`이 됨.
  - 노드: `개체`를 의미. 주로 테이블에 속해있는 `각각의 개체(행)`가 하나의 노드가 됨.
  - 간선: `노드간의 관계`를 의미. 일반적으로 `외래키`가 가리키는 테이블 간의 관계를 적절한 의미 있는 방향성과 이름을 가진 간선으로 변환 
  - Cypher: Neo4j에서 사용되는 `쿼리 언어`, 그래프 데이터를 조회, 삽입, 업데이트, 삭제하는 데 사용됩니다.
 
 ### cyper 문법 정리
  1. create 노드 생성 쿼리
  ```cyper
      CREATE (u:User {ID: 1, 이름: '홍길동', 나이: 30})
  ```

  User 라벨을 가진 노드를 생성하고, ID, 이름, 나이 속성을 부여합니다.

  2. 관계(간선) 생성 (CREATE)   
  ```cyper
        MATCH (u:User {ID: 1}), (c:City {이름: '서울'})
        CREATE (u)-[:LIVES_IN]->(c)
  ```
  User 노드와 City 노드를 찾고, 이들 간에 LIVES_IN이라는 관계를 생성합니다.

  ```cyper
        MATCH (u1:User), (u2:User)
        WHERE u1.나이 = u2.나이 AND u1.도시 = u2.도시 AND id(u1) < id(u2)
        CREATE (u1)-[:SAME_AGE_AND_CITY]->(u2)
  ```

  WHERE 조건문에 맞는 User노드를 찾아서 관계(간선) 생성
  예시에서는 나이가 같고 같은 도시에 사는 사용자끼리 같은 (같은 도시,같은 나이)의 관계(간선) 생성



# address, Business Parter, employee (+ sales orders)에 대한 노드와 엣지 관계

##  `Addresses.csv` 파일 분석

  - 속성 
     - `ADDRESSID`: 주소를 식별하는 고유 ID.
     - `CITY`: 주소가 위치한 도시.
     - `POSTALCODE`: 우편번호.
     - `STREET`: 거리 이름.
     - `BUILDING`: 건물 번호.
     - `COUNTRY`: 국가 코드 (예: US).
     - `REGION`: 지역 코드 (예: AMER).
     - `ADDRESSTYPE`: 주소 유형을 나타내는 코드.
     - `VALIDITY_STARTDATE`: 주소의 유효 시작일 (YYYYMMDD 형식).
     - `VALIDITY_ENDDATE`: 주소의 유효 종료일 (YYYYMMDD 형식).
     - `LATITUDE`: 위도 좌표.
     - `LONGITUDE`: 경도 좌표.
     
  - 생성 될 노드의 개수 : 54개 
  - 라벨명 : Addresses

  #### Addresses 노드 생성 cyper 예시
  - 노드 생성
  ```cyper
    CREATE (a:Addresses {
        ADDRESSID: 1000000034,
        CITY: 'West Nyack',
        POSTALCODE: '10994',
        STREET: 'Settlers Lane',
        BUILDING: 5027,
        COUNTRY: 'US',
        REGION: 'AMER',
        ADDRESSTYPE: 2,
        VALIDITY_STARTDATE: date('2000-01-01'),
        VALIDITY_ENDDATE: date('9999-12-31'),
        LOCATION: point({latitude: 41.100057, longitude: -73.973562})
    })

  ```

  ##### 데이터 타입 지정
  - `ADDRESSID` , `BUILDING`, `ADDRESSTYPE` : 문자 타입이 포함되어 있지 않음. 숫자 타입으로 저장
  - `CITY` , `POSTALCODE` , `STREET` , `CONTRY`, `REGION` : 문자 타입이 포함되어 있어 문자형으로 저장
  - `VALIDITY_STARTDATE` 와 `VALIDITY_ENDDATE`는 `date()` 내장함수를 사용하여 날짜형식으로 저장
  - `LATITUDE` 와 `LONGITUDE` 는 point로 묶어 지리적 좌표를 표현





  ## `BusinessPartners.csv` 파일 분석
  - 속성
    - `PARTNERID`: 비즈니스 파트너를 식별하는 고유 ID
     - `PARTNERROLE`: 비즈니스 파트너의 역할을 나타내는 코드
     - `EMAILADDRESS`: 파트너의 이메일 주소
     - `PHONENUMBER`: 파트너의 전화번호
     - `FAXNUMBER`: 파트너의 팩스 번호 (결측값이 많음)
     - `WEBADDRESS`: 파트너의 웹사이트 주소
     - `ADDRESSID`: 주소 ID로, `Addresses.csv`와 연결될 수 있는 외래 키
     - `COMPANYNAME`: 회사 이름
     - `LEGALFORM`: 회사의 법적 형태 (예: Inc., LLC 등)
     - `CREATEDBY`: 레코드 생성자 ID
     - `CREATEDAT`: 레코드 생성 날짜 (YYYYMMDD 형식)
     - `CHANGEDBY`: 마지막으로 변경한 사용자 ID
     - `CHANGEDAT`: 마지막으로 변경한 날짜 (YYYYMMDD 형식)
     - `CURRENCY`: 사용되는 통화 코드 (예: USD)

  - 생성될 노드의 개수 : 40개 
  - 라벨명: BusinessPartners

  #### BusinessPartners 노드 생성 cyper 예시
  - 노드 생성
   ```cyper
      CREATE (b:BusinessPartners {
          PARTNERID: 100000022,
          PARTNERROLE: 2,
          EMAILADDRESS: 'maria.brown@all4bikes.com',
          PHONENUMBER: '622734567',
          FAXNUMBER: NULL,
          WEBADDRESS: 'http://www.all4bikes.com',
          ADDRESSID: 1000000034,
          COMPANYNAME: 'All For Bikes',
          LEGALFORM: 'Inc.',
          CREATEDBY: 10,
          CREATEDAT: date('2018-10-03'),
          CHANGEDBY: 10,
          CHANGEDAT: date('2023-10-03'),
          CURRENCY: 'USD'
      })
  ```
      
  ##### 데이터 타입 지정
  - `PARTNERID` , `PARTNERROLE` , `ADDRESSID` , `CREATEDBY` , `CHANGEDBY` : 숫자 타입으로 지정
  - `EMAILADDRESS` , `PHONENUMBER` , `WEBADDRESS` , `COMPANYNAME` , `LEGALFORM` , `CURRENCY` : 문자 타입으로 지정
  - `CREATEDAT` , `CHANGEDAT` : date() 함수 사용하여 날짜 형식으로 지정

  ###### 특이사항
  - `FAXNUMBER` 속성에 해당하는 값은 하나도 없음.






 ## `Employees.csv` 파일 분석 
  - 속성
    - `EMPLOYEEID`: 직원의 고유 ID
    - `NAME_FIRST`: 직원의 이름
    - `NAME_MIDDLE`: 직원의 중간 이름
    - `NAME_LAST`: 직원의 성
    - `NAME_INITIALS`: 이름의 이니셜
    - `SEX`: 성별 (예: M, F)
    - `LANGUAGE`: 사용 언어 (예: E는 영어)
    - `PHONENUMBER`: 직원의 전화번호
    - `EMAILADDRESS`: 직원의 이메일 주소
    - `LOGINNAME`: 직원의 로그인 이름
    - `ADDRESSID`: 주소 ID로, `Addresses.csv`와 연결될 수 있는 외래 키
    - `VALIDITY_STARTDATE`: 직원 정보의 유효 시작일 (YYYYMMDD 형식)
    - `VALIDITY_ENDDATE`: 직원 정보의 유효 종료일 (YYYYMMDD 형식)   

  - 생성될 노드의 개수 : 14개
  - 라벨명 : Employees


  #### Employees 노드 생성 cyper 예시
  - 노드 생성
  ```
    CREATE (e:Employees {
        EMPLOYEEID: 1,
        NAME_FIRST: 'Derrick',
        NAME_MIDDLE: 'L',
        NAME_LAST: 'Magill',
        NAME_INITIALS: NULL,
        SEX: 'M',
        LANGUAGE: 'E',
        PHONENUMBER: '630-374-0306',
        EMAILADDRESS: 'derrick.magill@itelo.info',
        LOGINNAME: 'derrickm',
        ADDRESSID: 1000000001,
        VALIDITY_STARTDATE: date('2020-01-01'),
        VALIDITY_ENDDATE: date('2025-12-31')
        })
  ```

  ##### 데이터 타입 지정
  - `EMPLOYEEID` , `ADDRESSID`: 숫자 타입으로 지정
  - `NAME_FIRST` , `NAME_MIDDLE` , `NAME_LAST` , `NAME_INITIALS` , `SEX` , `LANGUAGE` , `PHONENUMBER` , `EMAILADDRESS` , `LOGINNAME` : 문자로 지정
  - `VALIDITY_STARTDATE` , `VALIDITY_ENDDATE` : 날짜 형식으로 지정

  ###### 특이 사항
  - csv 파일 9번째 줄 `NAME_INITIALS` 부터 한칸 씩 밀림
  - `PHONENUMBER` 속성의 데이터 형식 일관성이 없음




## `SalesOrders.csv` 파일 분석
  - 속성
     - `SALESORDERID`: 판매 주문을 식별하는 고유 ID (`SalesOrderItems.csv`와 연결 가능)
     - `CREATEDBY`: 레코드를 생성한 사용자 ID
     - `CREATEDAT`: 주문 생성 날짜 (YYYYMMDD 형식)
     - `CHANGEDBY`: 마지막으로 변경한 사용자 ID
     - `CHANGEDAT`: 마지막으로 변경된 날짜 (YYYYMMDD 형식)
     - `FISCVARIANT`: 회계 변형 코드
     - `FISCALYEARPERIOD`: 회계 연도 기간
     - `NOTEID`: 추가 노트 ID (현재 데이터에서 사용되지 않음)
     - `PARTNERID`: 비즈니스 파트너 ID (`BusinessPartners.csv`와 연결 가능)
     - `SALESORG`: 판매 조직 코드
     - `CURRENCY`: 통화 코드 (예: USD)
     - `GROSSAMOUNT`: 총 금액
     - `NETAMOUNT`: 순 금액
     - `TAXAMOUNT`: 세금 금액
     - `LIFECYCLESTATUS`: 주문 생명 주기 상태 코드
     - `BILLINGSTATUS`: 청구 상태 코드
     - `DELIVERYSTATUS`: 배송 상태 코드

  생성될 노드의 개수 : 334개
  라벨명 : SalesOrders

   #### SalesOrders 노드 생성 cyper 예시
  - 노드 생성
  ```
    CREATE (s:SalesOrders {
        SALESORDERID: 500000000,
        CREATEDBY: 4,
        CREATEDAT: date('2018-01-11'),
        CHANGEDBY: 4,
        CHANGEDAT: date('2018-01-16'),
        FISCVARIANT: 'K4',
        FISCALYEARPERIOD: 2018001,
        NOTEID: NULL, -- NoteID가 없는 경우 NULL로 처리
        PARTNERID: 100000022,
        SALESORG: 'APJ',
        CURRENCY: 'USD',
        GROSSAMOUNT: 13587,
        NETAMOUNT: 11888.625,
        TAXAMOUNT: 1698.375,
        LIFECYCLESTATUS: 'C',
        BILLINGSTATUS: 'C',
        DELIVERYSTATUS: 'C'
    })
   ```

  ##### 데이터 타입 지정
  - `SALESORDERID` , `CREATEDBY` , `CHANGEDBY` , `FISCALYEARPERIOD` , `PARTNERID` , `GROSSAMOUNT` , `NETAMOUNT` , `TAXAMOUNT` : 숫자 타입 지정
  - ` FISCVARIANT` , `SALESORG` , `CURRENCY` , ` LIFECYCLESTATUS` , `BILLINGSTATUS` , `DELIVERYSTATUS` : 문자 타입 지정
  - `CREATEDAT` , `CHANGEDAT` : date()함수 사용하여 날짜 형식 지정

  ###### 특이 사항  
        - `NOTEID` : 해당 값이 모두 비어있음


  ### 간선(관계)
  - Employees 노드와 Addresses 노드 중 속성 `ADDRESSID`가 같은 노드들끼리 간선 생성
  - BusinessPartners 노드와 Addresses 노드 중 속성 `ADDRESSID`가 같은 노드들끼리 간선 생성
  - SalesOrders 노드와 BusinessPartners 노드 중 속성 `PARTNERID`가 같은 노드들끼리 간선 생성

  #### 간선 생성 cyper 예시

  ```cyper
      MATCH (a:Addresses), (e:Employees)
      WHERE a.ADDRESSID = e.ADDRESSID
      CREATE (e)-[:LOCATED_AT]->(a)
   ```

   Addresses 라벨을 가진 노드와 Employees 라벨을 가진 노드 중 ADDRESSID가 같은 노드들 사이의 LOCATED_AT이라는 간선을 생성.

   ```cyper
      MATCH (a:Addresses), (b:BusinessPartners)
      WHERE a.ADDRESSID = b.ADDRESSID
      CREATE (b)-[:LOCATED_AT]->(a)
   ```

  Addresses 라벨을 가진 노드와 BusinessPartners 라벨을 가진 노드 중 ADDRESSID가 같은 노드들 사이의 LOCATED_AT이라는 간선을 생성.

  ```cyper
      MATCH (s:SalesOrders), (b:BusinessPartners)
      WHERE s.PARTNERID = b.PARTNERID
      CREATE (s)-[:RELATED_TO]->(b)
  ```




  ### docker 실행 중 로컬 호스트의 파일을 neo4j import 디렉터리에 업로드
  ```
    docker cp "C:\Users\고대영\OneDrive - Dtonic Corp\인턴십활동\SAP 데이터 분석\SAP_archive\Addresses.csv" neo4j:/var/lib/neo4j/import/
  ```


###### csv 파일을 onnx파일로 변환하고, onnx파일을 neo4j에 파싱하여 graphsql 생성 

 ##### 1. csv 파일을 로드하여 onnx 형식으로 변환
  ```python
    import pandas as pd
    import onnx
    from onnx import helper, TensorProto
    import numpy as np

    # CSV 파일 로드
    csv_file = '/path/to/your/csvfile.csv'  # 실제 CSV 파일 경로로 변경
    data = pd.read_csv(csv_file)

    # CSV 데이터 확인
    print(data.head())

    # NumPy 배열로 변환
    array_data = data.values  # CSV 데이터를 NumPy 배열로 변환

    # ONNX 텐서 생성
    tensor = helper.make_tensor(
        name='csv_tensor',  # 텐서 이름
        data_type=TensorProto.STRING,  # 모든 데이터를 문자열로 처리 (필요에 따라 수정 가능)
        dims=array_data.shape,  # 데이터의 차원 (행, 열)
        vals=array_data.flatten().tolist()  # 데이터를 일렬로 변환하여 저장
    )

    # 그래프 생성 (노드 없음, 텐서 초기화만 사용)
    graph = helper.make_graph(
        nodes=[],  # 노드 없음
        name='csv-to-onnx',
        inputs=[],  # 입력 텐서 정의 안함
        outputs=[],  # 출력 텐서 정의 안함
        initializer=[tensor]  # 초기화된 텐서
    )

    # 모델 생성 및 ONNX 파일로 저장
    model = helper.make_model(graph)
    onnx.save(model, 'address_data.onnx')  # ONNX 파일로 저장

    print("CSV 데이터를 ONNX 파일로 변환 완료")

  ```


  ##### 2. Neo4j 데이터베이스 연결

Neo4j에 연결하기 위해 Python의 neo4j 라이브러리를 사용함.
아래 코드 스니펫을 입력하기 전에 비밀번호를 설정함.

  ```python
      from neo4j import GraphDatabase
      import onnx
      import numpy as np
      from onnx import numpy_helper

      # Neo4j 데이터베이스 URI와 인증 정보 설정
      uri = "bolt://localhost:7687"
      driver = GraphDatabase.driver(uri, auth=("neo4j", "{password}"))

      def close_driver():
          driver.close()
  ```

  ##### 3. Neo4j에 데이터 삽입

  ```python
      # ONNX 모델 로드
      model = onnx.load('address_data.onnx')

      # ONNX에서 텐서 추출
      tensor_data = None
      for tensor in model.graph.initializer:
          if tensor.name == 'csv_tensor':
              tensor_data = numpy_helper.to_array(tensor)  # ONNX 텐서를 NumPy 배열로 변환

      # NumPy 배열을 리스트로 변환
      rows = tensor_data.tolist()

      # Neo4j에 데이터 삽입 함수
      def insert_address(tx, row):
          query = """
          CREATE (a:Address { 
              address_id: $address_id, 
              city: $city, 
              postal_code: $postal_code, 
              street: $street, 
              building: $building, 
              country: $country, 
              region: $region, 
              address_type: $address_type, 
              validity_start: $validity_start, 
              validity_end: $validity_end, 
              latitude: $latitude, 
              longitude: $longitude
          })
          """
          tx.run(query, 
                address_id=row[0], city=row[1], postal_code=row[2], street=row[3], building=row[4], 
                country=row[5], region=row[6], address_type=row[7], validity_start=row[8], 
                validity_end=row[9], latitude=row[10], longitude=row[11])

      # Neo4j에 데이터 삽입
      with driver.session() as session:
          for row in rows:
              session.write_transaction(insert_address, row)

      # 세션 종료
      close_driver()
      print("Neo4j에 데이터 삽입 완료")
  ```




  ###### 자동화

   1. CSV 파일을 ONNX 파일로 변환하는 로직

  ```python
      import pandas as pd
      import numpy as np
      import onnx
      from onnx import helper, TensorProto

      # 데이터 타입별 ONNX 텐서 생성 함수
      def create_tensor(column_name, data, dtype):
          if dtype == 'int64':
              return helper.make_tensor(column_name, TensorProto.INT64, [len(data)], data.astype(np.int64))
          elif dtype == 'float64':
              return helper.make_tensor(column_name, TensorProto.FLOAT, [len(data)], data.astype(np.float32))
          elif dtype == 'object':  # 문자열 데이터 처리
              return helper.make_tensor(column_name, TensorProto.STRING, [len(data)], data.astype(str).tolist())
          else:
              raise ValueError(f"Unsupported dtype: {dtype}")

      # CSV에서 데이터 타입을 추론하여 ONNX 모델 생성
      def csv_to_onnx(csv_file, onnx_file):
          # CSV 파일 로드
          df = pd.read_csv(csv_file)

          # 열 이름과 데이터 타입 분석
          tensors = []
          for column in df.columns:
              dtype = df[column].dtype.name
              tensor = create_tensor(column, df[column].values, dtype)
              tensors.append(tensor)

          # ONNX 그래프 생성 (노드 없이 텐서 초기화만 사용)
          graph = helper.make_graph(
              nodes=[],  # 노드 없음
              name='csv-to-onnx',
              inputs=[],  # 입력 텐서 정의 없음
              outputs=[],  # 출력 텐서 정의 없음
              initializer=tensors  # 모든 텐서 초기화
          )

          # ONNX 모델 생성 및 저장
          model = helper.make_model(graph)
          onnx.save(model, onnx_file)
          print(f"ONNX 파일 생성 완료: {onnx_file}")

      # 실행 예시
      csv_file = r'C:\Users\고대영\gdb_env\SAP_archive\Addresses.csv'  # CSV 파일 경로
      onnx_file = r'C:\Users\고대영\gdb_env\onnx'  # ONNX 파일 저장 경로

      # CSV 파일을 ONNX 파일로 변환
      csv_to_onnx(csv_file, onnx_file)

  ```

  2. ONNX 파일을 Neo4j에 적재하는 로직

  ```python

    import onnx
    import onnx
    from onnx import numpy_helper
    from neo4j import GraphDatabase

    # Neo4j 데이터베이스 URI와 인증 정보 설정
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "{password}"))

    def close_driver():
      driver.close()


    # ONNX 파일에서 데이터를 추출하고 Neo4j에 적재하는 함수
    def onnx_to_neo4j(onnx_file, label_name):
        # ONNX 파일 로드
        model = onnx.load(onnx_file)

        # ONNX 텐서에서 데이터를 추출하는 함수
        def extract_tensor(tensor_name):
            for tensor in model.graph.initializer:
                if tensor.name == tensor_name:
                    return numpy_helper.to_array(tensor)

        # 텐서 데이터 추출
        data_dict = {}
        for tensor in model.graph.initializer:
            data_dict[tensor.name] = extract_tensor(tensor.name)

        # Neo4j에 데이터 삽입 함수 정의
        def insert_data(tx, row_dict):
            columns = ", ".join([f"{key}: ${key}" for key in row_dict.keys()])
            query = f"CREATE (a:{label_name} {{{columns}}})"
            tx.run(query, **row_dict)

        # Neo4j에 데이터 삽입
        with driver.session() as session:
            for i in range(len(next(iter(data_dict.values())))):  # 첫 열을 기준으로 개수만큼 반복
                row_dict = {key: data_dict[key][i] for key in data_dict.keys()}
                session.write_transaction(insert_data, row_dict)

        print(f"Neo4j에 데이터 삽입 완료")

    # 실행 예시
    onnx_file = '/path/to/save/onnxfile.onnx'  # ONNX 파일 경로
    label_name = 'Address'  # Neo4j에 생성될 노드 레이블 이름

    # ONNX 파일을 Neo4j에 적재
    onnx_to_neo4j(onnx_file, label_name)

    # Neo4j 세션 종료
    close_driver()
  ```




  ### ----------------------------------------------neo4j 라벨명이 노드 이름으로 표시되게 하기

  1. 밑에 cyper 명령을 실행하여 모든 노드에 name이라는 속성이 생기도록 하고, 해당 name속성에는 라벨명이 들어가게 한다.
  
    MATCH (n)
    SET n.name = head(labels(n))
    RETURN n  
    
  2. 표시되는 속성을 name으로 설정한다.

  ### neo4j 모든 노드 삭제하기

    MATCH (n)
    DETACH DELETE n
    



  ### 특정 라벨의 노드만 조회하기

    MATCH (n:Label1)
    RETURN n
    UNION
    MATCH (n:Label2)
    RETURN n

  ### 특정 노드와 연결된 노드와 엣지 보기
    MATCH (bp:BusinessPartners {PARTNERID: 300})-[r]-(connectedNode)
    RETURN bp, r, connectedNode

  ### 특정 노드와 연결된 연쇄적인 노드와 엣지 보기

    MATCH (bp:BusinessPartners {PARTNERID: 100000027})-[r*1..3]-(connectedNode)
 RETURN bp, r, connectedNode