from django.urls import path
from .views import UserView, SignupView, SignInView
from knox.views import LogoutView

urlpatterns = [
    path('user/', UserView.as_view(), name='user-info'),
    path('signup/', SignupView.as_view(), name='create-account'),
    path('login/', SignInView.as_view(), name='signIn'),
    path('logout/', LogoutView.as_view(), name='signout')
]
