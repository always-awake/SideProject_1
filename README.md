## 장고 기본 학습
### 01 개발환경 구축하기 (2/27)
- 웹프레임워크의 필요성
- 장고 설치
- 장고 프로젝트 생성하고 초기화하기

### 02 장고의 주요 구성 요소 (2/27)
- Function Based Views
- Models
- Templates
- 등..

### 03 장고 앱 (2/27)
- Tip: 앱의 규모가 커짐에 따라 models/views 모듈을 팩키지로 전환 -> 관리 용이

### 04 VSCode 장고 디버깅 세팅하기 (2/27)
- pipenv 실행시 디버깅: Command Palette 에서 Python: Select Interpreter 메뉴를 통해, 지정 가상환경 안의 인터프리터를 지정 -> 디버깅 진행

### 05 URLConf와 정규 표현식 (2/27)
- 간단한 정규표현식에 대한 이해
- 다양한 URL 패턴 : 정수, 년/월/일, slug
- path, re_path(url)

### 06 다양한 응답의 함수 기반 뷰 만들기 (2/27)
- What is View?
- FBV & CBV
- HttpRequest와 HttpResponse
- 다양한 타입의 Response (Excel, CSV, 이미지(Pillow))

### 07 적절한 HTTP 상태코드로 응답하기 (2/28)
모든 웹서버는 현재 요청에 대한 처리결과를 숫자코드로서 응답해야 합니다. 이것이 HTTP 상태코드입니다.

### 08 장고 쉘 (2/28)
- 장고 쉘을 사용하기 위해 -> 초기 세팅 필요(os, sys ...)

### 09 장고 모델 (ORM) (2/28)
- Django ORM(Object Relational Mapping) = Model 

### 10 장고 모델 필드 (2/28)
- Primary Key: AutoField
- 문자열: charField, TextField, SlugField
- 날짜/시간: DateTimeField
- 참/거짓: BooleanField
- 숫자: IntegerField, PositiveIntegerField
- 파일: FileField, ImageField
- 이메일: EmailField
- URL: URLField
- 등...
- 최대한 타이트하게 필드 지정하기 / 다양한 validator 사용하기

### 11 마이그레이션을 통한 데이터베이스 스키마 관리 (2/28)
- 마이그레이션 파일은 모델의 변화내역을 누적하는 역할 -> 이미 적용된 migration 파일 삭제하면 안됨
- 마이그레이션 파일이 너무 많아질 경우, squashmigrations 명령으로 다수의 마이그레이션 파일 통합 가능

### 12 장고 Admin을 통한 데이터 관리 (2/28)
- 실제 서비스에서는 Admin 페이지의 디폴트 경로 변경 권장
- 'django-admin-honeypot 앱'을 통해 가짜 Admin 페이지 노출 가능
- @admin.register(모델명) 데코레이터를 이용해 Admin 페이지에 모델 등록
- list_display, list_display_links, search_fields 등의 속성을 이용해 Admin 페이지 커스터마이징

### 13 모델을 통한 데이터 조회 (3/2)
- SQL을 생성해주는 인터페이스
- 순회가능한 객체 (Iterable)
- QuerySet은 Chaining 지원
- QuerySet을 만드는 동안에는 DB접근x -> 실제로 데이터가 필요한 시점(출력, list(), tuple(), for문과 함께 등)에 접근 (QuerySet의 Lazy한 특성)
- OR조건으로 filter -> from django.db.models import Q / ~.filter(Q(~) | Q(~))

### 14 모델을 통한 데이터 생성/수정/삭제 (3/2)
- SQL이 가급적 적게 생성되는 코드 선택하기 (병목현상의 주요 요인은 데이터베이스)
- 데이터를 일괄처리할 경우, QuerySet 함수를 사용하는 것이 좋음
- .save() 함수: 인스턴스 pk가 존재x -> INSERT / 인스턴스 pk가 존재o -> UPDATE (장고 내부 처리)

### 15 관계를 표현하는 모델 필드 (3/2)
- ManyToManyField의 경우, blank=True 설정, 사용하는 쪽에서 ManyToManyField 선언이 가독성에 좋음 

### 16 django-debug-toolbar를 통한 SQL 디버깅(3/11)
- 현재 request/response에 대한 대양한 디버깅 정보를 보여줌
- SQL Panel을 통해, 각 요청 처리 시에 발생한 SQL 내역 확인 가능 (Ajax 요청에 대한 내역은 미지원)
