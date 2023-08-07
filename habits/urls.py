from django.urls import path

from habits.views.good_habit import GoodHabitListView, GoodHabitDetailView, GoodHabitUpdateView, GoodHabitCreateView, \
    GoodHabitDeleteView, GoodHabitPublicListView
from habits.views.pleasant_habit import PleasantHabitDetailView, PleasantHabitListView, PleasantHabitUpdateView, \
    PleasantHabitCreateView, PleasantHabitDeleteView, PleasantHabitPublicListView

urlpatterns = [
    # PleasantHabit
    path('pleasant-habit/', PleasantHabitListView.as_view(), name="pleasant_habit_list"),
    path('pleasant-habit-public/', PleasantHabitPublicListView.as_view(), name="pleasant_habit_public_list"),
    path('pleasant-habit/<int:pk>/', PleasantHabitDetailView.as_view(), name="pleasant_habit_detail"),
    path('pleasant-habit/<int:pk>/update/', PleasantHabitUpdateView.as_view(), name="pleasant_habit_update"),
    path('pleasant-habit/create/', PleasantHabitCreateView.as_view(), name="pleasant_habit_create"),
    path('pleasant-habit/<int:pk>/delete/', PleasantHabitDeleteView.as_view(), name="pleasant_habit_delete"),

    # GoodHabit
    path('good-habit/', GoodHabitListView.as_view(), name="good_habit_list"),
    path('good-habit-public/', GoodHabitPublicListView.as_view(), name="good_habit_public_list"),
    path('good-habit/<int:pk>/',  GoodHabitDetailView.as_view(), name="good_habit_detail"),
    path('good-habit/<int:pk>/update/',  GoodHabitUpdateView.as_view(), name="good_habit_update"),
    path('good-habit/create/',  GoodHabitCreateView.as_view(), name="good_habit_create"),
    path('good-habit/<int:pk>/delete/',  GoodHabitDeleteView.as_view(), name="good_habit_delete"),
]
