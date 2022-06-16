# drf_class

drf 특강 1일차 과제
## 1. args, kwargs를 사용하는 예제 코드 짜보기
'''
 def myFun(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(f"key = {key}, value = {value}")

myFun('This', 'is', 'an example', arg1 ='Hello', arg2 ='World', arg3='Python')
'''

## 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기

: mutable은 값이 변한다는 뜻이고, immutable은 값이 변하지 않는다는 의미이다.

- mutable: 리스트(List), 딕셔너리(Dictionary)
- immutable: 숫자형(Number), 문자열(String), 튜플(Tuple)
 

## 3. DB Field에서 사용되는 Key 종류와 특징 서술하기

- Unique Key: 테이블 내 항상 유일해야하는 값. 여러개여도 되고, null값도 입력가능. Unique key에 Primary key도 포함될 수 있음
- Primary Key: 기본키. data table에 있는 유일하게 구분되는 key. 유일하기 때문에 중복된 값을 가질 수 없고, 공백(null)도 불가
- Foreign Key: 외래키. 한 table과 참조되는 다른 table 간 연결되는 Primary key column. 다른 Primary key를 참조하는 속성 또는 속성들의 집합을 말한다 (참조관계의 기본키와 같은 속성을 가짐)
 

## 4. django에서 queryset과 object는 어떻게 다른지 서술하기

- queryset: Database에서 전달받은 객체들의 모음(list)
- object: 어떠한 속성값과 행동을 가지고 있는 데이터. 여기서는 db에 들어있는 데이터를 가리키는데 dictionary로 출력된다.
