from django.db import models
from django.contrib import admin
# Create your models here.
'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now'''
class Product(models.Model):
    id = models.AutoField(unique=True,primary_key=True,auto_created=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/images',null=True)
    desc = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.title