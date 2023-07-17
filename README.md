# django-blog-service
Django로 개발된 블로그 서비스입니다.

## Use case diagram
![blog_use_case](https://github.com/sungbinlee/django-blog-service/assets/52542229/d2b3ac11-4a17-47f3-a252-cc6189ed0476)

## ER diagram
![ERDblog](https://github.com/sungbinlee/django-blog-service/assets/52542229/70aa98f9-7ea9-45e6-854f-766ba31f4c82)

## 기능 정리
| 기능                    | URL                                                                      |
|-------------------------|--------------------------------------------------------------------------|
| 메인페이지 구현         | /                                                                        |
| 회원가입 기능 구현      | /register                                                                |
| 로그인 기능 구현        | /login                                                                   |
| 로그아웃 기능 구현      | /logout                                                                  |
| 게시글 작성 기능 구현   | /blog/write                                                              |
| 게시글 목록 기능 구현   | /blog                                                                    |
| 게시글 상세보기 기능    | /blog/<int:post_id>                                                      |
| 게시글 검색 기능 구현   | /blog/search/<str:tag>                                                   |
| 게시글 수정 기능 구현   | /blog/edit/<int:post_id>                                                 |
| 게시글 삭제 기능 구현   | /blog/delete/<int:post_id>                                               |
| 댓글 작성 기능 구현     | /blog/<int:post_id>/comment/create                                       |
| 댓글 수정 기능 구현     | /blog/<int:post_id>/comment/edit/<int:comment_id>                        |
| 댓글 삭제 기능 구현     | /blog/<int:post_id>/comment/delete/<int:comment_id>                      |
| 댓글 좋아요 기능 구현   | /blog/<int:post_id>/comment/<int:comment_id>/like                        |
| 게시물 좋아요 기능 구현 | /blog/<int:post_id>/like                                                 |
| 대댓글 작성 기능 구현   | /blog/<int:post_id>/comment/<int:comment_id>/reply/create                |
| 대댓글 수정 기능 구현   | /blog/<int:post_id>/comment/<int:comment_id>/reply/edit/<int:reply_id>   |
| 대댓글 삭제 기능 구현   | /blog/<int:post_id>/comment/<int:comment_id>/reply/delete/<int:reply_id> |
