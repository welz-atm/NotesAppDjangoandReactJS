from django.urls import path
from usersapp.api.views import register_user, change_password, ObtainAuthTokenView, AllUsers
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'notesapp'

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('list/', AllUsers.as_view(), name='list'),
    path('change_password/', change_password, name='change_password'),
    path('login/', ObtainAuthTokenView.as_view(), name='token_view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)