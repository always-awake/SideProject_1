## 장고 기본 학습
<<<<<<< HEAD
=======

>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
### 01 개발환경 구축하기
- 웹프레임워크의 필요성
- 장고 설치
- 장고 프로젝트 생성하고 초기화하기

<<<<<<< HEAD
### 02 장고의 주요 구성 요소
=======
### 02 장고의 주요 구성 요소 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- Function Based Views
- Models
- Templates
- 등..

### 03 장고 앱
- Tip: 앱의 규모가 커짐에 따라 models/views 모듈을 팩키지로 전환 -> 관리 용이

<<<<<<< HEAD
### 04 VSCode 장고 디버깅 세팅하기
=======
### 04 VSCode 장고 디버깅 세팅하기 

>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- pipenv 실행시 디버깅: Command Palette 에서 Python: Select Interpreter 메뉴를 통해, 지정 가상환경 안의 인터프리터를 지정 -> 디버깅 진행

### 05 URLConf와 정규 표현식
- 간단한 정규표현식에 대한 이해
- 다양한 URL 패턴 : 정수, 년/월/일, slug
- path, re_path(url)

<<<<<<< HEAD
### 06 다양한 응답의 함수 기반 뷰 만들기
=======
### 06 다양한 응답의 함수 기반 뷰 만들기 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- What is View?
- FBV & CBV
- HttpRequest와 HttpResponse
- 다양한 타입의 Response (Excel, CSV, 이미지(Pillow))

### 07 적절한 HTTP 상태코드로 응답하기
모든 웹서버는 현재 요청에 대한 처리결과를 숫자코드로서 응답해야 합니다. 이것이 HTTP 상태코드입니다.

<<<<<<< HEAD
### 08 장고 쉘
- 장고 쉘을 사용하기 위해 -> 초기 세팅 필요(os, sys ...)

### 09 장고 모델 (ORM)
- Django ORM(Object Relational Mapping) = Model 

### 10 장고 모델 필드
=======
### 08 장고 쉘 
- 장고 쉘을 사용하기 위해 -> 초기 세팅 필요(os, sys ...)

### 09 장고 모델 (ORM) 
- Django ORM(Object Relational Mapping) = Model 

### 10 장고 모델 필드 

>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
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

<<<<<<< HEAD
### 11 마이그레이션을 통한 데이터베이스 스키마 관리
=======
### 11 마이그레이션을 통한 데이터베이스 스키마 관리 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- 마이그레이션 파일은 모델의 변화내역을 누적하는 역할 -> 이미 적용된 migration 파일 삭제하면 안됨
- 마이그레이션 파일이 너무 많아질 경우, squashmigrations 명령으로 다수의 마이그레이션 파일 통합 가능

### 12 장고 Admin을 통한 데이터 관리 
- 실제 서비스에서는 Admin 페이지의 디폴트 경로 변경 권장
- 'django-admin-honeypot 앱'을 통해 가짜 Admin 페이지 노출 가능
- @admin.register(모델명) 데코레이터를 이용해 Admin 페이지에 모델 등록
- list_display, list_display_links, search_fields 등의 속성을 이용해 Admin 페이지 커스터마이징

<<<<<<< HEAD
### 13 모델을 통한 데이터 조회
=======
### 13 모델을 통한 데이터 조회 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- SQL을 생성해주는 인터페이스
- 순회가능한 객체 (Iterable)
- QuerySet은 Chaining 지원
- QuerySet을 만드는 동안에는 DB접근x -> 실제로 데이터가 필요한 시점(출력, list(), tuple(), for문과 함께 등)에 접근 (QuerySet의 Lazy한 특성)
- OR조건으로 filter -> from django.db.models import Q / ~.filter(Q(~) | Q(~))

<<<<<<< HEAD
### 14 모델을 통한 데이터 생성/수정/삭제
=======
### 14 모델을 통한 데이터 생성/수정/삭제 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
- SQL이 가급적 적게 생성되는 코드 선택하기 (병목현상의 주요 요인은 데이터베이스)
- 데이터를 일괄처리할 경우, QuerySet 함수를 사용하는 것이 좋음
- .save() 함수: 인스턴스 pk가 존재x -> INSERT / 인스턴스 pk가 존재o -> UPDATE (장고 내부 처리)

