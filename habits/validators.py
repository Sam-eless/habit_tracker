from datetime import time

from rest_framework import serializers


class ConnectedHabitAndRewardValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("reward") is None and value.get("connected_habit") is not None:
            return True
        if value.get("reward") is not None and value.get("connected_habit") is not None:
            raise serializers.ValidationError(
                "Невозможно установить награду и приятную привычку одновременно")


class ExecutionTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("execution_time") is not None:
            if value.get("execution_time") > time(00, 2, 00):
                raise serializers.ValidationError("Время выполнения не должно превышать 120 секунд")


class FrequencyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("frequency") is not None:
            if value.get("frequency") > 7:
                raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
