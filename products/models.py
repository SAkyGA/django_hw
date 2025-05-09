from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def rating(self):
        reviews = self.reviews.filter(is_active=True)
        total = sum(r.stars for r in reviews)
        count = reviews.count()
        return round(total / count, 1) if count else 0

    def __str__(self):
        return self.title


STARS = (
    (i, '*' * i) for i in range(1, 6)
)

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.product} - {self.text} '
    

# Create your models here.
