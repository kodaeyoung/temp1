# SAP data 분석 리포트

## 간단한 데이터 분석 보고서 목차

1. 서론
   - 분석 목적
   - 데이터 출처와 파일 설명

2. 데이터 개요
   - 각 파일의 데이터 구조와 주요 내용 설명
   - 데이터 간 관계 요약

## 분석 목적 및 파일 설명

분석 목적: GraphDB에 저장시키기 전에 데이터를 분석하여 특성과 특이 사항을 미리 파악하고 원할히 작업하기 위함

내부 파일 종류:
    Addresses.csv
    BusinessPartners.csv
    Employees.csv
    ProductCategories.csv
    ProductCategoryText.csv
    Products.csv
    ProductTexts.csv
    SalesOrderItems.csv
    SalesOrders.csv

## 데이터 개요

각 파일의 데이터 구조와 주요 내용을 설명합니다.

### `Addresses.csv` 파일 분석

1. 파일 구조:
   - 주소 관련 정보를 포함
   - 주요 컬럼:
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

2. 데이터 유형:
   - `ADDRESSID`, `CITY`, `POSTALCODE`, `STREET`, `COUNTRY`, `REGION`, `ADDRESSTYPE`: 문자형 또는 문자열 (String).
   - `BUILDING`: 숫자형 (Float)으로 보이며, 건물 번호를 나타내는 것으로 추정됨.
   - `VALIDITY_STARTDATE`, `VALIDITY_ENDDATE`: 날짜형 데이터 (YYYYMMDD 형식의 문자열로 저장).
   - `LATITUDE`, `LONGITUDE`: 숫자형 (Float)으로, 주소의 지리적 좌표를 나타냄.

3. 특이사항 및 주의점:
   - 날짜 필드 (`VALIDITY_STARTDATE`, `VALIDITY_ENDDATE`)는 문자열로 저장되어 있어, 날짜로 변환하여 사용하는 것 권장.
   - 주소 데이터 (`CITY`, `STREET`, `POSTALCODE` 등)는 여러 파일에서 사용할 수 있는 중요한 연결 키 가능성.
   - 위도 및 경도가 포함되어 있어, 지도 시각화나 공간 분석 가능성 존재.

### `BusinessPartners.csv` 파일 분석

1. 파일 구조
   - 비즈니스 파트너 정보 포함
   - 주요 컬럼:
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

2. 데이터 유형
   - `PARTNERID`, `PARTNERROLE`, `ADDRESSID`, `CREATEDBY`, `CHANGEDBY`: 정수형 (Integer)
   - `EMAILADDRESS`, `PHONENUMBER`, `FAXNUMBER`, `WEBADDRESS`, `COMPANYNAME`, `LEGALFORM`, `CURRENCY`: 문자열 (String)
   - `CREATEDAT`, `CHANGEDAT`: 날짜형 데이터로 사용되지만, 현재는 정수형으로 저장됨 (YYYYMMDD 형식)

3. 특이사항 및 주의점
   - `FAXNUMBER` 필드에 결측값이 많아 사용 시 주의 필요
   - `CREATEDAT`, `CHANGEDAT`는 정수 형태로 저장되어 있어 날짜 형식으로 변환 권장
   - `ADDRESSID`는 `Addresses.csv` 파일과의 조인을 통해 비즈니스 파트너의 주소 정보를 조회할 수 있음
   - `PARTNERROLE` 필드는 다른 파일과의 관계를 분석하는 데 유용할 수 있음

### `Employees.csv` 파일 분석

1. 파일 구조
   - 직원 관련 정보 포함
   - 주요 컬럼:
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

2. 데이터 유형
   - `EMPLOYEEID`, `ADDRESSID`: 정수형 (Integer)
   - `NAME_FIRST`, `NAME_MIDDLE`, `NAME_LAST`, `NAME_INITIALS`, `SEX`, `LANGUAGE`, `PHONENUMBER`, `EMAILADDRESS`, `LOGINNAME`: 문자열 (String)
   - `VALIDITY_STARTDATE`, `VALIDITY_ENDDATE`: 날짜형 데이터로 사용되지만, 현재는 정수형으로 저장됨 (YYYYMMDD 형식)

