
from django.urls import path
from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #https://stackoverflow.com/questions/55369645/how-to-customize-default-auth-login-form-in-django
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
]