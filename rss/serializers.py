from django.contrib.auth.models import User, Group
from .models import Rss
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RssSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rss
        fields = ('nombre', 'url', 'categoria', 'fuente')