# django-blog-service

Django로 개발된 블로그 서비스입니다.

## Use case diagram
![blog_use_case](https://github.com/sungbinlee/django-blog-service/assets/52542229/d2b3ac11-4a17-47f3-a252-cc6189ed0476)

추가기능: 게시글 좋아요, 댓글 좋아요

## ER diagram

![ERDblog](https://github.com/sungbinlee/django-blog-service/assets/52542229/70aa98f9-7ea9-45e6-854f-766ba31f4c82)

## 기능 정리

|          기능           |                                URL                                 | 구현 |
| :---------------------: | :----------------------------------------------------------------: | ---- |
|     메인페이지 구현     |                                 /                                  | v    |
|   회원가입 기능 구현    |                             /register                              | v    |
|    로그인 기능 구현     |                               /login                               | v    |
|   로그아웃 기능 구현    |                              /logout                               | v    |
|  게시글 작성 기능 구현  |                            /blog/write                             | v    |
|  게시글 목록 기능 구현  |                               /blog                                | v    |
|  게시글 상세보기 기능   |                         /blog/int:post_id                          | v    |
|  게시글 검색 기능 구현  |                        /blog/search/str:tag                        | v    |
|  게시글 수정 기능 구현  |                       /blog/edit/int:post_id                       | v    |
|  게시글 삭제 기능 구현  |                      /blog/delete/int:post_id                      | v    |
|   댓글 작성 기능 구현   |                  /blog/int:post_id/comment/create                  | v    |
|   댓글 수정 기능 구현   |           /blog/int:post_id/comment/edit/int:comment_id            | v    |
|   댓글 삭제 기능 구현   |          /blog/int:post_id/comment/delete/int:comment_id           | v    |
|  댓글 좋아요 기능 구현  |           /blog/int:post_id/comment/int:comment_id/like            | v    |
| 게시물 좋아요 기능 구현 |                       /blog/int:post_id/like                       | v    |
|  대댓글 작성 기능 구현  |       /blog/int:post_id/comment/int:comment_id/reply/create        | v    |
|  대댓글 수정 기능 구현  |  /blog/int:post_id/comment/int:comment_id/reply/edit/int:reply_id  | v    |
|  대댓글 삭제 기능 구현  | /blog/int:post_id/comment/int:comment_id/reply/delete/int:reply_id | v    |
|     태그 추가, 삭제     |                                N/A                                 | V    |
|         조회 수         |                                N/A                                 | V    |
|        사진 첨부        |                                N/A                                 |  v  |
|       프로필 설정       |                         profile/update/                             |   v |

## 이메일 인증 기능
이메일 인증 기능은 사용자가 회원가입을 진행한 후, 회원가입한 이메일 주소가 유효하고 접근 가능한지 확인하기 위해 사용되는 기능입니다. 이메일 인증이 완료된 사용자만 로그인이 가능하도록 제한할 수 있으며, 이를 통해 사용자의 계정 보안을 강화할 수 있습니다. 이를 위해 다음과 같은 원리로 구현하였습니다:

1. 이메일 템플릿 작성: 인증 이메일을 보낼 때 사용자의 정보를 동적으로 삽입하기 위해 이메일 템플릿을 작성하였습니다. 템플릿에는 사용자의 이름, 인증 링크 등이 포함되어 있습니다.

2. 인증 URL 생성: 회원가입 시 사용자의 정보와 토큰을 기반으로 인증 링크를 생성합니다. 이 링크는 사용자의 이메일 주소를 확인하고 계정을 활성화하는 데 사용됩니다.

3. 이메일 보내기: 생성된 인증 링크를 사용자의 이메일 주소로 전송합니다. 이메일 전송은 Django의 `send_mail()` 함수를 사용하며, SSL 인증 관련 설정을 적절히 처리해야 합니다.

4. 인증 확인: 사용자가 이메일 링크를 클릭하여 접속하면 해당 링크의 정보를 통해 사용자를 인증합니다. 인증은 토큰을 검증하고 사용자 계정을 활성화하는 과정을 거칩니다.

5. 인증 상태 관리: 인증이 완료된 사용자는 로그인이 가능하며, 사용자 모델의 `is_active` 속성을 활용하여 활성화 상태를 관리합니다.

## 환경변수 설정
환경변수 설정은 애플리케이션에 필요한 중요한 설정 정보들을 외부에 저장하고 관리하기 위한 방법입니다. 이 방식을 사용함으로써 애플리케이션 코드에 직접 설정 값을 작성하는 것을 피하고, 보안적인 이점과 설정 관리의 편의성을 제공합니다.

저는 `environ` 라이브러리를 사용하여 환경변수를 관리하고 있습니다. `.env` 파일에 설정 값을 작성하고, `environ.Env.read_env()` 함수를 통해 해당 파일에서 설정 값을 읽어옵니다. 이렇게 하면 애플리케이션 코드에서는 환경변수를 직접 사용하면서도 보안적인 이점을 얻을 수 있습니다.

```.env 파일에는 중요한 정보를 포함해도 됩니다. 하지만 .env 파일 자체를 보안에 취약한 곳에 저장하거나, 누출되지 않도록 주의해야 합니다. 보안을 위해 .env 파일은 .gitignore 파일에 등록하여 버전 관리 시스템에 포함되지 않도록 해야 합니다.```

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

4. 개발 서버를 실행합니다:

```
python manage.py runserver
```

서버가 성공적으로 실행되면 브라우저에서 http://localhost:8000/ 으로 접속하여 블로그 웹 애플리케이션을 사용할 수 있습니다.



