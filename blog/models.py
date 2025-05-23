from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.title