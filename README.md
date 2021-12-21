# PickMePickMe
## Subgroup2 진행 상황
- 입후보 신청서 등록/확인/수정 구현 완료 
- 공보물 등록/확인/수정 구현 완료
- 선거 결과 확인

## 사이트 이용 방법
### 입후보 신청 목록 확인
- 주소: localhost:{port_num}/promotions

### 입후보 신청
- 주소: localhost:{port_num}/promotions/new

### 선거 결과 확인
- 주소: localhost:{port_num}/elections/{election-id}/result/

## Sprint1 (~12/01)
- 기존에는 입후보 등록 과정을 간략히 하고 입후보 등록이 완료된 후 공보물 관리를 수행할 수 있도록 설계하였습니다.
- 하지만 후보자의 정보를 추후 유권자들이 확인해야하는 과정이 필요하기 때문에 입후보 등록 과정을 상세히 하여 후보자의 정보를 먼저 작성할 수 있게 하였습니다.

---

## Subgroup3 진행 상황
- 선거 등록/수정/삭제中 선거 등록 구현 완료 
- 유저 관리 기능中 회원가입, 로그인 구현 완료

## 사이트 이용 방법
### 입후보 신청
- 주소: localhost:{port_num}/promotions/  
- 입력 필드: 제목, 본문, 기호, 정당, 이름, 성별, 생년월일, 직업, 학력, 경력, 공약, 공보물, 선거(선거 모델과 연결 예정)

### 공보물
- localhost:{port_num}/portfolios/  
- 입력 필드: 제목, 본문, 포스터, 후보자 이름(유저 모델과 연결 예정)
### 회원 가입
- 주소: localhost:{port_num}/users/signup  
- 입력 필드: 성, 이름, 이메일, 주민등록번호, 성별, 거주지-시, 거주지-구, 패스워드, 패스워드 확인


### 로그인
- 주소: localhost:{port_num}/elections/register  
- 입력 필드: 이메일, 패스워드
---

