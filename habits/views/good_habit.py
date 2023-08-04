from rest_framework.generics import DestroyAPIView, UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import GoodHabit
from habits.permissions import OwnerOrStuff
from habits.serializers.good_habit import GoodHabitSerializer


class GoodHabitDetailView(RetrieveAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]


class GoodHabitListView(ListAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]
    # pagination_class = CustomPagination


class GoodHabitCreateView(CreateAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()

    # permission_classes = [IsAuthenticated, OwnerOrStuff]
    #
    # def create(self, request, *args, **kwargs):
    #     super().create(request, *args, **kwargs)
    #     lesson_title = self.request.data['title']
    #     lesson = get_object_or_404(Lesson, title=lesson_title)
    #     course = get_object_or_404(Course, id=lesson.course_id)
    #
    #     subscriptions = Subscription.objects.filter(course=course)
    #     if lesson.is_active and course.is_active:
    #         for subscription in subscriptions:
    #             email = subscription.user.email
    #             mailing_by_update_course.delay(email, lesson=lesson.title, course=course.title)
    #     return Response(request.data, status=status.HTTP_201_CREATED)


class GoodHabitUpdateView(UpdateAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrStuff]

    # def partial_update(self, request, *args, **kwargs):
    #
    #     lesson_id = self.kwargs['pk']
    #     lesson = get_object_or_404(Lesson, id=lesson_id)
    #     course = get_object_or_404(Course, id=lesson.course_id)
    #
    #     subscriptions = Subscription.objects.filter(course=course)
    #     if lesson.is_active and course.is_active:
    #         for subscription in subscriptions:
    #             email = subscription.user.email
    #             mailing_by_update_course.delay(email, lesson=lesson.title, course=course.title)
    #     return super().partial_update(request, *args, **kwargs)


class GoodHabitDeleteView(DestroyAPIView):
    serializer_class = GoodHabitSerializer
    queryset = GoodHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]
