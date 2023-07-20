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



