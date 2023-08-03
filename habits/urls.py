from django.urls import path

from habits.views.pleasant_habit import PleasantHabitDetailView, PleasantHabitListView, PleasantHabitUpdateView, \
    PleasantHabitCreateView, PleasantHabitDeleteView

urlpatterns = [
    # PleasantHabit
    path('', PleasantHabitListView.as_view(), name="pleasant_habit_list"),
    path('<int:pk>/', PleasantHabitDetailView.as_view(), name="pleasant_habit_detail"),
    path('<int:pk>/update/', PleasantHabitUpdateView.as_view(), name="pleasant_habit_update"),
    path('create/', PleasantHabitCreateView.as_view(), name="pleasant_habit_create"),
    path('<int:pk>/delete/', PleasantHabitDeleteView.as_view(), name="pleasant_habit_delete"),


]




