from habits.models import PleasantHabit
from habits.serializers.pleasant_habit import PleasantHabitSerializer


class PleasantHabitDetailView(RetrieveAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]


class PleasantHabitListView(ListAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]
    # pagination_class = CustomPagination


class PleasantHabitCreateView(CreateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()

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


class PleasantHabitUpdateView(UpdateAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]

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


class PleasantHabitDeleteView(DestroyAPIView):
    serializer_class = PleasantHabitSerializer
    queryset = PleasantHabit.objects.all()
    # permission_classes = [IsAuthenticated, OwnerOrStuff]
