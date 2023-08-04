from django.contrib import admin

from habits.models import PleasantHabit, GoodHabit


# Register your models here.

@admin.register(PleasantHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    list_display = (
    "title", "user", "place", "time", "action", "frequency", "execution_time", "is_public", "is_active",)


@admin.register(GoodHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "place", "time", "action", "frequency", "execution_time", "is_public", "is_active",
                    "connected_habit", "reward",)
