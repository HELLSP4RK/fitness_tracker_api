from api.models import Workout


def get_workouts_by_user_later_than_the_date(username, date):
    return Workout.objects.filter(user__username=username, start__gte=date)
