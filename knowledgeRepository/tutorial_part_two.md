[🏠 처음으로](/README.md)

# Knowledge Repository

- write: 2024-07-04
- study period: 2024-07-03 ~ 2024-07-04
- update: 2024-07-10
- 파이썬 기초 문법
- 클래스, OOP, 이터레이터, 제너레이터


### Table Of Contents

- [파이썬 기초 문법](#파이썬-기초-문법)
  - [클래스와 객체지향 프로그래밍](#클래스와-객체지향-프로그래밍)
    - [객체 지향 프로그래밍(Object-Oriented Programming)](#객체-지향-프로그래밍object-oriented-programming)
    - [OOP의 특징](#oop의-특징)
    - [클래스](#클래스)
    - [매직 메서드(Magic Methods)](#매직-메서드magic-methods)
  - [이터레이터와 제너레이터](#이터레이터와-제너레이터)
    - [이터레이터(Iterator)](#이터레이터iterator)
    - [제너레이터(generator)](#제너레이터generator)
    - [제너레이터 표현식](#제너레이터-표현식)
  - [이터레이터와 제너레이터의 비교](#이터레이터와-제너레이터의-비교)
    - [구현 방식](#구현-방식)
    - [사용 용이성](#사용-용이성)
    - [메모리 효율성](#메모리-효율성)

# 파이썬 기초 문법

## 클래스와 객체지향 프로그래밍

### 객체 지향 프로그래밍(Object-Oriented Programming)

- 객체의 관점에서 프로그래밍 한다는 것
- 객체를 기준으로 코드를 나누어 구현

### OOP의 특징

- 캡슐화
    - 데이터와 메서드를 하나의 단위로 묶고 외부로부터 숨기는 것
    - 클래스의 생성 목적을 잘 수행할 수 있도록 관련 모듈을 잘 묶고 구성해야함
    - 정보은닉
        - 캡슐화의 중요한 목적 중 하나
        - 외부에서 클래스의 필요한 정보만 접근 가능하게 하고, 필요하지 않은 부분은 접근할 수 없도록 캡슐화를 통해 정보를 은닉할 수 있다
        - `protexted` 변수
            - 변수 앞에 `_`를 붙여 protected 변수로 명명
            - 강제성이 없는 약속의 의미
            - 접근가능함
            - 자기 클래스 내부 혹은 상속받은 자식 클래스의 접근 허용
        - `private` 변수
            - 변수 앞에 `__`(underscore * 2)를 붙여 private 변수 선언
            - `private` 변수에 접근하려고 하면 에러 발생
            - `_클래스이름__`변수이름 으로 접근은 가능하나...
            - 자기 클래스 내부의 메서드에서만 접근 허용
- 추상화
    - 중요한 정보만을 표현하고, 불필요한 세부 사항을 숨기는 것
    - 중요한 정보는 무엇이고 불필요한 세부 사항은 무엇일까?
        - 필수, 공통적인 요소를 추출하는 과정이 추상화
        - 자동차라면 엔진, 바퀴, 핸들 등 필수적인 부분
- 상속
    - 부모 클래스를 기반으로 새로운 자식 클래스를 정의
    - 코드의 재사용성 증가
    - 계층적 관계를 명확히 함

            class 부모클래스:
                # 속성과 메서드
            
            class 자식클래스(부모클래스):
                # 속성과 메서드 정의

- 다형성
    - 동일한 인터페이스를 사용하여 서로 다른 데이터 타입의 객체를 다루는 것
    - 코드의 유연성과 확장성을 높임
- OOP의 장점
    - 코드 재사용성: 기존 코드를 재사용하여 효율성 증가
    - 코드 유지보수성: 모듈화된 코드 구조를 통해 유지보수를 쉽게 할 수 있음
    - 확장성: 새로운 기능 추가 시 기존 코드를 수정하지 않고 확장할 수 있음

<!-- > TODO: OOP 좀 더 자세하게 공부하기
https://velog.io/@hkoo9329/OOPObject-Oriented-Programming-%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%9D%B4%EB%9E%80 -->

### 클래스

- 인스턴스를 정의하는데 사용되는 틀
- 속성(attributes)과 메서드로 구성
- OOP의 기본 단위

### 매직 메서드(Magic Methods)

- 특별한 이름을 가진 메서드, python built-in method
- 객체의 특정 동작을 사용자 정의할 수 있음
- 예
    - `__init__`: 인스턴스 이니셜라이저
    - `__str__`: 인스턴스의 문자열 표현을 반환
    - `__repr__`: 인스턴스의 공식 문자열 표현을 반환
- 연산자 오버로딩(Operator Overloading)
    - 파이썬의 기본 연산자를 `override` 해서 사용할 수 있도록 정의
    - 객체간 연산을 가능하게 함
- 예
    - `__add__`, `__sub__`, `__mul__`, `__truediv__`

## 이터레이터와 제너레이터

### 이터레이터(Iterator)

- `__iter__()`와 `__next__()` 메서드를 구현한 객체
- 반복자: 반복 가능한 객체에서 값을 순차적으로 꺼내는 역할
- 상태 유지: 현재 위치를 기억하여 `next()` 호출 시 다음 값을 반환

        for element in [1, 2, 3]:
            print(element)
        for element in (1, 2, 3):
            print(element)
        for key in {'one':1, 'two':2}:
            print(key)
        for char in "123":
            print(char)
        for line in open("myfile.txt"):
            print(line, end='')

        # 위 코드를 이터레이터를 사용하여 통합시킬 수 있음
        # Swift의 Reactive Programming에서 자주 사용하는 내용

        s = 'abc'
        it = iter(s)
        it
        # <str_iterator object at 0x10c90e650>
        next(it)
        # 'a'
        next(it)
        # 'b'
        next(it)
        # 'c'
        next(it)
        # Traceback (most recent call last):
        # File "<stdin>", line 1, in <module>
        #     next(it)
        # StopIteration

- 클래스에 이터레이터 동작 추가하기
    1. 클래스에 `__next__()`메서드 정의하기
    2. `__next__()`메서드를 가지고 있는 객체를 반환하는 `__iter__()`메서드를 정의하기
    3. 클래스에서 `__next__()`메서드를 정의하면 `__iter__()`는 그냥 자기자신(self)을 반환할 수 있다

            # 시퀀스를 거꾸로 반복하는 이터레이터
            class Reverse:
                def __init__(self, data):
                    self.data = data
                    self.index = len(data)

                # self를 반환하는 __iter__() 메서드 정의
                def __iter__(self):
                    return self

                # __next__() 메서드 정의
                def __next__(self):
                    if self.index == 0:
                        raise StopIteration
                    self.index = self.index - 1
                    return self.data[self.index]

            rev = Reverse('spam')
            iter(rev)
            # <__main__.Reverse object at 0x00A1DB50>
            for char in rev:
                print(char)
            # m
            # a
            # p
            # s


### 제너레이터(generator)

- 이터레이터를 만드는 간단하고 강력한 도구
- 제너레이터도 이터레이터이므로 `__iter__()`와 `__next__()` 자동 구현
- 제너레이터로 할 수 있는 모든 작업은 이터레이터로 수행할 수 있음
- 일반적인 함수처럼 정의
- 값을 반환할 때, `return`이 아닌 `yield` 키워드를 사용
- 제너레이터의 next()가 호출될 때마다, 멈춘 곳에서 실행을 재개함
    - 모든 데이터 값들과 어떤 문장이 마지막으로 실행되었는지 기억함
- 메모리 효율성: 한 번에 하나의 값만 생성하므로 메모리 사용을 최소화 할 수 있음
- 코드 간결화: 복잡한 이터레이터 코드를 간단하게 작성 
- 제너레이터가 종료될 때 `StopIteration`을 일으킴
- `yield` 키워드
    - 제너레이터에서 값을 반환하고 **함수의 실행 상태를 일시 중지**
    - 지연 평가 Lazy Evaluation
        - 값, 데이터를 한번에 다 출력하는 것이 아니라 필요한 시점에 값을 생성함  
        ➞ 메모리 절약: 한 번에 하나의 값만 생성함으로 메모리 사용을 최소화 할 수 있다
        - `yield` 키워드를 만나면 값을 반환하고 함수의 실행 상태를 저장
    - 상태 유지
        - 마지막 실행 시점에서 멈추고 상태를 기억
        - 다음 호출 시 저장된 상태에서, 그 지점부터 다시 시작
- 활용
    - 대량 데이터 처리: 대규모 파일 읽기, 대규모 데이터베이스 쿼리 결과 처리 등
    - 스트리밍 데이터 처리: 실시간 데이터 스트리밍에 유용
- 예시

        def reverse(data):
            for index in range(len(data)-1, -1, -1):
                yield data[index]

        for char in reverse('golf'):
            print(char)
        
        # f
        # l
        # o
        # g


### 제너레이터 표현식

- List Comprehension과 비슷하게 사용할 수 있음
- 대괄호 대신 괄호를 사용하는 것이 List Comprehension과 차이
- 제너레이터 표현식은 함수가 제너레이터를 즉시 사용하는 상황을 위해서 설계되었음
- 일반 제너레이터보다 간결하지만 융통성이 떨어짐
- List Comprehension보다 메모리를 덜 사용하는 경향이 있음

        # 리스트 컴프리헨션  
        squares = [x**2 for x in range(10)]
        print(squares)
        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

        # 제너레이터 표현식
        squares = (x**2 for x in range(10))
        print(squares)
        # <generator object <genexpr> at 0x1...>

        # 제너레이터 객체를 반복하여 값을 출력
        for value in squares:
            print(value)
        # 0
        # 1
        # ...
        # 81


## 이터레이터와 제너레이터의 비교

### 구현 방식

- 이터레이터: 클래스 형태, `__iter__()`와 `__next__()` 메서드 구현
- 제너레이터: 함수 형태, `yield` 키워드 사용


### 사용 용이성

- 이터레이터: 상대적으로 복잡한 구조
- 제너레이터: 간단한 코드 구현


### 메모리 효율성

- 이터레이터: 모든 값을 메모리에 저장
- 제너레이터: 값을 필요할 때마다 생성

---

### 참고

- 이지형(Jhin). "파이썬 프로그래밍I(240704)." _생성형 인공지능(AI) 과정_, kakao tech bootcamp, 2024.
- “9.클래스.” _3.12.4 Documentation_, [docs.python.org/ko/3/tutorial/classes.html](https://docs.python.org/ko/3/tutorial/classes.html). Accessed 10 July 2024. 