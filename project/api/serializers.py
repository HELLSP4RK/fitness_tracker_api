from rest_framework.exceptions import ValidationError
from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from api.models import Workout


class WorkoutCreateSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    def validate(self, attrs):
        if attrs['start'] < attrs['stop']:
            return attrs
        raise ValidationError('Время начала не может быть позднее времени окончания тренировки')

    class Meta:
        model = Workout
        fields = '__all__'
