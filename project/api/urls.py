from django.urls import path

from api.views import *

urlpatterns = [
    path('workout/create/', WorkoutCreateView.as_view(), name='create_workout'),

    # 'period' should be equal to 'hour' or 'day'
    path('statistics/<str:period>/', StatisticsView.as_view(), name='statistics'),
]
