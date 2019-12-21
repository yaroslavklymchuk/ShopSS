from django.db import models
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver


class Artist(models.Model):
	artits_name = models.CharField(max_length=101)
	artist_desc = models.TextField('About artits')

	def __str__(self):
		return self.artits_name

class PictureModel(models.Model):
	work_pic = models.FileField(upload_to='pic_folder/', blank=True)

class User(models.Model):
	user = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	ph_number = models.CharField(max_length=100)
	#emails = models.EmailField(max_length = 254)

class Good(models.Model):
	good_id = models.AutoField(primary_key=True)
	good_title = models.CharField('Product Name', unique=True, max_length = 200)
	good_description = models.TextField()
	good_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	#release_date = models.DateTimeField()
	good_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

	def __str__(self):
		return self.	good_title

class Cart(models.Model):
	id_basket = models.AutoField(primary_key=True) #id корзины - номер заказа
	c_user = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE)
	count = models.PositiveIntegerField(default=0)
	total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)

	@receiver(post_save) #sender=Entry
	def update_cart(sender, instance, **kwargs):
		line_cost = instance.quantity * instance.product.cost
		instance.cart.total += line_cost
		instance.cart.count += instance.quantity
		instance.cart.updated = datetime.now() 

