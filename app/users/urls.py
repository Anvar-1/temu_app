from django.urls import path
from .views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailView, CartCreateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('cart/add/', CartCreateView.as_view(), name='cart-create'),
]