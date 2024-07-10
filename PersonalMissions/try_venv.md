[🏠 처음으로](/README.md)

# Knowledge Repository

- write: 2024-07-09
- study period: 2024-07-09
- update: 2024-07-10
- `venv` → python 가상환경 설정(macOS, zsh, terminal 사용)
- TOC
    - [venv](#venv)
        - [설치하기](#설치하기)
        - [가상환경 설정](#가상환경-설정)
        - [가상환경 activate](#가상환경-activate)
        - [가상환경 비활성화](#가상환경-비활성화)
        - [패키지 설치](#패키지-설치)
    - [참고](#참고)


# venv

- 패키지 의존성 문제를 예방하고자 venv를 사용해보자
- `venv`는 `conda`나 `virtualenv`과 다르게 python의 표준 라이브러리에 포함되어 있어서 별도의 설치가 필요하지 않다
- 가상환경을 통해서 프로젝트마다 독립적인 버전 관리가 가능하게 된다
- 장점
    - 의존성 관리: 프로젝트마다 독립적인 패키지 설치 환경을 제공해서, 패키지 버전 충돌을 방지할 수 있다.
    - 재현성: 특정 프로젝트의 환경을 그대로 재현할 수 있기 때문에 협업 시 환경을 통제할 수 있다.
        - `requirements.txt` 으로 손쉽게 환경을 내보내고 설치할 수 있다


## 설치하기

- 위에서 언급한 것처럼, python 3.3 버전 이후로는 표준 라이브러리에 포함되어 있기 때문에, 별도의 설치가 필요없다.
- 단, 그래서 python이 미리 설치되어 있어야 한다
    - python 설치 여부는 `python --version` 이나 `python3 --version` 으로 확인


## 가상환경 설정

    python3 -m venv 폴더이름

- 현재 디렉토리에 myenv라는 이름의 디렉토리를 생성하고 가상환경을 설정함


## 가상환경 activate

    source 폴더이름/bin/activate

- 폴더를 만들었을 때, 폴더 내의 bin폴더, bin폴더 내의 activate를 경로로 실행


## 가상환경 비활성화

    deactivate

- 가상환경 활성화 되어있다면 현재 위치(경로)에 상관 없이 비활성화가 가능하다
- source 커맨드는 파일을 읽고 현재 셀에서 그 안의 명령을 실행하게 하는 것


## 패키지 설치

4.4. 가상환경 내에서 패키지 설치
가상환경이 활성화된 상태에서 pip 명령어를 사용하여 패키지를 설치할 수 있습니다. 예를 들어, requests 패키지를 설치하려면 다음과 같이 합니다.

<!-- pip install requests -->
<!-- 1.requirements.txt 파일 사용 -->
<!-- 2.pip freeze > requirements.txt # 다르 환경에서 동일한 패키지 의존성 설치-->
<!-- 3. pip install -r requirements.txt -->


--- 

### 참고

- “venv — Creation of virtual environments.” _3.12.4 Documentation_, Python Software Foundation, 7 7 2024, 00:57 UTC, [docs.python.org/ko/3/library/venv.html#module-venv](https://docs.python.org/ko/3/library/venv.html#module-venv). Accessed 9 7 2024. 
- Park, Tony. _[Python] 가상환경 생성, 활성화, 비활성화, 삭제 방법(Venv 활용)_. Hey Tech, 22 Feb. 2022, [heytech.tistory.com/295](https://heytech.tistory.com/295). Accessed 9 7 2024.