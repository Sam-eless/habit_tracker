from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habits.models import GoodHabit, PleasantHabit
from users.models import User


class GoodHabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@sky.pro", is_staff=True, is_superuser=True)
        self.user.set_password("123131")
        self.user.save()

        response = self.client.post(
            "/users/api/token/",
            {"email": "admin@sky.pro", "password": "123131"},
            format="json"
        )
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.good_habit = GoodHabit.objects.create(title="Утренняя зарядка")
        self.pleasant_habit = PleasantHabit.objects.create(title="Посидеть в тишине")

    def test_good_habit_create(self):
        response = self.client.post(
            reverse("good_habit_create"),
            {
                "title": "Медитировать",
                "connected_habit": "Посидеть в тишине"
            },
            format="json"
        )
        self.assertEqual(self.good_habit.__str__(), "Утренняя зарядка")
        self.assertEqual(GoodHabit.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GoodHabit.objects.last().title, "Медитировать")
        self.assertEqual(GoodHabit.objects.first().title, "Утренняя зарядка")

    def test_good_habit_list(self):
        response = self.client.get(reverse("good_habit_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_good_habit_public_list(self):
        response = self.client.get(reverse("good_habit_public_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_connected_habit_and_reward_validator(self):
        response = self.client.post(
            reverse("good_habit_create"),
            {
                "title": "Медитировать",
                "connected_habit": "Посидеть в тишине",
                "reward": 'еда'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_execution_time_validator(self):
        response = self.client.post(
            reverse("good_habit_create"),
            {
                "title": "Медитировать",
                "connected_habit": "Посидеть в тишине",
                "execution_time": '00:06'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_frequency_validator(self):
        response = self.client.post(
            reverse("good_habit_create"),
            {
                "title": "Медитировать",
                "connected_habit": "Посидеть в тишине",
                "frequency": '8'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_good_habit_detail(self):
        response = self.client.get(reverse('good_habit_detail', kwargs={'pk': self.good_habit.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_good_habit_update_valid_data(self):
        valid_data = {
            "title": "Медитировать",
            "place": "дом2",
            "connected_habit": "Посидеть в тишине"

        }
        response = self.client.put(
            reverse('good_habit_update', kwargs={'pk': self.good_habit.id}),
            data=valid_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_good_habit_delete(self):
        response = self.client.delete(
            reverse('good_habit_delete', kwargs={'pk': self.good_habit.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PleasantHabitTestCase(APITestCase):

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

        self.pleasant_habit = PleasantHabit.objects.create(title="Посидеть в тишине")

    def test_pleasant_habit_create(self):
        response = self.client.post(
            reverse("pleasant_habit_create"),
            {
                "title": "Прочитать главу манхвы",
            },
            format="json"
        )
        self.assertEqual(self.pleasant_habit.__str__(), "Посидеть в тишине")
        self.assertEqual(PleasantHabit.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PleasantHabit.objects.last().title, "Прочитать главу манхвы")

    def test_pleasant_habit_list(self):
        response = self.client.get(reverse("pleasant_habit_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pleasant_habit_public_list(self):
        response = self.client.get(reverse("pleasant_habit_public_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_execution_time_validator(self):
        response = self.client.post(
            reverse("pleasant_habit_create"),
            {
                "title": "",
                "execution_time": '00:06'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_frequency_validator(self):
        response = self.client.post(
            reverse("pleasant_habit_create"),
            {
                "title": "Прочитать главу манхвы",
                "frequency": '8'
            },
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pleasant_habit_detail(self):
        response = self.client.get(reverse('pleasant_habit_detail', kwargs={'pk': self.pleasant_habit.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pleasant_habit_update_valid_data(self):
        valid_data = {
            "title": "Прочитать главу манхвы",
            "place": "кровать",
            "frequency": '1',
            "execution_time": '00:02'
        }
        response = self.client.put(
            reverse('pleasant_habit_update', kwargs={'pk': self.pleasant_habit.id}),
            data=valid_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pleasant_habit_delete(self):
        response = self.client.delete(
            reverse('pleasant_habit_delete', kwargs={'pk': self.pleasant_habit.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