<<<<<<< HEAD
### 15 관계를 표현하는 모델 필드
=======
### 15 관계를 표현하는 모델 필드 
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
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
<<<<<<< HEAD
#### media 파일이란?
- FileField/ImageField를 통해 저장한 모든 파일 (다른 언어의 프레임워크에서는 없는 용어)
- (중요) DB필드에는 저장 경로를 저장하며, 파일은 별도의 파일 스토리지에 저장
- 프로젝트 단위로 저장/서빙
#### Media 파일 처리 순서
- HttpRequest.FILES(request의 인자)를 통해 파일이 전달
- View 로직이나 Form 로직을 통해, 유효성 검증을 수행
- FileField/ImageField에 "경로(문자열)"을 저장
- settings.MEDIA_ROOT 경로의 하위 파일을 저장 (이 이외의 경로에는 파일을 저장하지 않는다.)
#### settings.py의 Media 파일 관련 설정
- 기본적으로 MEDIA관련 설정인 MEDIA_URL = ""/MEDIA_ROOT="" 인 상태로 media 파일을 업로드 한다면, manage.py 파일과 같은 경로에 저장됨 -> 따라서 필수적으로 media 파일 관련 설정을 해야함
- MEDIA_URL: 각 media 파일에 대한 URL Prefix
  - 필드명.url 속성에 의해서 참조되는 설정
- MEDIA_ROOT: 파일 필드를 통한 저장 시, 실제 파일을 저장할 ROOT 경로
#### FileField와 ImageField
- FileField
  - File Storage API를 통해 파일을 저장 (장고에서는 로컬 File System Storage만 지원, django-storages를 통해 AWS S3, Azure storage, Google Cloud storage 등으로의 확장 지원)
  - 해당 필드를 옵션 필드로 두고자 할 경우, blank=True 옵션 적용
- ImageField (FileField 상속)
  - Pillow(이미지 처리 라이브러리)를 통해 이미지 width/height 획득
  - Pillow를 설치하지 않을 경우, ImageField를 추가한 makemigrations 수행 실패함
- 위 필드를 상속받은 커스텀 필드를 만들 수 있음 (ex. PDFField, ExcelField 등)
#### 유용한 필드 옵션
- blank 옵션
  - 업로드 옵션 처리 여부 (필수 옵션 여부)
  - 디폴트: False
- upload_to 옵션
  - settings.MEDIA_ROOT 경로 내 어디에 저장될지 지정하는 옵션
  - 디폴트: 파일명 그대로 settings.MEDIA_ROOT에 정리 되지 않고 저장됨
  - 동일 파일명으로 저장 시, 기존 파일이 오버라이트되지 않고, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지
- upload_to 인자
  - 파일 저장 시, upload_to 함수를 호출하여, media 파일 저장 경로를 계산
  - 몇 개의 파일을 저장한 후에 upload_to 인자를 변경한다고 해서, 이전에 DB내 기존 upload_to 인자의 경로로 저장됬던 미디어 파일들이 새로운 upload_to 인자 경로에 저장되지 않는다. 때문에 기존 경로에 저장됬던 파일들을 새로운 upload_to 경로로 재업로드해야함
  - 문자열 인자: 파일을 저장할 "중간 디렉토리 경로"로서 활용 (ex. blog)
  - 함수 인자: "중간 디렉토리 경로" 및 "파일명"까지 결정 가능