3. 특이사항 및 주의점
   - 일부 컬럼 (`Unnamed: 13`부터 `Unnamed: 18`)은 불필요하거나 비어있는 데이터로 보이며, 데이터 분석 시 제거가 필요함
   - `VALIDITY_STARTDATE`, `VALIDITY_ENDDATE`는 정수 형태로 저장되어 있어 날짜 형식으로 변환하는 것이 좋음
   - `ADDRESSID`는 `Addresses.csv` 파일과의 조인을 통해 직원의 주소 정보를 조회할 수 있음

### `ProductCategories.csv` 파일 분석

1. 파일 구조
   - 제품 카테고리 정보 포함
   - 주요 컬럼:
     - `PRODCATEGORYID`: 제품 카테고리를 식별하는 고유 ID
     - `CREATEDBY`: 레코드를 생성한 사용자 ID
     - `CREATEDAT`: 레코드 생성 날짜 (YYYYMMDD 형식)

2. 데이터 유형
   - `PRODCATEGORYID`: 문자열 (String)
   - `CREATEDBY`: 정수형 (Integer)
   - `CREATEDAT`: 날짜형 데이터로 사용되지만, 현재는 정수형으로 저장됨 (YYYYMMDD 형식)

3. 특이사항 및 주의점
   - `CREATEDAT`는 정수 형태로 저장되어 있어 날짜 형식으로 변환하는 것이 좋음
   - 이 파일은 제품 카테고리의 기본 정보를 제공하며, 추가적인 설명이나 텍스트 정보는 별도의 파일에서 찾을 수 있을 가능성이 있음

### `ProductCategoryText.csv` 파일 분석

1. 파일 구조
   - 제품 카테고리에 대한 텍스트 설명 정보 포함
   - 주요 컬럼:
     - `PRODCATEGORYID`: 제품 카테고리를 식별하는 고유 ID (예: `ProductCategories.csv`와 연결 가능)
     - `LANGUAGE`: 언어 코드 (예: EN)
     - `SHORT_DESCR`: 제품 카테고리의 짧은 설명
     - `MEDIUM_DESCR`: 제품 카테고리의 중간 길이 설명
     - `LONG_DESCR`: 제품 카테고리의 긴 설명

2. 데이터 유형
   - `PRODCATEGORYID`: 문자열 (String)
   - `LANGUAGE`: 문자열 (String)
   - `SHORT_DESCR`, `MEDIUM_DESCR`, `LONG_DESCR`: 문자열 (String)

3. 특이사항 및 주의점
   - `MEDIUM_DESCR`, `LONG_DESCR` 필드는 결측값이 많아 사용 시 주의가 필요함
   - `PRODCATEGORYID`는 `ProductCategories.csv` 파일과 연결하여 각 제품 카테고리에 대한 텍스트 설명을 조회할 수 있음
   - 제품 카테고리의 설명이 여러 언어로 제공될 수 있으므로, 언어 필드를 기준으로 필요한 텍스트를 선택하여 사용해야 함

### `Products.csv` 파일 분석

1. 파일 구조
   - 제품 관련 정보 포함
   - 주요 컬럼:
     - `PRODUCTID`: 제품을 식별하는 고유 ID
     - `TYPECODE`: 제품 유형 코드
     - `PRODCATEGORYID`: 제품 카테고리 ID (`ProductCategories.csv`와 연결 가능)
     - `CREATEDBY`: 레코드를 생성한 사용자 ID
     - `CREATEDAT`: 레코드 생성 날짜 (YYYYMMDD 형식)
     - `CHANGEDBY`: 마지막으로 변경한 사용자 ID
     - `CHANGEDAT`: 마지막으로 변경한 날짜 (YYYYMMDD 형식)
     - `SUPPLIER_PARTNERID`: 공급업체 파트너 ID (`BusinessPartners.csv`와 연결 가능)
     - `TAXTARIFFCODE`: 세금 코드
     - `QUANTITYUNIT`: 수량 단위 (예: EA)
     - `WEIGHTMEASURE`: 제품 무게
     - `WEIGHTUNIT`: 무게 단위 (예: KG)
     - `CURRENCY`: 가격 통화 (예: USD)
     - `PRICE`: 제품 가격
     - `WIDTH`, `DEPTH`, `HEIGHT`: 제품의 치수 (폭, 깊이, 높이)
     - `DIMENSIONUNIT`: 치수 단위
     - `PRODUCTPICURL`: 제품 이미지 URL

