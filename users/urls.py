from django.urls import path
from users.views import PaymentsListAPIView, UserRetrieveAPIView, UserListAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users-detail'),
    path('users/', UserListAPIView.as_view(), name='users'),
    ]
