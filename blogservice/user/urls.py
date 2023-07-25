from django.urls import path
from .views import Registration, Login, Logout, ProfileUpdateView, VerifyEmailView, VerificationSentView

app_name = 'user'

urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    # 이메일인증
    path('verify-email/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verification-sent/', VerificationSentView.as_view(), name='verification_sent'),

]