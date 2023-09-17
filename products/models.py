from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("product title"))
    description = models.TextField(verbose_name=_("product description"))
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover/', blank=True)
    price = models.PositiveIntegerField(default=0, verbose_name=_("product price"))
    active = models.BooleanField(default=True, verbose_name=_("product status"))

    creation_datetime = models.DateTimeField(default=timezone.now, verbose_name=_("product  creation time"))
    modified_datetime = models.DateTimeField(auto_now=True, verbose_name=_("product  modified time"))

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(is_active=True)


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField(verbose_name=_('email'))
    text = models.TextField(verbose_name=_('comment text'))
    is_active = models.BooleanField(default=False)

    creation_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    active_comment_manage = ActiveCommentManager()
    def __str__(self):
        return f'{self.user} : {self.product}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
