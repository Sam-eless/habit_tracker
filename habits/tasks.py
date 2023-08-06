from celery import shared_task

from habits.services.services import checking_good_habit, checking_pleasant_habit


@shared_task
def checking_need_for_habit():
    checking_good_habit()
    checking_pleasant_habit()