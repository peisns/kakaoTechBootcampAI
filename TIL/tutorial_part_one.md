[🏠 처음으로](/README.md)

# TIL (Today I Learned)

- 2024-07-03 ~ 2024-07-04
- 변수, 자료형, 연산자, 조건문, 반복문, 함수, 리스트 등
- [파이썬 기초 문법](#파이썬-기초-문법)
  * [변수](#변수)
  * [자료형](#자료형)
  * [서식 문자열](#서식-문자열)
  * [연산자](#연산자)
  * [문자열 슬라이싱](#문자열-슬라이싱)
  * [조건문](#조건문)
    + [시퀀스](#시퀀스)
    + [반복문 while](#반복문-while)
    + [반복문 continue / break](#반복문-continue--break)
  * [함수](#함수)
    + [람다(lambda) 함수](#람다lambda-함수)
    + [함수형 프로그래밍](#함수형-프로그래밍)
- [참고](#참고)

# 파이썬 기초 문법

## 변수

- 어떤 값을 저장하거나 변경할 수 있는 `메모리 공간`
- 변수 선언과 할당
    - 변수이름 = 값
    - ex) name = "model"
    - ex) age = 10
    - name과 age는 "변수 이름" 또는 "식별자"
    - "model", 10은 변수 값
    - "="은 할당 연산자
- 네이밍 규칙
    - 숫자로 시작하지 않기
    - 공백이나 특수문자를 사용하지 않기
        - underscore("_") 는 사용가능

## 자료형

- 변수가 갖는 데이터의 종류
- 숫자형: 정수(int), 실수(float)
- 문자형: 문자(str)
- 불리언형: bool(True, False)
- 변환: int(), float(), str() 등

## 서식 문자열

- [공식 문서 링크로 대체함](https://docs.python.org/ko/3.10/reference/lexical_analysis.html#formatted-string-literals)

## 연산자

- 산술 연산자: +, -, *, /, //, %
- 비교 연산자: ==, !=, >, <, >=, <=
- 논리 연산자: and, or, not
- 내용 생략

## 문자열 슬라이싱

- 문자열 변수 이름[start : stop : step]
- start를 생략하면 문자열의 처음부터,
- stop을 생략하면 문자열의 끝까지,
- step을 생략하면 1만큼씩 증가


## 조건문

- 사용형식

        if 조건식1:
            실행문1
        elif 조건식2:
            실행문2
        elif 조건식3:
            실행문3
        else:
            실행문n

- 중첩 조건문

        a = 10
        b = 5
        
        if a > 5:
            if b < 10:
                print("a는 5보다 크고 b는 10보다 작다.")

- 반복문 for

        for 변수 in 시퀀스:
            # 시퀀스의 각 요소에 대해 실행할 코드
        
        a = [1, 2, 3, 4, 5]

        for i in a:
            print(i)

        # 1
        # 2 
        # 3
        # 4
        # 5

    - range() 함수 사용

            for i in range(start, stop, step):
                # 실행코드

            for i in range(1, 10, 2):
                print(i)

    - 반복 범위가 문자인 경우

            for char in "가나다"
                print(char)
            
            # 가
            # 나
            # 다

### 시퀀스

- 나열된 데이터, 연속된 데이터
- 리스트, 문자열, 튜플 등 순서가 있는 자료형

### 반복문 while

    while 조건식:
        # 조건식이 참일 때 실행할 코드

    i = 1
    while i <= 10:
        print(i)
        i += 1

    # 1
    # 2
    # ...
    # 10

### 반복문 continue / break

- continue 키워드를 만나면 코드 실행을 멈추고 처음부터 다시 반복
- break 키워들 만나면 코드 실행을 멈추고 반복문 실행도 멈춘다
- Swift와 같음

## 함수

- 정의, 실행

        def 함수명([매개변수1, 매개변수2, ... ]):
            # 실행할 코드
            [return 반환값1, 반환값2, ...]

        def add(x, y):
            return x + y
        
        print(add(2, 4))
        # 6

- 함수 호출
    - 함수 이름과 괄호를 사용해서 호출

            result = say("hello")

- 함수의 종류
    - 내장 함수
        - 파이썬에서 제공하는 기본 함수
        - print(), len() 등
    - 사용자 정의 함수
        - 프로그래머가 직접 정의하는 함수
- 함수의 주요 기능
    - 코드의 재사용성 향상
    - 코드의 가독성 향상
    - 코드의 유지보수성 향상
- 함수를 사용할 때 고려해야할 사항
    - 함수의 이름을 명확하고 의미 있게 지정해야 함
    - 함수의 매개변수는 최소한의 개수로 지정
    - 함수의 코드는 간결하고 이해하기 쉽도록 작성
    - 함수의 반환값은 명확하게 지정
- 함수의 인자 
    - *args
        - 가변인자
        - n개의 인자를 함수에 전달할 때 사용
        - 튜플 형태로 전달

                def 함수이름(*args):
                    # 코드 실행
    
    - **kwargs
        - 키워드 가변인자
        - 키워드 인자를 함수에 전달할 때 사용
        - 딕셔너리 형태로 전달

                def 함수이름(**kwargs):
                    # 코드 실행
    
    - 가변인자를 사용하는 상황?
        - 유연하게 함수를 설계할 수 있음
        - 다양한 함수 호출 패턴을 지원함

### 람다(lambda) 함수

- 익명 함수
- 한줄로 작성 가능
- `lambda` 키워드를 사용해서 정의
- 간단한 연산이나, 데이터 변환에 유요함
- 일회성으로 사용 + 코드의 간결화를 위해 사용

        lambda 매개변수: 반환값
        result = lambda x: x ** 2

### 함수형 프로그래밍

- 함수를 일급 객체로 사용하여 코드를 구성
- 대규모 데이터 처리에 유용함
- 데이터 파이프라인 구축 시 사용함
- map, filter, reduce와 같은 고차함수 사용
- 단, list를 반환하는 것은 아니고 이터레이터를 반환함
- 다른 부분은 Swift와 같음



<!-- > TODO: 리스트 -->

--- 

### 참고

- 이지형(Jhin). _생성형 인공지능(AI) 과정_, kakao tech bootcamp, 2024.
- 성창규. "파이썬 기초 문법(Ⅰ)." _AI 이해를 위한 파이썬 기초_, 부산대학교 소프트웨어융합교육원, [www.inflearn.com/course/ai-이해-파이썬기초](https://www.inflearn.com/course/ai-%EC%9D%B4%ED%95%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B8%B0%EC%B4%88). Accessed 7 7 2024.
- 성창규. "파이썬 기초 문법(Ⅱ)." _AI 이해를 위한 파이썬 기초_, 부산대학교 소프트웨어융합교육원, [www.inflearn.com/course/ai-이해-파이썬기초](https://www.inflearn.com/course/ai-%EC%9D%B4%ED%95%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B8%B0%EC%B4%88). Accessed 7 7 2024.
- “Python 3.10.13 문서.” _3.10.13 Documentation_, [docs.python.org/ko/3.10/index.html](). Accessed 8 July 2024. 