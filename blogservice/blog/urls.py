from django.urls import path
from .views import CreatePostView, PostListView, PostDetailView, PostUpdateView, PostDeleteView


app_name = 'blog'

urlpatterns = [
    # 글목록 조회
    path('', PostListView.as_view(), name='post_list'),
    # 글 생성
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
]