2. 데이터 유형
   - `PRODUCTID`, `TYPECODE`, `PRODCATEGORYID`, `QUANTITYUNIT`, `WEIGHTUNIT`, `CURRENCY`, `DIMENSIONUNIT`, `PRODUCTPICURL`: 문자열 (String)
   - `CREATEDBY`, `CREATEDAT`, `CHANGEDBY`, `CHANGEDAT`, `SUPPLIER_PARTNERID`, `TAXTARIFFCODE`: 정수형 (Integer)
   - `WEIGHTMEASURE`, `PRICE`, `WIDTH`, `DEPTH`, `HEIGHT`: 부동소수점형 (Float)

3. 특이사항 및 주의점
   - `CREATEDAT`, `CHANGEDAT` 필드는 정수 형태로 저장되어 있어 날짜 형식으로 변환하는 것이 좋음
   - `PRODUCTPICURL` 등 일부 필드는 결측값이 많을 수 있음
   - `PRODCATEGORYID`와 `SUPPLIER_PARTNERID` 필드는 각각 `ProductCategories.csv`와 `BusinessPartners.csv` 파일과의 조인을 통해 제품의 카테고리와 공급업체 정보를 조회할 수 있음
   - 제품의 치수와 이미지 URL 정보가 결측값일 수 있으므로, 데이터 분석 시 이러한 필드의 유효성에 주의 필요

### `ProductTexts.csv` 파일 분석

1. 파일 구조
   - 제품에 대한 텍스트 설명 정보 포함
   - 주요 컬럼:
     - `PRODUCTID`: 제품을 식별하는 고유 ID (`Products.csv`와 연결 가능)
     - `LANGUAGE`: 언어 코드 (예: EN)
     - `SHORT_DESCR`: 제품의 짧은 설명
     - `MEDIUM_DESCR`: 제품의 중간 길이 설명
     - `LONG_DESCR`: 제품의 긴 설명

2. 데이터 유형
   - `PRODUCTID`: 문자열 (String)
   - `LANGUAGE`: 문자열 (String)
   - `SHORT_DESCR`, `MEDIUM_DESCR`, `LONG_DESCR`: 문자열 (String)

3. 특이사항 및 주의점
   - `MEDIUM_DESCR`, `LONG_DESCR` 필드는 결측값이 많아 사용 시 주의가 필요함
   - `PRODUCTID`는 `Products.csv` 파일과 연결하여 각 제품에 대한 텍스트 설명을 조회할 수 있음
   - 제품 설명이 여러 언어로 제공될 수 있으므로, 필요한 언어로 텍스트를 선택하여 사용해야 함

### `SalesOrderItems.csv` 파일 분석

1. 파일 구조
   - 판매 주문 항목 정보 포함
   - 주요 컬럼:
     - `SALESORDERID`: 판매 주문을 식별하는 고유 ID (`SalesOrders.csv`와 연결 가능)
     - `SALESORDERITEM`: 판매 주문 내 항목 번호
     - `PRODUCTID`: 제품을 식별하는 고유 ID (`Products.csv`와 연결 가능)
     - `NOTEID`: 추가 노트 ID (현재 데이터에서 사용되지 않음)
     - `CURRENCY`: 통화 코드 (예: USD)
     - `GROSSAMOUNT`: 총 금액
     - `NETAMOUNT`: 순 금액
     - `TAXAMOUNT`: 세금 금액
     - `ITEMATPSTATUS`: 항목 상태 코드
     - `OPITEMPOS`: 운영 항목 위치 (현재 데이터에서 사용되지 않음)
     - `QUANTITY`: 주문된 제품 수량
     - `QUANTITYUNIT`: 수량 단위 (예: EA)
     - `DELIVERYDATE`: 배송 날짜 (YYYYMMDD 형식)

