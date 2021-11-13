from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password_confrim = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confrim')

    def save(self, **kwargs):
        # print(self.validated_data)
        if self.validated_data.get('password') != self.validated_data.get('password_confrim'):
            raise serializers.ValidationError(
                {
                    'password': "Password doesn't match"
                }
            )
        user = User(
                email=self.validated_data.get('email'),
                username=self.validated_data.get('username')
                )
        
        
        user.set_password(self.validated_data.get('password'))
        user.save()
        return user