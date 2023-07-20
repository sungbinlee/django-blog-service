from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password, password_validators_help_text_html
from django.core.exceptions import ValidationError



User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': '이메일'})
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': '이름'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호 확인'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용 중인 이메일 주소입니다.')
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            self.add_error('password1', error)

        return cleaned_data
    
    def add_password_validation_help_text(self):
        help_text = password_validators_help_text_html()
        self.fields['password1'].help_text = help_text



class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '이메일'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호'})


class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="새 비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호를 입력하세요'}),
        required=False,
        help_text=password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="새 비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 확인'}),
        required=False,
    )

    class Meta:
        model = User
        fields = ['name', 'profile_picture', 'introduction']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                validate_password(password1, self.instance)
            except ValidationError as error:
                self.add_error('password1', error)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "비밀번호가 일치하지 않습니다.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user