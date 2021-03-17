from django.db import models
from django.contrib.auth.models import User


genre = (
    ('Jangari', 'Jangari'),
    ('Fantastik', 'Fantastik'),
    ('Tarixiy', 'Tarixiy'),
    ('Detektiv', 'Detektiv'),
    ('Kamediya', 'Kamediya'),
    ('Drama', 'Drama'),
    ('Multfilm', 'Multfilm')
)

class Movie(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='pics', default='pics/movie.jpg')
    janr = models.CharField(choices=genre, max_length=15, default='Kamediya')
    narxi = models.FloatField(default=0)
    yili = models.IntegerField(verbose_name='Ishlangan yili')
    davomiyligi = models.CharField(max_length=10)
    movie = models.FileField(upload_to='movie', verbose_name='Video fayli')
    batafsil = models.TextField(default='')
    reyting = models.FloatField(default=0)
    avtor = models.CharField(max_length=50, default='')
    upload_date = models.DateField(auto_now=True, verbose_name='Yuklangan sanasi')
    owner = models.ForeignKey(User, related_name='movies', on_delete=models.CASCADE)
    is_bestseller = models.BooleanField(verbose_name="Eng ko'p sotilgan kino", default=False)

    class Meta:
        verbose_name = 'Kino'
        verbose_name_plural = 'Kinolar'
    
    def __str__(self):
        return self.nomi