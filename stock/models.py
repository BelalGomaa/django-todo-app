from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=100, verbose_name="اسم القسم")

  def str(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=200, verbose_name="اسم المنتج")
  category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="القسم")
  price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
  quantity = models.IntegerField(default=0, verbose_name="الكمية المتاحة")
  min_stock_level = models.IntegerField(default=5, verbose_name="الحد الأدنى للتنبيه")

  def str(self):
    return self.name

class StockMovement(models.Model):
  MOVEMENT_CHOICES = (
    ('IN', 'إضافة للمخزن'),
    ('OUT', 'صرف من المخزن'),
 )
  product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
  movement_type = models.CharField(max_length=3, choices=MOVEMENT_CHOICES, verbose_name="نوع الحركة")
  quantity = models.PositiveIntegerField(verbose_name="الكمية")
  date = models.DateTimeField(auto_now_add=True, verbose_name="التاريخ")
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المسؤول")

  def str(self):
    return f"{self.product.name} - {self.get_movement_type_display()} - {self.quantity}"

  def save(self, *args, **kwargs):
    if not self.pk:
     if self.movement_type == 'IN':
        self.product.quantity += self.quantity
    elif self.movement_type == 'OUT':
         self.product.quantity -= self.quantity
    self.product.save()
    super().save(*args, **kwargs)