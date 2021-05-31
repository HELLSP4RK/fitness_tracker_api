from django.db.models import Sum


def get_workout_totals(workouts):
    return workouts.values('type').annotate(calories=Sum('calories'), distance=Sum('distance'))
