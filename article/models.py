from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):

	author = models.ForeignKey('auth.User', on_delete = models.CASCADE, verbose_name = 'Yazar')
	title = models.CharField(max_length = 50, verbose_name = 'Başlık')
	content = RichTextField(verbose_name = 'İçerik')
	date = models.DateTimeField(auto_now_add = True, verbose_name = 'Oluşturulma Tarihi')