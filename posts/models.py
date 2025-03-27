from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    # author
    title = models.CharField(verbose_name='Заголовк')
    content = models.TextField(verbose_name='Контент')
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
    edited = models.BooleanField(default=False, verbose_name='Редактирован ли?')

    class Meta: 
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def __str__(self):
        return f'{self.title}: {self.time_stamp}'
    
class PostAttachment(models.Model):
    name = models.CharField(verbose_name='Название картинки', blank=True, null=True)
    image = models.ImageField(upload_to='image', verbose_name='Картинка')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def save(self, *args, **kwags):
        self.name = self.image.name.split('.')[0].capitalize()
        super().save(*args, **kwags)
        
