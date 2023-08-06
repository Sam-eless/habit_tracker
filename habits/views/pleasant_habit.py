from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import PleasantHabit
from habits.pagination import CustomPagination
from habits.permissions import OwnerOrStuff
from habits.serializers.pleasant_habit import PleasantHabitSerializer


class PleasantHabitDetailView(RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]


class PleasantHabitListView(ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]
    pagination_class = CustomPagination


class PleasantHabitPublicListView(ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class PleasantHabitCreateView(CreateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()

    permission_classes = [IsAuthenticated]


class PleasantHabitUpdateView(UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]


class PleasantHabitDeleteView(DestroyAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]
