from rest_framework import serializers

from habits.models import GoodHabit, PleasantHabit


class PleasantHabitSerializer(serializers.ModelSerializer):
    good_habit = SlugRelatedField(slug_field='title', queryset=GoodHabit.objects.all())
    # validators = [UrlValidator(field="url")]

    class Meta:
        model = PleasantHabit
        fields = '__all__'
