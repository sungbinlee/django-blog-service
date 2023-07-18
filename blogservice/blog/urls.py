from django.urls import path
from .views import CreatePostView

app_name = 'blog'

urlpatterns = [
    path('post/create/', CreatePostView.as_view(), name='create_post'),
]
