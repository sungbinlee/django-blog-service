from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm
from .models import Post, Comment, Tag
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView


class CreatePostView(LoginRequiredMixin, View):
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

            # 태그 처리
            tags = form.cleaned_data.get('tags')
            if tags:
                for tag_name in tags:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

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
        post.views += 1
        post.save()
        comment_form = CommentForm()
        context = {
            'post': post,
            'comment_form': comment_form,
        }
        return render(request, 'blog/post_detail.html', context)


class PostUpdateView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        cleaned_tags = ', '.join(tag.name for tag in post.tags.all())
        form = PostForm(instance=post, initial={'tags': cleaned_tags})
        tags = post.tags.all() 
        context = {
            'form': form,
            'post': post,
            'tags': tags
        }
        return render(request, 'blog/post_update.html', context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.save()

            # 태그 업데이트
            tags = request.POST.get('tags')  # 요청에서 태그 가져오기
            tag_names = [tag.strip() for tag in tags.split(',')]

            # 기존 태그 삭제 및 새로운 태그 추가
            new_post.tags.clear()
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                new_post.tags.add(tag)

            return redirect('blog:post_detail', post_id=post_id)
        else:
            context = {
                'form': form,
                'post': post
            }
            return render(request, 'blog/post_update.html', context)

class PostDeleteView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        context = {
            'post': post
        }
        return render(request, 'blog/post_delete.html', context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        post.delete()
        return redirect('blog:post_list')
    

class CreateCommentView(View):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            parent_comment_id = request.POST.get('parent_comment_id')  # 대댓글인 경우 부모 댓글의 ID를 가져옴
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                Comment.objects.create(
                    post=post,
                    parent_comment=parent_comment,  # 부모 댓글 설정
                    author=request.user,
                    content=content
                )
            else:
                Comment.objects.create(
                    post=post,
                    author=request.user,
                    content=content
                )
            return redirect('blog:post_detail', post_id=post.id)


class UpdateCommentView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('blog:post_detail', post_id=comment.post.id)


class DeleteCommentView(View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post_id = comment.post.id
        comment.delete()
        return redirect('blog:post_detail', post_id=post_id)
    

@login_required(login_url='user:login')
@require_POST
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        # 이미 좋아요한 경우 좋아요 취소
        post.liked_by.remove(request.user)
    else:
        # 아직 좋아요하지 않은 경우 좋아요 추가
        post.liked_by.add(request.user)
    return redirect('blog:post_detail', post_id=post_id)

@login_required(login_url='user:login')
@require_POST
def like_comment(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.liked_by.filter(id=request.user.id).exists():
        # 이미 좋아요한 경우 좋아요 취소
        comment.liked_by.remove(request.user)
    else:
        # 아직 좋아요하지 않은 경우 좋아요 추가
        comment.liked_by.add(request.user)
        
    return redirect('blog:post_detail', post_id)


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search_results.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(tags__name__icontains=query)
        return posts.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context