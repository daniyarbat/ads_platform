from rest_framework import serializers


# Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    # сериалайзер для модели
    pass


class AdDetailSerializer(serializers.ModelSerializer):
    # сериалайзер для модели
    pass
