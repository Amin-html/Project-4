from django.db import models
from django.contrib.auth.models import User
from games.models import Game

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.game.price * self.quantity

    def __str__(self):
        return f'{self.user} | {self.game} X {self.quantity}'
# Create your models here.
