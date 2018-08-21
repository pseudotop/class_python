# cr_zdnet.py 기술 명세
# 목록
  - [개요](#개요)
    - [도입 배경](#도입-배경)
    - [기술 개요](#기술-개요)
  - [사용법](#사용법)
  - [결과값](#결과값)
  - [개선 사항](#개선-사항)
## 개요
### 도입 배경
* IT 기술이 나날이 빠르게 발전하고 있다. 신기술이 도입된 사업분야에 대한 빠른 이해와 대처를 하기 위해 본 서비스를 도입하였다  
### 기술 개요
* IT 전문 온라인 출판사(zdnet)에 있는 다수의 기사에서 자주 언급되는 단어를 출력 및 내림차순 정렬
-----------------
## 사용법
```
$ python cr_zdnet.py

DFS depth: 
```
여기서, 콘솔창에 표현된 `DFS depth` 는 **DFS(depth-first search)** 방식의 _depth_ 와 일치하며 탐색 깊이를 나타낸다. 
예를 들어, `DFS depth` 에 **1** 로 타이핑하면 아래와 같은 결과값을 출력한다
### 결과값
```
DFS depth: 1
<url> depth: 0
<url-suburl> depth: 1
...
```
실행 후 `cr_result.txt` 생성 
```

 ==================================================
 Depth:1
 Count_Searching_Page:54
 Total_Words:5031
 ==================================================
 있 : 90
 등 : 52
  : 46
 많 : 45
 것 : 44
 같 : 39
 삼성전자 : 32
 ...
```
-----------------
* `Depth` - depth 단계
* `Count_Searching_Page` - 서칭 페이지 수
* `Total_Words` - `split()`이후 전체 단어 수
## 개선 사항
> 이 버전은 `프로토타입` 버전입니다
* To do list
  1. `split()`이후에 쪼갠 단어들의 조사('은','는','이','가' 등) 및 괄호 등을 다시 정제
     - 올바른 **텍스트 마이닝**을 위해서 **딥러닝**을 사용 필수
     - [KoNLPy: 파이썬 한국어 NLP](http://konlpy.org/ko/latest/)
  2. 특정 사이트(zdnet)뿐만 아니라 다양한 사이트에서 마이닝할 수 있도록 **리스트업**
  3. 사용자 편의를 위해 **GUI** 환경에서 지원