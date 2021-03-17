from rest_framework import fields, serializers
from .models import Movie
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'movies']


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = ['nomi', 'janr', 'narxi', 'yili', 'davomiyligi', 'movie', 'batafsil', 'reyting', 'avtor', 'rasm', 'owner']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomi = validated_data.get('nomi', instance.nomi)
        instance.janr = validated_data.get('janr', instance.janr)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.yili = validated_data.get('yili', instance.yili)
        instance.davomiyligi = validated_data.get('davomiyligi', instance.davomiyligi)
        instance.movie = validated_data.get('movie', instance.movie)
        instance.batafsil = validated_data.get('batafsil', instance.batafsil)
        instance.reyting = validated_data.get('reyting', instance.reyting)
        instance.avtor = validated_data.get('avtor', instance.avtor)
        # instance.is_bestseller = validated_data.get('is_bestseller', instance.is_bestseller)
        instance.rasm = validated_data.get('rasm', instance.rasm)
        instance.save()
        return instance