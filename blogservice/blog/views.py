from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm, CommentForm, ImageForm
from .models import Post, Comment, Tag, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.db.models import Q


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        image_form = ImageForm()
        context = {"form": form, "image_form": image_form}
        return render(request, "blog/post_create.html", context)

    def post(self, request):
        form, image_form = self.get_forms(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            post = self.save_post(form, request.user)
            self.save_image(image_form, post)
            self.process_tags(form, post)
            return redirect("blog:post_detail", post_id=post.id)
        else:
            return render(request, "blog/post_create.html", {"form": form, "image_form": image_form})

    def get_forms(self, *args, **kwargs):
        form = PostForm(*args)
        image_form = ImageForm(*args, **kwargs)
        return form, image_form

    def save_post(self, form, user):
        post = form.save(commit=False)
        post.author = user
        post.save()
        return post

    def save_image(self, image_form, post):
        if image_form.cleaned_data.get("file_path"):
            image = image_form.save(commit=False)
            image.post = post
            image.save()

    def process_tags(self, form, post):
        tags = form.cleaned_data.get("tags")
        tag_names = [tag.strip() for tag in tags.split(",")]
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)


class PostListView(View):
    def get(self, request):
        # 글 목록 조회
        posts = Post.objects.all().order_by("-created_at")

        context = {"posts": posts}
        return render(request, "blog/post_list.html", context)


class PostDetailView(View):
    def get(self, request, post_id):
        # 글 상세 조회
        post = get_object_or_404(Post, id=post_id)
        self.increment_views(post)
        comment_form = CommentForm()
        context = {
            "post": post,
            "comment_form": comment_form,
        }
        return render(request, "blog/post_detail.html", context)

    def increment_views(self, post):
        post.views += 1
        post.save()


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        cleaned_tags = ", ".join(tag.name for tag in post.tags.all())
        form = PostForm(instance=post, initial={"tags": cleaned_tags})
        tags = post.tags.all()
        context = {"form": form, "post": post, "tags": tags}
        return render(request, "blog/post_update.html", context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            self.save_post(form, request.POST.get("tags"))
            return redirect("blog:post_detail", post_id=post_id)
        else:
            context = {"form": form, "post": post}
            return render(request, "blog/post_update.html", context)

    def save_post(self, form, tags):
        updated_post = form.save(commit=False)
        updated_post.save()
        self.update_tags(updated_post, tags)
        return updated_post

    def update_tags(self, post, tags_string):
        tag_names = [tag.strip() for tag in tags_string.split(",")]
        post.tags.clear()
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        context = {"post": post}
        return render(request, "blog/post_delete.html", context)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)
        post.delete()
        return redirect("blog:post_list")


class CreateCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            self.create_comment(request, post, form)
            return redirect("blog:post_detail", post_id=post.id)

    def create_comment(self, request, post, form):
        content = form.cleaned_data["content"]
        parent_comment_id = request.POST.get("parent_comment_id")

        comment_data = {
            "post": post,
            "author": request.user,
            "content": content,
        }

        if parent_comment_id:
            parent_comment = Comment.objects.get(id=parent_comment_id)
            comment_data["parent_comment"] = parent_comment

        Comment.objects.create(**comment_data)


class UpdateCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect("blog:post_detail", post_id=comment.post.id)


class DeleteCommentView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        post_id = comment.post.id
        comment.delete()
        return redirect("blog:post_detail", post_id=post_id)


@login_required(login_url="user:login")
@require_POST
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        # 이미 좋아요한 경우 좋아요 취소
        post.liked_by.remove(request.user)
    else:
        # 아직 좋아요하지 않은 경우 좋아요 추가
        post.liked_by.add(request.user)
    return redirect("blog:post_detail", post_id=post_id)


@login_required(login_url="user:login")
@require_POST
def like_comment(request, comment_id, post_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.liked_by.filter(id=request.user.id).exists():
        # 이미 좋아요한 경우 좋아요 취소
        comment.liked_by.remove(request.user)
    else:
        # 아직 좋아요하지 않은 경우 좋아요 추가
        comment.liked_by.add(request.user)

    return redirect("blog:post_detail", post_id)


class PostSearchView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            posts = Post.objects.filter(
                Q(title__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()
        else:
            posts = Post.objects.none()
        return posts.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context


class PostSearchByCategoryView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            return Post.objects.filter(category_id=category_id).order_by("-created_at")
        else:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get("category_id")
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            context["selected_category"] = category
        return context