#### uuid를 통한 파일명 정하기 예시 (upload_to의 인자를 함수로)
```
import os
from uuid import uuid4
from django.utils import timezone
def uuid_name_upload_to(instance, filename):
   app_label = instance.__class__._meta.app_label # 앱별로
   cls_name = instance.__class__.__name__.lower() # 모델 별로
   ymd_path = timezone.now().strftime('%Y/%m/%d’) # 업로드 하는 년/월/일 별로
   uuid_name = uuid4().hex
   extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환 return '/'.join([
      app_label,
      cls_name,
      ymd_path,
      uuid_name[:2],
      uuid_name + extension,
])
```
#
#### os.path.splitext(filename)
- 입력 받은 경로를 확장자 부분과 그 외의 부분으로 나눕니다.
- 단순한 문자열 연산이므로 실제 파일의 존재 여부는 확인하지 않습니다.
```
In: splitext('C:\\Python30\\python.exe')
Out: ('C:\\Python30\\python', '.exe') # 튜플로 리턴
```
#
#### Tip
- 성능을 위해, 한 디렉토리에 너무 많은 파일들이 저장되지 않도록 조정하기
- 한 디렉토리에 파일을 너무 많이 몰아둘 경우, OS 파일 찾기 성능이 저하됨
- 디렉토리 깊이가 깊어지는 것은 성능에 큰 영향이 없음
- 필드 별로, 다른 디렉토리 저장경로를 갖는 것이 좋은
  - 대안1: 필드 별로 다른 디렉토리에 저장 
  - photo = models.ImageField(upload_to=“blog”)
  - photo = models.ImageField(upload_to=“blog/photo”)
  - 대안2: 업로드 시간대 별로 다른 디렉토리에 저장
  - upload_to에서 strftime 포맷팅을 자동 지원
  - photo = models.ImageField(upload_to=“blog/%Y/%m/%d”)
- 아마존 S3, Azure Storage 등에서도 적용하면 좋은 Tip
#### 파일 업로드 시에 HTML Form enctype
- form method는 필히 POST로 지정
  - GET의 경우 enctype이 "application/x-www-form-urlencoded"로 고정
- form enctype을 필히 "multipart/form-data"로 지정 -> 지정하지 않는다면, 브라우저는 파일을 서브하지 않고, 파일명만 서브한다. 즉, 파일이 업로드가 되지 않음
  - "application/x-www-form-urlencoded"의 경우, 파일명만 전송
  - "multipart/form-data"을 입력하는 도중에 오타가 있으면, "application/x-www-form-urlencoded"로 지정되어, 파일명만 전송
```
<form action="" method="post" enctype="multipart/form-data">
   {% csrf_token %}
   <table>
      {{ form.as_table }}
   </table>
   <input type="submit">
</form>
```

#### 템플릿에서 media URL 처리 예시
- 필드의 .url 속성 활용
  - 내부적으로 settings.MEDIA_URL과 조합하여 처리함
  `<img src="{{ post.photo.url }}" %}" />`
  - 필드에 저장된 경로에 파일이 없을 경우, .url 계산에 실패함 때문(ValueError: no file associated with it.)에 안전하게 필드명 저장유무를 체크해주는 것이 좋음
  ```
   {% if post.photo %}
      <img src="{{ post.photo.url }}" %}" />
   {% endif %}
  ```
  - 출력: `/media/shop/item/2019/03/22/9f/9fcb448231314cd6ba3a04422c6ceefe.png`
- 참고: 파일 시스템 상의 절대 경로가 필요하다면, .path 속성을 활용
  - 출력: `/Users/leemirim/Documents/SideProject_1/sideproject/media/shop/item/2019/03/22/9f/9fcb448231314cd6ba3a04422c6ceefe.png` 
  - 오직 로컬에서만 유효


#### 개발환경에서의 media 파일 서빙
- static 파일과 다르게, 장고 개발 서버에서 서빙을 지원하지 않음
- 개발 편의성 목적으로 url.py에 직접 서빙 Rule을 추가

#### File Upload Handler
- 파일 크기가 2.5MB 이하일 경우
  - 파일은 메모리에 담겨 전달됨
  - MemoryFileUploadHandler
- 파일 크기가 2.5MB 초과일 경우
  - 디스크에 담겨 전달
  - TemporaryFileUploadHandler
- 관련 설정
  - settings.FILE_UPLOAD_MAX_MEMORY_SIZE (디폴트 설정 값: 2.5MB)
=======
- media 파일이란?
- FileField/ImageField를 통해 저장한 모든 파일
- (중요) DB필드에는 저장 경로를 저장하며, 파일은 파일 스토리지에 저장
- 프로젝트 단위로 저장/서빙
>>>>>>> 548cf7a8c938d91f08ecb7a48f3e91fa973ba4d9
