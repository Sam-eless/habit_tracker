from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    # validators = [UrlValidator(field="url")]

    class Meta:
        model = User
        fields = '__all__'
