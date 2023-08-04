from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import GoodHabit, PleasantHabit
from habits.validators import ConnectedHabitAndRewardValidator, ExecutionTimeValidator, FrequencyValidator


class GoodHabitSerializer(serializers.ModelSerializer):
    connected_habit = SlugRelatedField(slug_field='title', queryset=PleasantHabit.objects.all())
    validators = [ConnectedHabitAndRewardValidator(field="connected_habit"),
                  ExecutionTimeValidator(field="execution_time"), FrequencyValidator(field="frequency")]

    class Meta:
        model = GoodHabit
        fields = '__all__'