2. 데이터 유형
   - `SALESORDERID`, `SALESORDERITEM`, `PRODUCTID`, `NOTEID`, `ITEMATPSTATUS`, `QUANTITYUNIT`: 문자열 (String)
   - `CURRENCY`: 문자열 (String)
   - `GROSSAMOUNT`, `NETAMOUNT`, `TAXAMOUNT`: 부동소수점형 (Float)으로 변환이 필요할 수 있음
   - `QUANTITY`: 정수형 (Integer)
   - `DELIVERYDATE`: 정수형 (Integer)으로 저장된 날짜 (YYYYMMDD 형식)

3. 특이사항 및 주의점
   - `DELIVERYDATE`는 정수 형태로 저장되어 있어 날짜 형식으로 변환하는 것이 좋음
   - `PRODUCTID`는 `Products.csv` 파일과의 조인을 통해 제품에 대한 추가 정보를 조회할 수 있음
   - `SALESORDERID`는 `SalesOrders.csv` 파일과 연결하여 주문 정보를 분석할 수 있음
   - 일부 컬럼 (`NOTEID`, `OPITEMPOS`)은 현재 데이터에서 사용되지 않거나, 결측값으로 처리될 수 있음

### `SalesOrders.csv` 파일 분석

1. 파일 구조
   - 판매 주문 정보 포함
   - 주요 컬럼:
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

2. 데이터 유형
   - `SALESORDERID`, `NOTEID`, `PARTNERID`, `SALESORG`, `LIFECYCLESTATUS`, `BILLINGSTATUS`, `DELIVERYSTATUS`: 문자열 (String)
   - `CREATEDBY`, `CREATEDAT`, `CHANGEDBY`, `CHANGEDAT`, `FISCVARIANT`, `FISCALYEARPERIOD`: 정수형 (Integer)
   - `GROSSAMOUNT`, `NETAMOUNT`, `TAXAMOUNT`: 부동소수점형 (Float)으로 변환이 필요할 수 있음
   - `CURRENCY`: 문자열 (String)

3. 특이사항 및 주의점
   - `CREATEDAT`, `CHANGEDAT` 필드는 정수 형태로 저장되어 있어 날짜 형식으로 변환하는 것이 좋음
   - `PARTNERID`는 `BusinessPartners.csv` 파일과 연결하여 주문을 생성한 비즈니스 파트너 정보를 조회할 수 있음
   - `SALESORDERID`는 `SalesOrderItems.csv` 파일과의 조인을 통해 주문에 포함된 항목 정보를 분석할 수 있음
   - 회계 정보 (`FISCVARIANT`, `FISCALYEARPERIOD`)와 상태 정보 (`LIFECYCLESTATUS`, `BILLINGSTATUS`, `DELIVERYSTATUS`)를 통해 주문의 재무 상태와 진행 상황을 추적 가능

### 데이터 간의 관계 추정

각 파일의 주요 컬럼을 기준으로 파일 간의 관계 추정

1. `Addresses.csv`
   - `ADDRESSID`: `BusinessPartners.csv`, `Employees.csv`와의 관계에서 사용되는 키.
     - 연결 관계:
       - `BusinessPartners.csv`의 `ADDRESSID`
       - `Employees.csv`의 `ADDRESSID`

2. `BusinessPartners.csv`
   - `PARTNERID`: 비즈니스 파트너를 식별하는 고유 ID로, `SalesOrders.csv`와 관계를 형성.
   - `ADDRESSID`: `Addresses.csv`의 `ADDRESSID`와 연결하여 비즈니스 파트너의 주소 정보 조회 가능.
     - 연결 관계:
       - `SalesOrders.csv`의 `PARTNERID`
       - `Addresses.csv`의 `ADDRESSID`

