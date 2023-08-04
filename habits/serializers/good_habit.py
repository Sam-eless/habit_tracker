from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

# from rest_framework.relations import SlugRelatedField

from habits.models import GoodHabit, PleasantHabit


class GoodHabitSerializer(serializers.ModelSerializer):
    pleasant_habit = SlugRelatedField(slug_field='title', queryset=PleasantHabit.objects.all())
    # validators = [UrlValidator(field="url")]

    class Meta:
        model = GoodHabit
        fields = '__all__'
