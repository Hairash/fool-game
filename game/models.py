from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    class Status(models.TextChoices):
        OPENED = 'OP', 'opened'
        FINISHED = 'FI', 'finished'

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.OPENED,
    )
    players = models.ManyToManyField(User, null=True)

    @classmethod
    def get_game(cls):
        game = cls.objects.filter(status=cls.Status.OPENED).last()
        if not game:
            game = cls()
        return game
