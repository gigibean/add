from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from ..models import Users
from rest_framework import serializers


class Users(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'objects',
            'idx',
            'user_id',
            'pw',
            'nickname',
            'email',
            'profile',
            'salt',
            'follower_count',
            'following_count',
            'tracks_count',
            'grade',
            'status',
            'created_dt',
            'access_dt',
            'updated_dt',
            'refresh_token',
            # 'email',
        ]

class Friends(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
        'idx',
        'sender_idx',
        'receiver_idx',
        'created_dt'
        ]
