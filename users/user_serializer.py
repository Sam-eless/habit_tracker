from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    # validators = [UrlValidator(field="url")]

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "tg_login", "tg_chat_id"]
