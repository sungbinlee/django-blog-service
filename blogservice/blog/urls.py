from django.urls import path
from .views import CreatePostView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, CreateCommentView, UpdateCommentView, DeleteCommentView


app_name = 'blog'

urlpatterns = [
    # 글목록 조회
    path('', PostListView.as_view(), name='post_list'),
    # 글 CRUD
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('<int:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:post_id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # 댓글 CRUD
    path('<int:post_id>/comment/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:comment_id>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:comment_id>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
