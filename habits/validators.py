from datetime import time

from rest_framework import serializers


class ConnectedHabitAndRewardValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("reward") is not None and value.get("connected_habit") is not None:
            raise serializers.ValidationError(
                "it is impossible to establish a reward and a pleasant habit at the same time")


class ExecutionTimeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get("execution_time") > time(00, 2, 00):
            raise serializers.ValidationError("Время выполнения не должно превышать 120 секунд")
