from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import GoodHabit
from habits.pagination import CustomPagination
from habits.permissions import OwnerOrStuff
from habits.serializers.good_habit import GoodHabitSerializer


class GoodHabitDetailView(RetrieveAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]


class GoodHabitListView(ListAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]
    pagination_class = CustomPagination


class GoodHabitPublicListView(ListAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class GoodHabitCreateView(CreateAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated]


class GoodHabitUpdateView(UpdateAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]


class GoodHabitDeleteView(DestroyAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]
