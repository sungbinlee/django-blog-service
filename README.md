# django-blog-service

Django로 개발된 블로그 서비스입니다.

## Use case diagram
![blog_use_case](https://github.com/sungbinlee/django-blog-service/assets/52542229/d2b3ac11-4a17-47f3-a252-cc6189ed0476)

추가기능: 게시글 좋아요, 댓글 좋아요, 이메일 인증

## ER diagram

![ERDblog](https://github.com/sungbinlee/django-blog-service/assets/52542229/70aa98f9-7ea9-45e6-854f-766ba31f4c82)

## 🎥 Demo
| 회원가입 |
|-----|
| ![ezgif-3-c719fd923b](https://github.com/sungbinlee/django-blog-service/assets/52542229/f9f79596-d195-4ace-9dfd-4d74a17c9644)|
| 이메일 인증 |
|<img width="686" alt="스크린샷 2023-10-13 오후 1 59 50" src="https://github.com/sungbinlee/django-blog-service/assets/52542229/388b0186-3a2d-47c2-8eaf-52e05b9895b4"> |
| 로그인 |
|![ezgif-3-c04de768c8](https://github.com/sungbinlee/django-blog-service/assets/52542229/de44be85-b56e-4419-b65a-ae9ac2164643)|
| 블로그 |
|![ezgif-3-bd287a80ff](https://github.com/sungbinlee/django-blog-service/assets/52542229/23da3440-fa80-47d7-aad3-b9f23f4a4518)|
| 검색기능(태그, 제목) |
| ![ezgif-3-feea1fa9cd](https://github.com/sungbinlee/django-blog-service/assets/52542229/f2efd39b-345b-428a-8e92-b9d674fc9bb1) |
| 댓글 작성 및 삭제, 좋아요 기능 |
| ![ezgif-3-086428c532 (1)](https://github.com/sungbinlee/django-blog-service/assets/52542229/eb0c3dfd-43e4-4689-9d8b-19ffc11993e5)|
| 게시글 작성 및 삭제 |
| ![ezgif-3-458a1ad1ea](https://github.com/sungbinlee/django-blog-service/assets/52542229/9e560bb3-3129-4230-9d70-b333f22eed38) |

## 기능 정리

|          기능           |                                URL                                 | 구현 |
| :---------------------: | :----------------------------------------------------------------: | ---- |
|     메인페이지     |                                 /                                  | v    |
|   회원가입 기능    |                             /register                              | v    |
|    로그인 기능     |                               /login                               | v    |
|   로그아웃 기능    |                              /logout                               | v    |
|  게시글 작성 기능  |                            /blog/write                             | v    |
|  게시글 목록 기능  |                               /blog                                | v    |
|  게시글 상세보기 기능   |                         /blog/int:post_id                          | v    |
|  게시글 검색 기능  |                        /blog/search/str:tag                        | v    |
|  게시글 수정 기능  |                       /blog/edit/int:post_id                       | v    |
|  게시글 삭제 기능  |                      /blog/delete/int:post_id                      | v    |
|   댓글 작성 기능   |                  /blog/int:post_id/comment/create                  | v    |
|   댓글 수정 기능  |           /blog/int:post_id/comment/edit/int:comment_id            | v    |
|   댓글 삭제 기능   |          /blog/int:post_id/comment/delete/int:comment_id           | v    |
|  댓글 좋아요 기능  |           /blog/int:post_id/comment/int:comment_id/like            | v    |
| 게시물 좋아요 기능 |                       /blog/int:post_id/like                       | v    |
|  대댓글 작성 기능  |       /blog/int:post_id/comment/int:comment_id/reply/create        | v    |
|  대댓글 수정 기능  |  /blog/int:post_id/comment/int:comment_id/reply/edit/int:reply_id  | v    |
|  대댓글 삭제 기능  | /blog/int:post_id/comment/int:comment_id/reply/delete/int:reply_id | v    |
|       프로필 설정       |                         /profile/update/                             |   v |
|       이메일 발송       |                   /verification-sent/                        |   v |
|       이메일 인증       |                /verify-email/<str:uidb64>/<str:token>/                |   v |
|     태그 추가, 삭제     |                                N/A                                 | V    |
|         조회 수         |                                N/A                                 | V    |
|        사진 첨부        |                                N/A                                 |  v  |

## 배포 환경
배포 환경에는 Nginx + Gunicorn으로 AWS에 Django 애플리케이션을 배포하였습니다. 

### 왜 runserver로 배포하면 안되는가?
`runserver`는 Django 개발 단계에서 테스트 목적으로 사용하는 간단한 개발용 서버입니다. 실제 운영 환경에서는 다음과 같은 이유로 `runserver`를 사용해서는 안 됩니다:

1. 보안 문제: `runserver`는 간단한 기능만 제공하며 보안에 취약합니다. 운영 환경에서 사용할 경우 보안 위협에 쉽게 노출될 수 있습니다.

2. 성능 문제: `runserver`는 단일 스레드로 동작하여 동시에 여러 요청을 처리하기 어렵습니다. 실제 운영 환경에서는 다수의 요청을 처리해야 하므로 다중 스레드 또는 다중 프로세스로 동작해야 합니다.

3. 스케일링: `runserver`는 단일 프로세스로 동작하여 스케일링이 어렵습니다. 실제 운영 환경에서는 다수의 서버 인스턴스로 확장하여 부하를 분산시키는 것이 필요합니다.

4. 안정성: `runserver`는 개발용이므로 오류가 발생하거나 비정상적인 상태에서도 자동으로 다시 시작되지 않습니다. 반면 실제 운영 환경에서는 안정성을 보장하기 위해 자동 복구 기능이 필요합니다.

### Django + Nginx + Gunicorn으로 배포하기
Django 애플리케이션을 실제 운영 환경에 배포하기 위해 다음과 같은 구성을 사용합니다:

- Gunicorn: WSGI(Web Server Gateway Interface) 서버로, Django 애플리케이션을 다중 프로세스로 실행하여 동시에 여러 요청을 처리할 수 있도록 합니다.

- Nginx: Reverse Proxy 서버로, 정적 파일 처리와 로드 밸런싱을 담당하여 애플리케이션 서버의 부하를 분산시키고 안정성과 성능을 향상시킵니다.

### 배포 환경의 중요성
배포 환경은 애플리케이션을 실제 사용자에게 제공하는 단계로, 다수의 사용자가 접속하고 안정성과 성능이 중요한 요소입니다. 실제 운영 환경에서 발생하는 다양한 상황에 대비하여 안정성을 보장하고 성능을 최적화하는 것이 중요합니다. Nginx + Gunicorn과 같은 배포 환경을 구성하여 웹 애플리케이션을 효과적으로 배포하고 운영할 수 있습니다.

## 이메일 인증 기능
이메일 인증 기능은 사용자가 회원가입을 진행한 후, 회원가입한 이메일 주소가 유효하고 접근 가능한지 확인하기 위해 사용되는 기능입니다. 이메일 인증이 완료된 사용자만 로그인이 가능하도록 제한할 수 있으며, 이를 통해 사용자의 계정 보안을 강화할 수 있습니다. 이를 위해 다음과 같은 원리로 구현하였습니다:

1. 이메일 템플릿 작성: 인증 이메일을 보낼 때 사용자의 정보를 동적으로 삽입하기 위해 이메일 템플릿을 작성하였습니다. 템플릿에는 사용자의 이름, 인증 링크 등이 포함되어 있습니다.

2. 인증 URL 생성: 회원가입 시 사용자의 정보와 토큰을 기반으로 인증 링크를 생성합니다. 이 링크는 사용자의 이메일 주소를 확인하고 계정을 활성화하는 데 사용됩니다.

3. 이메일 보내기: 생성된 인증 링크를 사용자의 이메일 주소로 전송합니다. 이메일 전송은 Django의 `send_mail()` 함수를 사용하며, SSL 인증 관련 설정을 적절히 처리해야 합니다.

4. 인증 확인: 사용자가 이메일 링크를 클릭하여 접속하면 해당 링크의 정보를 통해 사용자를 인증합니다. 인증은 토큰을 검증하고 사용자 계정을 활성화하는 과정을 거칩니다.

5. 인증 상태 관리: 인증이 완료된 사용자는 로그인이 가능하며, 사용자 모델의 `is_active` 속성을 활용하여 활성화 상태를 관리합니다.

## 환경변수 설정
환경변수 설정은 애플리케이션에 필요한 중요한 설정 정보들을 외부에 저장하고 관리하기 위한 방법입니다. 이 방식을 사용함으로써 애플리케이션 코드에 직접 설정 값을 작성하는 것을 피하고, 보안적인 이점과 설정 관리의 편의성을 제공합니다.

여기에서는 `environ` 라이브러리를 사용하여 환경변수를 관리하고 있습니다. `.env` 파일에 설정 값을 작성하고, `environ.Env.read_env()` 함수를 통해 해당 파일에서 설정 값을 읽어옵니다. 이렇게 하면 애플리케이션 코드에서는 환경변수를 직접 사용하면서도 보안적인 이점을 얻을 수 있습니다.

> .env 파일에는 중요한 정보를 포함해도 됩니다. 하지만 .env 파일 자체를 보안에 취약한 곳에 저장하거나, 누출되지 않도록 주의해야 합니다. 보안을 위해서 .env 파일은 .gitignore 파일에 등록하여 버전 관리 시스템에 포함되지 않도록 해야 합니다.

### 환경변수 설정의 중요성
1. 보안 강화: 중요한 정보인 SECRET_KEY와 비밀번호 등을 코드에 하드코딩하는 것은 보안상 위험합니다. 환경변수를 사용하면 애플리케이션 코드에 민감한 정보가 노출되지 않아 보안성이 향상됩니다.

2. 설정 관리 용이성: 애플리케이션의 설정 값을 외부 파일에 작성하고 관리함으로써, 설정을 변경하거나 업데이트하는 데 용이합니다. 설정 값을 변경할 때 코드를 수정할 필요 없이 .env 파일만 수정하면 됩니다.

## 설치 및 실행

1. 해당 프로젝트를 클론합니다.

```
git clone https://github.com/sungbinlee/django-blog-service.git
```

2. 가상환경을 생성하고 필요한 패키지를 설치합니다:

```
python -m venv venv
source venv/bin/activate  # Windows에서는 "venv\Scripts\activate" 실행
pip install -r requirements.txt
```

3. 데이터베이스를 마이그레이션합니다:

```
python manage.py migrate
```

4. 환경변수 파일을 작성합니다. (manage.py와 동일한 위치에)
```
vi .env
```
```
#EMAIL={"EMAIL_BACKEND": "django.core.mail.backends.smtp.EmailBackend","EMAIL_USE_TLS": "True","EMAIL_PORT": "587","EMAIL_HOST": "smtp.gmail.com","EMAIL_HOST_USER": "[사용자 계정]","EMAIL_HOST_PASSWORD": "[사용자 비밀번호]"}

SECRET_KEY="[사용자 시크릿 키]"
```

5. 개발 서버를 실행합니다:

```
python manage.py runserver
```

서버가 성공적으로 실행되면 브라우저에서 http://localhost:8000/ 으로 접속하여 블로그 웹 애플리케이션을 사용할 수 있습니다.

## 기술 문서
기술문서를 참조하려면  [`technical-documentation.pdf`](https://github.com/sungbinlee/django-blog-service/blob/main/technical-documentation.pdf) 파일을 확인해주세요.