3. `Employees.csv`
   - `EMPLOYEEID`: 각 직원을 식별하는 고유 ID로, 현재 업로드된 다른 파일과 직접적인 연결은 없음.
   - `ADDRESSID`: `Addresses.csv`의 `ADDRESSID`와 연결하여 직원의 주소 정보 조회 가능.
     - 연결 관계:
       - `Addresses.csv`의 `ADDRESSID`

4. `ProductCategories.csv`
   - `PRODCATEGORYID`: 제품 카테고리를 식별하는 ID로, `Products.csv`와 `ProductCategoryText.csv`와의 관계에서 사용.
     - 연결 관계:
       - `Products.csv`의 `PRODCATEGORYID`
       - `ProductCategoryText.csv`의 `PRODCATEGORYID`

5. `ProductCategoryText.csv`
   - `PRODCATEGORYID`: `ProductCategories.csv`의 `PRODCATEGORYID`와 연결하여 각 카테고리의 텍스트 설명 조회 가능.
     - 연결 관계:
       - `ProductCategories.csv`의 `PRODCATEGORYID`

6. `Products.csv`
   - `PRODUCTID`: 제품을 식별하는 고유 ID로, `SalesOrderItems.csv`와 관계를 형성.
   - `PRODCATEGORYID`: `ProductCategories.csv`의 `PRODCATEGORYID`와 연결하여 제품의 카테고리 정보 조회 가능.
   - `SUPPLIER_PARTNERID`: `BusinessPartners.csv`의 `PARTNERID`와 연결하여 공급업체 정보 조회 가능.
     - 연결 관계:
       - `SalesOrderItems.csv`의 `PRODUCTID`
       - `ProductCategories.csv`의 `PRODCATEGORYID`
       - `BusinessPartners.csv`의 `PARTNERID`

7. `ProductTexts.csv`
   - `PRODUCTID`: `Products.csv`의 `PRODUCTID`와 연결하여 각 제품의 텍스트 설명 조회 가능.
     - 연결 관계:
       - `Products.csv`의 `PRODUCTID`

8. `SalesOrderItems.csv`
   - `SALESORDERID`: `SalesOrders.csv`의 `SALESORDERID`와 연결하여 주문 정보 조회 가능.
   - `PRODUCTID`: `Products.csv`의 `PRODUCTID`와 연결하여 주문 항목의 제품 정보 조회 가능.
     - 연결 관계:
       - `SalesOrders.csv`의 `SALESORDERID`
       - `Products.csv`의 `PRODUCTID`

9. `SalesOrders.csv`
   - `SALESORDERID`: 판매 주문을 식별하는 고유 ID로, `SalesOrderItems.csv`와 관계를 형성.
   - `PARTNERID`: `BusinessPartners.csv`의 `PARTNERID`와 연결하여 주문을 생성한 비즈니스 파트너 정보 조회 가능.
     - 연결 관계:
       - `SalesOrderItems.csv`의 `SALESORDERID`
       - `BusinessPartners.csv`의 `PARTNERID`

#### 주요 관계 요약

- 고객 및 공급업체 정보: `BusinessPartners.csv`와 `Addresses.csv`를 통해 고객 및 공급업체의 상세 주소 정보를 조회 가능.
- 직원 정보: `Employees.csv`와 `Addresses.csv`의 `ADDRESSID`를 사용하여 직원의 주소 정보를 조회 가능.
- 제품 정보: `Products.csv`, `ProductCategories.csv`, `ProductCategoryText.csv`, `ProductTexts.csv`는 제품과 제품 카테고리, 그리고 제품의 텍스트 설명을 제공하며 서로 연결.
- 주문 및 판매 데이터: `SalesOrders.csv`와 `SalesOrderItems.csv`는 판매 주문과 각 주문 항목에 대한 정보를 제공하며, `Products.csv` 및 `BusinessPartners.csv`와의 연결을 통해 제품과 고객 정보를 연계 가능.
