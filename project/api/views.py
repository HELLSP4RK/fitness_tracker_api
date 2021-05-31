from datetime import timedelta
from django.utils import timezone

from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import WorkoutCreateSerializer
from api.services.get_annotate import get_workout_totals
from api.services.get_queryset import get_workouts_by_user_later_than_the_date


class WorkoutCreateView(CreateAPIView):
    serializer_class = WorkoutCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class StatisticsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, **kwargs):
        period = kwargs['period']
        date = timezone.now()
        if period == 'hour':
            date -= timedelta(hours=1)
        elif period == 'day':
            date -= timedelta(days=1)
        else:
            raise Http404
        workouts = get_workouts_by_user_later_than_the_date(username=request.user.username, date=date)
        totals = get_workout_totals(workouts)
        return Response(totals)
