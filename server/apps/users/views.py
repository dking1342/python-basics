from django.http.response import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from django.shortcuts import render
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','email','password','is_student')
        extra_kwargs = {'password':{'write_only':True,'min_length':8}}

    def create(self,validated_data):
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user  

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = UserProfile
        fields = ('__all__')

# @permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     raise PermissionDenied()