import pandas as pd
import re

pd.set_option('display.max_columns', None)

df = pd.read_csv('raw_data.txt', delimiter='|')

# print(df)
print(df.head())

allowed_special_chars = "\"',:"


# 필터링 함수 정의
def filter_special_chars(text, allowed_chars):
    
    # 정규 표현식 패턴 생성 (허용된 특수문자를 제외한 모든 특수문자를 찾는 패턴)
    
    pattern = f"[^\w\s{re.escape(allowed_chars)}]"
    # 정규 표현식을 사용하여 허용되지 않은 특수문자 제거
    return re.sub(pattern, '', text)


# 데이터프레임의 모든 문자열 셀에 대해 필터링 적용
data_deleted_special_character = df.applymap(lambda x: filter_special_chars(x, allowed_special_chars) if isinstance(x, str) else x)

# 필터링된 데이터프레임 출력
print("After Delete")
print(data_deleted_special_character)




"""
import pandas as pd
import re

# 파일 경로 지정
file_path = "customer_purchase_data.txt"

# |로 구분된 텍스트 파일을 데이터프레임으로 읽기
data = pd.read_csv(file_path, delimiter='|')

# 허용할 특수문자 지정 (예: !, ?, ., ,)
allowed_special_chars = "!?.," 

# 필터링 함수 정의
def filter_special_chars(text, allowed_chars):
    # 정규 표현식 패턴 생성 (허용된 특수문자를 제외한 모든 특수문자를 찾는 패턴)
    pattern = f"[^\w\s{re.escape(allowed_chars)}]"
    # 정규 표현식을 사용하여 허용되지 않은 특수문자 제거
    return re.sub(pattern, '', text)

# 데이터프레임의 모든 문자열 셀에 대해 필터링 적용
data = data.applymap(lambda x: filter_special_chars(x, allowed_special_chars) if isinstance(x, str) else x)

# 필터링된 데이터프레임 출력
print(data)
"""
