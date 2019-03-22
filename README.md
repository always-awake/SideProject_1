## 장고 기본 학습
### 01 개발환경 구축하기
- 웹프레임워크의 필요성
- 장고 설치
- 장고 프로젝트 생성하고 초기화하기

### 02 장고의 주요 구성 요소
- Function Based Views
- Models
- Templates
- 등..

### 03 장고 앱
- Tip: 앱의 규모가 커짐에 따라 models/views 모듈을 팩키지로 전환 -> 관리 용이

### 04 VSCode 장고 디버깅 세팅하기
- pipenv 실행시 디버깅: Command Palette 에서 Python: Select Interpreter 메뉴를 통해, 지정 가상환경 안의 인터프리터를 지정 -> 디버깅 진행

### 05 URLConf와 정규 표현식
- 간단한 정규표현식에 대한 이해
- 다양한 URL 패턴 : 정수, 년/월/일, slug
- path, re_path(url)

### 06 다양한 응답의 함수 기반 뷰 만들기
- What is View?
- FBV & CBV
- HttpRequest와 HttpResponse
- 다양한 타입의 Response (Excel, CSV, 이미지(Pillow))

### 07 적절한 HTTP 상태코드로 응답하기
모든 웹서버는 현재 요청에 대한 처리결과를 숫자코드로서 응답해야 합니다. 이것이 HTTP 상태코드입니다.

### 08 장고 쉘
- 장고 쉘을 사용하기 위해 -> 초기 세팅 필요(os, sys ...)

### 09 장고 모델 (ORM)
- Django ORM(Object Relational Mapping) = Model 

### 10 장고 모델 필드
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

### 11 마이그레이션을 통한 데이터베이스 스키마 관리
- 마이그레이션 파일은 모델의 변화내역을 누적하는 역할 -> 이미 적용된 migration 파일 삭제하면 안됨
- 마이그레이션 파일이 너무 많아질 경우, squashmigrations 명령으로 다수의 마이그레이션 파일 통합 가능

### 12 장고 Admin을 통한 데이터 관리 
- 실제 서비스에서는 Admin 페이지의 디폴트 경로 변경 권장
- 'django-admin-honeypot 앱'을 통해 가짜 Admin 페이지 노출 가능
- @admin.register(모델명) 데코레이터를 이용해 Admin 페이지에 모델 등록
- list_display, list_display_links, search_fields 등의 속성을 이용해 Admin 페이지 커스터마이징

### 13 모델을 통한 데이터 조회
- SQL을 생성해주는 인터페이스
- 순회가능한 객체 (Iterable)
- QuerySet은 Chaining 지원
- QuerySet을 만드는 동안에는 DB접근x -> 실제로 데이터가 필요한 시점(출력, list(), tuple(), for문과 함께 등)에 접근 (QuerySet의 Lazy한 특성)
- OR조건으로 filter -> from django.db.models import Q / ~.filter(Q(~) | Q(~))

### 14 모델을 통한 데이터 생성/수정/삭제
- SQL이 가급적 적게 생성되는 코드 선택하기 (병목현상의 주요 요인은 데이터베이스)
- 데이터를 일괄처리할 경우, QuerySet 함수를 사용하는 것이 좋음
- .save() 함수: 인스턴스 pk가 존재x -> INSERT / 인스턴스 pk가 존재o -> UPDATE (장고 내부 처리)

### 15 관계를 표현하는 모델 필드
- ManyToManyField의 경우, blank=True 설정, 사용하는 쪽에서 ManyToManyField 선언이 가독성에 좋음 

### 16 django-debug-toolbar를 통한 SQL 디버깅
- 현재 request/response에 대한 대양한 디버깅 정보를 보여줌
- SQL Panel을 통해, 각 요청 처리 시에 발생한 SQL 내역 확인 가능 (Ajax 요청에 대한 내역은 미지원)
- 코드를 통한 SQL 내역 확인 가능: QuerySet의 query 속성 참조
  - print(Post.objects.all().query) / str(Post.objects.all().query)
  - 실제 문자열 참조 시에 SQL이 생성됨

### 17 장고 Logging과 SQL Logging 처리 -> 복습!
- 로그: 특정 형식으로 현 상황을 기록하는 문자열 기록
- 파이썬에서는 로깅을 기본적으로 지원
- 로그 레벨
  - DEBUG: 개발 환경에서 디버깅 목적
  - INFO: 분석이 필요한 유용한 상태 정보
  - WARNING: 중요도가 낮은 문제가 발생할 가능성 o / ex) 403 Forbidden, admin 침입 시도
  - ERROR: 상용 환경의 에러 / ex) 500/400 에라
  - CRITICAL: 빠른 대처가 요구되는 심각한 상황 / ex) 내부 API 서비스에 접근 불가(서비스 불능 상황)

### 19 장고 템플릿 엔진
- 템플릿: 단순히 html 응답뿐아니라, 복잡한 문자열을 좀 더 편리하게 조합할 수 있도록 도와주는 라이브러리
- "Stupid 장고 템플릿 언어"의 철학 / 장고의 기본 철학
  - 풍성한(Fat) Model
  - 비즈니스 로직이 없는(Stupid) Template
  - 간결한(Thin) View
- 템플릿 기능에 제한을 둠으로써, 비즈니스 로직을 템플릿 단에 구현함을 방지
  - 비즈니스 로직은 Model에, 그리고 Form/ModelForm을 통한 유효성 검사 및 저장을 권장
  - 다른 템플릿 엔진을 씀으로써, 이러한 제약에서 벗어날 수 있으나, 비권장
- 한 프로젝트에서 다수의 템플릿 엔진을 사용할 경우 -> 하나의 render수행 시에, 하나의 템플릿 엔진만 선택적으로 사용

