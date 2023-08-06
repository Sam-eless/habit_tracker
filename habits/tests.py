from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import GoodHabit, PleasantHabit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro", is_staff=True, is_superuser=True)
        self.user.set_password("123131")
        self.user.save()

        response = self.client.post(
            "/users/api/token/",
            {"email": "admin@sky.pro", "password": "123131"},
            format="json"
        )
        print(self.user.is_authenticated)
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        print(self.user.is_authenticated)

        self.good_habit = GoodHabit.objects.create(title="Утренняя зарядка")
        self.pleasant_habit = PleasantHabit.objects.create(title="Посидеть в тишине")
        # self.valid_data = {
        #     'title': 'Update Lesson',
        #     'description': 'Update Description',
        #     'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        #     'owner': self.user.id,
        #     'course': self.course.title}

    def test_good_habit_create(self):
        response = self.client.post(
            reverse("good_habit_create"),
            {"title": "Пробежка по утрам", "connected_habit": "Посидеть в тишине"},
            format="json"
        )
        self.assertEqual(GoodHabit.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GoodHabit.objects.last().title, "Пробежка по утрам")
        self.assertEqual(GoodHabit.objects.first().title, "Утренняя зарядка")
