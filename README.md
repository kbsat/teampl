# teampl
팀프로젝트 매칭 플랫폼 ( with Django )
2020. 11. 1 ~ 2020. 12.11

## 목적 및 필요성

### 프로젝트 목적
- 팀 프로젝트를 하기 원하는 개발자, 디자이너들에게 팀 프로젝트의 기회를 제공하고 협업 능력, 개발 능력을 성장할 수 있는 기회를 제공한다.
- 자신이 기획한 아이디어를 실제로 구현하고 싶은 기획자에게 자신의 아이디어를 게시하고 프로젝트를 함께 진행할 팀원을 모집할 수 있게 돕는다.

### 프로젝트 필요성
- 아이디어는 기획했지만 개발자나 디자이너 등의 팀원들이 부족해 프로젝트를 진행하기 어려운 기획자들에게 자신의 아이디어를 공개하고 함께 프로젝트를 진행할 팀원들을 모집하는 것을 도울 수 있다.
- 팀 프로젝트의 중요성을 알고있고 이에 참여하고 싶지만 다른 팀원들을 찾기 어려운 상황에 놓인 개발자, 디자이너들에게 기획자가 내놓은 아이디어를 제공해주고 관심있는 프로젝트에 참여할 수 있도록 한다.
- 학교나 독학으로는 제공받기 어려운 프로젝트의 기회를 제공함으로써 함께 작업할 사람을 주변에서 찾기 어려운 이들에게 협업의 기회를 늘리고 배움과 소통의 장이 되도록 함으로써 참여자들의 개발 역량 및 커뮤니케이션 능력을 성장시킬 수 있다.

## 계획
### 사용할 기술 스택
- 웹 기반의 프로젝트이기 때문에 HTML, CSS, Javascript를 활용할 예정
- 서버 프로그래밍은 Python의 Django 프레임워크 활용 예정
- Git을 통해 소스코드의 버전관리 예정
- Visual studio code를 이용하여 개발 및 디버그 수행 예정
- Draw.io 사이트를 이용하여 ERD, 유스케이스 다이어그램 작성 예정
- Balsamiq Mockup을 활용하여 와이어프레임 작성 예정



### 개발 방법론 설정 및 단계별 계획
- 혼자 작업을 하는 것이기 때문에 폭포수 모델을 기반한 계획 -> 요구사항 분석 -> 설계 -> 구현의 과정을 거칠 예정
- Django의 특성상 ORM을 이용해 데이터베이스 중심으로 작업이 이루어지기 때문에 ER도를 이용한 정보 모델링에 중점을 둘 예정
- 유스케이스를 활용하여 요구사항을 분석할 예정
- 설계 단계에서 DB설계 ( Django 필드 기반 ), 페이지 설계, 페이지 기능 설계 등을 할 예정


### 일정
- 계획 ( 11.1 ~ 11. 7 )
- 요구사항 분석 ( 11. 8 ~ 11.14 )
- 설계 ( 11. 15 ~ 11. 20 )
- 구현 ( 11. 21 ~ 12. 11 )

## 설계

### 유스케이스 설계
![usecase](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/50035e4e-68dd-40e8-9d24-cfb3e1af669a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210416T133005Z&X-Amz-Expires=86400&X-Amz-Signature=196e46ac50b6712c1f2dc3fc1970cfa17b208b3a792858facc7a9734badfcc6d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 페이지 계층 설계
![page](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb9ba8da-f790-434c-8698-da910febc7f0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210416T133100Z&X-Amz-Expires=86400&X-Amz-Signature=4e9b9cc87357b88032c13c4ff1ab801f0163ec3f33cc9d6a43cf346d10b89a1a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
### DB 설계
![erd](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c9a4e7a6-69bd-4b8d-bbcf-e374d8e7ea0a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210416T132736Z&X-Amz-Expires=86400&X-Amz-Signature=32f9bf6d79cae5e806e344069e6b17428d5e6ab6197cdec79de98b236497b16b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

