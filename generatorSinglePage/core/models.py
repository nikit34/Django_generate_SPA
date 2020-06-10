from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
import datetime


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    html_file = models.FileField(upload_to='pages/html/')
    cover = models.ImageField(upload_to='pages/cover/', null=True, blank=True)
    publish_date = models.DateTimeField(null=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
     
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.html_file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(datetime.datetime.now())
        return super(Page, self).save(*args, **kwargs)