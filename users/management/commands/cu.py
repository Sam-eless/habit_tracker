from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='test1@sky.pro',
            first_name='test1',
            last_name='test1',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('123')
        user.save()

        user = User.objects.create(
            email='test2@sky.pro',
            first_name='test2',
            last_name='test2',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('123')
        user.save()

        user = User.objects.create(
            email='test3@sky.pro',
            first_name='test3',
            last_name='test3',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('123')
        user.save()
