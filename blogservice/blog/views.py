from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm

class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/create_post.html', context)

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
            return render(request, 'blog/create_post.html', context)
