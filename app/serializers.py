from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['data', 'title']


class PassageSerializer(WritableNestedModelSerializer):
    user = UserSerializer()
    level = LevelSerializer(allow_null=True)
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Passage
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect',
                  'user', 'coords', 'level', 'images']
