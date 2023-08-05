from celery import shared_task

from habits.services.services import checking_habit


@shared_task
def checking_need_for_habit():
    checking_habit()
