from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import GoodHabit, PleasantHabit
from habits.validators import ExecutionTimeValidator


class PleasantHabitSerializer(serializers.ModelSerializer):
    validators = [ExecutionTimeValidator(field="execution_time")]

    class Meta:
        model = PleasantHabit
        fields = '__all__'
