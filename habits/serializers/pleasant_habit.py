from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import GoodHabit, PleasantHabit


class PleasantHabitSerializer(serializers.ModelSerializer):
    good_habit = SlugRelatedField(slug_field='pk', queryset=GoodHabit.objects.all())
    # validators = [UrlValidator(field="url")]

    class Meta:
        model = PleasantHabit
        fields = '__all__'
