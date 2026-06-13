from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    PLATFORM_CHOICES = [
        ('pc', 'PC'),
        ('ps5', 'PlayStation 5'),
        ('xbox', 'Xbox Series X')
    ]
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES, default='pc')
    release_year = models.IntegerField()
    image = models.ImageField(upload_to='games', blank=True, null=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.
