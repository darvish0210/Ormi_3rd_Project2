# LGooogle
-LG Twins 팬 블로그

## 1. 목표와 기능

+ 회원가입, 로그인, 로그아웃 기능
+ 글 쓰기는 회원만이 가능
+ 글 삭제 및 수정은 작성자만이 가능 : 작성자가 아닌 회원이 수행하려 할 시 403 Forbidden
+ 글 검색 및 조회는 비회원도 가능

## 2. 개발환경 및 사용언어, 라이브러리

+ Visual Studio Code : ver 1.81.1
+ Chromium: 108.0.5359.215
+ OS: Windows_NT x64 10.0.25336

+ python 3.12
+ Django 4.2.7

## 3. 개발일정



## 4. 프로젝트 구조

├─blog
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_post_modified_date.py
│  │  │  0003_post_views.py
│  │  │  0004_remove_post_modified_date.py
│  │  │  0005_alter_post_views.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-312.pyc
│  │          0002_post_modified_date.cpython-312.pyc
│  │          0003_post_views.cpython-312.pyc
│  │          0004_remove_post_modified_date.cpython-312.pyc
│  │          0005_alter_post_views.cpython-312.pyc
│  │          __init__.cpython-312.pyc
│  │          
│  ├─templates
│  │  ├─blog
│  │  │      base.html
│  │  │      post-confirm-delete.html
│  │  │      post-detail.html
│  │  │      post-form.html
│  │  │      post-list.html
│  │  │      signup.html
│  │  │      
│  │  │      
│  │  └─registration
│  │          logged_out.html
│  │          login.html
│  │          
│  └─__pycache__
│          admin.cpython-312.pyc
│          apps.cpython-312.pyc
│          forms.cpython-312.pyc
│          models.cpython-312.pyc
│          urls.cpython-312.pyc
│          views.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─myblog
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-312.pyc
│          urls.cpython-312.pyc
│          wsgi.cpython-312.pyc
│          __init__.cpython-312.pyc

## 5. 순서도