### 25 static 파일을 다루는 방법
- static 파일이란?
- 개발 리소스로서의 정적인 파일 (js, css, image, font 등)
  - 위와 같은 정적인 파일을 웹 주소를 통해 접근(외부로 공개, 외부로부터 접근)하고자 할 때 사용
  - 웹 주소를 통해서가 아닌 내부 코드에 의해 접근하는 것이라면, 굳이 static 파일에 저장할 필요 없음
- 앱(특정 앱을 위한 static 파일들)/프로젝트 단위(2개 이상의 앱에서 사용하는 static 파일들)로 저장, 서빙
#### settings.py 내 static 파일 관련
- 공식 문서: https://docs.djangoproject.com/en/2.1/howto/static-files/
- STATIC_URL(필수)
  - 각 static 파일에 대한 URL Prefix
  - 템플릿 태구 {% static "경로" %}에 의해서 참조되는 설정
  - 항상 / 로 끝나도록 설정 (~/static파일명)
- STATICFILES_DIRS
  - 프로젝트 전반적으로 사용되는 static 파일의 위치(특정 앱만을 위한 static 파일은 장고가 알아서 로딩)
  - File System Loader에 의해 참조되는 설정
- STATIC_ROOT(필수)
  - python manage.py collectstatic 명령이 참조되는 설정
  - 여러 디렉토리(앱 단위 or 프로젝트 단위)로 나눠진 static 파일들을 이 경로의 디렉토리로 복사/서빙
  - 배포에서만 의미가 있는 설정
- Static Files Finders (Template Loader와 유사)
   - 설정된 Finders를 통해, static 템플릿이 있을 
   '디렉토리 목록'을 구성 (장고 서버를 시작할 때마다 1회 작성)
   - 디렉토리 목록에서 지정 상대 경로를 가지는 static 파일 찾기
- static 파일을 찾는 시기 (=Finder을 통해 static 파일을 찾는 시기)?
  - 개발 서버 구동 시, 매 static 파일들의 url 요청이 들어올 때마다 
  - 배포 할 때, python manage.py collectstatic 명령을 통해 각 static 파일들의 디렉토리 위치를 찾아 STATIC_ROOT위치에 static 파일 모두 복사할 때
#### 대표적인 2가지 Static Files Finders
- App Directories Finder: "장고앱/static/" 경로를 '디렉토리 목록'에 추가
- File System Finder settings.STATICFILES_DIRS 설정값을 '디렉토리 목록'에 추가
#
- Tip: 템플릿에서 static url 을 처리할 때, Template Tag를 통해 처리하기
  - 프로젝트 설정에 따라 또는 배포 환경에 따라 유연하게 static url prefix가 할당되기 때문이다.
  - {% load static %} 태그는 템플릿 가장 위, 상속 태그 다음에, 모든 개별 템플릿 마다 작성해주기
#
#### 개발 환경에서의 static 파일 서빙
- 개발 서버를 쓰고, (and) settings.DEBUG = True 일 때에만 static 서빙 지원
  - 프로젝트/url.py에 Rule이 따로 명시되지 않아도, 자동 Rule 추가 -> 이는 순수하게 '개발 목적'으로만 제공됨
- 개발 서버를 쓰지 않거나, (or) settings.DEBUG = False 일 때에는 별도로 static 서빙 설정을 해줘야 함.
#### static 서빙을 하는 여러가지 방법(3)
- 클라우드 정적 스토리지나 CDN 서비스를 활용
- apache/nginx 웹 서버를 통한 서빙
- 장고를 통한 서빙 (개발 단계에서 사용되는 방법)
  - whitenoise 라이브러리 활용 (ex. 해로쿠를 이용한 배포) / 공식문서: http://whitenoise.evans.io/en/stable/
#
- CDN(Content Delivery Network: 콘첸츠 전송 네트워크): 콘텐츠 전송 네트워크는 웹 애플리케이션 및 스트리밍 미디어를 비롯한 콘텐츠를 전송하도록 최적화된 전세계적으로 촘촘히 분산된 서버로 이루어진 플랫폼입니다. 이 서버 네트워크는 수많은 물리적 위치와 네트워크 위치에 분산되어 있어 웹 콘텐츠에 대한 엔드유저(클라이언트)의 요청에 직접적으로 응답하고 빠르고 안전한 미디어 전송을 보장합니다. CDN은 오리진이라고도 불리는 콘텐츠 서버와 엔드유저(클라이언트) 사이에서 중재자 역할을 합니다.
#
#### collectstatic 명령
- 실 서비스 배포 전에는 필히 본 명령을 통해, 여러 디렉토리에 나누어져 있는 static 파일들을 한 곳으로 복사해야한다.
- 복사하는 대상 디렉토리: settings.STATIC_ROOT
- 복사 이유
  - 여러 디렉토리에 나눠 저장한 static 파일들의 위치는 '현재 장고 프로젝트'만이 알고 있음/ 외부 웹서버는 전혀 알지 못함
  - 외부 웹서버에서 Finder의 도움 없이도 static 파일을 서빙하기 위함
  - 한 디렉토리에 모두 모여있기에, Finder의 도움 없이도 static 파일 서빙 가능
#### 외부 웹서버에 의한 static/media 컨텐츠 서빙
- 정적인 컨텐츠는 외부 웹서버를 통해 처리하면, 효율적인 처리 극대화 가능
- 정적 컨텐츠 최적화 방법 
  - memcache/redis 캐시 등
  - CDN(Content Delivery Network)

### 26 media 파일을 다루는 방법
- media 파일이란?
- FileField/ImageField를 통해 저장한 모든 파일
- (중요) DB필드에는 저장 경로를 저장하며, 파일은 파일 스토리지에 저장
- 프로젝트 단위로 저장/서빙