from django.urls import path, include
from .views import SignUpView, EditProfileView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign-up/', SignUpView.as_view(), name='register'),
    path('profile/<int:pk>/', EditProfileView.as_view(), name='profile'),
]

