from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PostForm
from .models import Post


class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_create.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post_id=post.id)
        else:
            context = {
                'form': form
            }
            return render(request, 'blog/post_create.html', context)


class PostListView(View):
    def get(self, request):
        # 글 목록 조회
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/post_list.html', context)


class PostDetailView(View):
    def get(self, request, post_id):
        # 글 상세 조회
        post = get_object_or_404(Post, id=post_id)
        context = {
            'post': post
        }
        return render(request, 'blog/post_detail.html', context)


class PostUpdateView(View):
    def get(self, request, post_id):
        # 글 수정 폼 보여주기
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        context = {
            'post': post,
            'form': form
        }
        return render(request, 'blog/post_update.html', context)

    def post(self, request, post_id):
        # 글 수정 처리
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_id=post.id)
        else:
            context = {
                'post': post,
                'form': form
            }
            return render(request, 'blog/post_update.html', context)


class PostDeleteView(View):
    def get(self, request, post_id):
        # 글 삭제 확인 페이지 보여주기
        post = get_object_or_404(Post, id=post_id)
        context = {
            'post': post
        }
        return render(request, 'blog/post_delete.html', context)

    def post(self, request, post_id):
        # 글 삭제 처리
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect('blog:post_list')