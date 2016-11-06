from django.db import models
from django.template.defaultfilters import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=500)
    main_image = models.ImageField(upload_to='products')
    main_image_thumbnail = ImageSpecField(source='main_image',
                            processors=[ResizeToFill(250, 250)],
                            format='JPEG',
                            options={'quality': 60})

    def __str__(self):
        return self.name

class ProductPart(models.Model):
    product = models.ForeignKey(Product, related_name='parts')
    image = models.ImageField(upload_to='product/parts')
    technical_drawing = models.ImageField(upload_to='product/parts/technical_drawing')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description

