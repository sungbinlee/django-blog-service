from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '태그 입력 (쉼표로 구분)'}),
    )


    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            tags = [tag.strip() for tag in tags.split(',') if tag.strip()]
        return tags


    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

    class Meta:
        model = Comment
        fields = ['content']