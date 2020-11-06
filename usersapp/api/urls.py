from django.urls import path
from usersapp.api.views import register_user, AllUsers, change_password, ObtainAuthTokenView, UpdateUser, ViewUser , \
    update_user
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'usersapp'

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('list/', AllUsers.as_view(), name='list'),
    path('update/<int:pk>/', UpdateUser.as_view(), name='update'),
    path('update_user/<int:pk>/', update_user, name='new_update'),
    path('view/<int:pk>/', ViewUser.as_view(), name='view'),
    path('change_password/', change_password, name='change_password'),
    path('login/', ObtainAuthTokenView.as_view(), name='token_view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)