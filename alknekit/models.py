from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe

class Category(models.Model):
    Category = models.CharField(max_length=50)
    Subcategory = models.CharField(max_length=50)

    def __str__(self):
        return self.Category + " " + self.Subcategory

class Products(models.Model):
    subcategory = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    newprice = models.FloatField(default=0)
    oldprice = models.FloatField(default=0)
    mainimage = models.ImageField(default=None, null=False,upload_to='static/images/products')
    main = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    Value = models.FloatField(default=None)
    def image_tag(self):
        if self.mainimage:
            return mark_safe('<img src="%s" style="width: 70px; height:100px;" />' % self.mainimage.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    def __str__(self):
        return self.tittle + " " + str(self.main)

