from django.urls import path
from .views import Registration, Login, Logout, ProfileUpdateView

app_name = 'user'

urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),

]