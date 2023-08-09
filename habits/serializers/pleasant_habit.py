from rest_framework import serializers

from habits.models import PleasantHabit
from habits.validators import ExecutionTimeValidator, FrequencyValidator


class PleasantHabitSerializer(serializers.ModelSerializer):
    validators = [ExecutionTimeValidator(field="execution_time"), FrequencyValidator(field="frequency")]

    class Meta:
        model = PleasantHabit
        fields = '__all__'
