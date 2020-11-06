from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from usersapp.models import CustomUser
from rest_framework.authtoken.models import Token
from usersapp.api.serializer import UserSerializer, ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter


@csrf_exempt
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def register_user(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = user.email
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['display_name'] = user.display_name
            data['bio'] = user.bio
            data['pk'] = user.pk
            token = Token.objects.get(user=user).key
            data['token'] = token
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


def validate_email(email):
    user = None
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return None
    if user is not None:
        return email


class AllUsers(ListAPIView):
    queryset = CustomUser.objects.all().order_by('pk')
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser, ]
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, )
    search_fields = 'author__username'


class ViewUser(RetrieveAPIView):
    queryset = CustomUser.objects.all().order_by('pk')
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    authentication_classes = [BasicAuthentication]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UpdateUser(UpdateAPIView):
    queryset = CustomUser.objects.all().order_by('pk')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication]

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
@authentication_classes([BasicAuthentication])
def update_user(request):
    data = {}
    if request.method == 'PUT':
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['display_name'] = user.display_name
            data['email'] = user.email
            data['bio'] = user.bio
            data['response'] = 'Updated Successfully'
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated, ])
@authentication_classes([TokenAuthentication])
def change_password(request):
    try:
        user = CustomUser.objects.get(pk=request.user.pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.user == user:
        if request.method == 'PUT':
            serializer = ChangePasswordSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                if not request.user.check_password(serializer.data.get('old_password')):
                    data['response'] = 'Wrong Password.'
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
                new_password = serializer.data.get('new_password')
                confirm_password = serializer.data.get('confirm_password')
                if new_password == confirm_password:
                    password = user.set_password(serializer.data.get('new_password'))
                    password.save()
                    data['response'] = 'Successfully changed password'
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    data['response'] = 'Password must match.'
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = {}
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            data['response'] = 'Successfully authenticated.'
            data['pk'] = account.pk
            data['email'] = email.lower()
            data['token'] = token.key
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['response'] = 'Error'
            data['error_message'] = 'Invalid credentials'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)