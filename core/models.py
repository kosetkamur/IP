from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from time import time

from simple_history.models import HistoricalRecords


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    time_to_cook = models.SmallIntegerField(default=0, db_index=True, verbose_name='Время приготовления')
    # image = models.ImageField(null=True,blank=True,  verbose_name='Изображение', max_length=200)
    count = models.SmallIntegerField(default=0, db_index=True, verbose_name='Количество порций')
    body = models.TextField(blank=True, db_index=True, verbose_name='Описание рецепта')
    slug = models.SlugField(max_length=150, blank=True, unique=True, verbose_name="URL")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    dish = models.ForeignKey('ViewDish', on_delete=models.PROTECT, null=True, verbose_name='Вид блюда')
    history = HistoricalRecords()

    def get_detail_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.cat_id})

    def get_cards_url(self):
        return reverse('viewDish', kwargs={'dish_id': self.dish_id})



class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})



class ViewDish(models.Model):
    viewDish = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.viewDish

    def get_absolute_url(self):
        return reverse('viewDish', kwargs={'dish_id': self.pk})


class People(models.Model):
    human = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    age = models.SmallIntegerField(default=0, db_index=True, verbose_name='Возраст', null=True)
    сity = models.CharField(max_length=100, db_index=True, verbose_name='Город', null=True)
    status = models.CharField(max_length=100, db_index=True, verbose_name='Статус', null=True)

    def __str__(self):
        return self.human

    def get_absolute_url(self):
        return reverse('human', kwargs={'human': self.human})


class Commentaries(models.Model):
    author = models.ForeignKey('People', on_delete=models.PROTECT, null=True, verbose_name='Комментаторы')
    comment = models.CharField(max_length=100, db_index=True, verbose_name='Город')
    tag_author = models.ForeignKey('Tags', on_delete=models.PROTECT, null=True, verbose_name='Теги')

    def get_people_url(self):
        return reverse('author', kwargs={'human': self.human})

    def get_tag_url(self):
        return reverse('tag_author', kwargs={'tag_id': self.tag_id})

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_id': self.pk})


class Tags(models.Model):
    tag = models.CharField(max_length=250, db_index=True, verbose_name='Тэги')

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_id': self.pk})