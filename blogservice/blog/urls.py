from django.urls import path
from .views import CreatePostView, PostListView

app_name = 'blog'

urlpatterns = [
    # 글목록 조회
    path('', PostListView.as_view(), name='post_list'),
    # 글 생성
    path('post/create/', CreatePostView.as_view(), name='create_post'),
    
]
