from rest_framework import serializers
from usersapp.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    display_name = serializers.CharField()
    bio = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'display_name', 'bio', 'password', 'password2', ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self, **kwargs):
        user = CustomUser(email=self.validated_data['email'],
                          first_name=self.validated_data['first_name'],
                          last_name=self.validated_data['last_name'],
                          display_name=self.validated_data['display_name'],
                          bio=self.validated_data['bio'],)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'password': 'Passwords must match.'})


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)