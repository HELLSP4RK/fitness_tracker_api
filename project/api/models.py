from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import *


class User(AbstractUser):
    email = EmailField(unique=True, verbose_name='Email')


class Workout(Model):

    class Type(TextChoices):
        RUN = 'run', 'Бег'
        WALKING = 'walking', 'Ходьба'
        BICYCLE = 'bicycle', 'Велосипед'

    user = ForeignKey(User, on_delete=CASCADE, related_name='workouts', verbose_name='Пользователь')
    type = CharField(max_length=15, choices=Type.choices, verbose_name='Вид спорта')
    distance = DecimalField(max_digits=4, decimal_places=1, verbose_name='Расстояние')
    calories = PositiveSmallIntegerField(verbose_name='Калории')
    start = DateTimeField(verbose_name='Время начала')
    stop = DateTimeField(verbose_name='Время окончания')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def save(self, *args, **kwargs):
        if self.start < self.stop:
            return super(Workout, self).save(*args, **kwargs)
        raise ValidationError('Время начала не может быть позднее времени окончания тренировки')

    def __str__(self):
        return f'{self.user} | {self.type} | {self.distance}'
