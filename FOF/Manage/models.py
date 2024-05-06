from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Season(models.Model):
    season_name = models.CharField(max_length=200)
    time_start = models.DateField()
    time_end = models.DateField()
    profit = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.season_name
    


class Land(models.Model):
    land_name = models.CharField(max_length=200)
    land_pos = models.CharField(max_length=1000)
    land_area = models.FloatField()
    land_pH = models.FloatField()
    land_doAm = models.DecimalField(max_digits=5, decimal_places=2)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.land_name


class Plant(models.Model):
    plant_name = models.CharField(max_length=200)
    plant_dev = models.DecimalField(max_digits=5, decimal_places=2, help_text="Thời gian phát triển (tháng)")

    # Use CharField with limited choices for older Django versions
    plant_type = models.CharField(max_length=1, choices=[
        ('0', 'Cây lương thực'),
        ('1', 'Cây ăn quả'),
        ('2', 'Cây rau củ'),
    ])
    plant_ND = models.CharField(max_length=200,help_text="Các khoáng chất cần thiết")
    plant_bp = models.IntegerField(help_text="Chu kỳ bón phân (ngày)")
    # Độ ẩm cây trồng cần
    # 
    land = models.ForeignKey(Land, on_delete=models.CASCADE)

    def __str__(self):
        return self.plant_name
    
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    birthday= models.CharField(max_length=50, null=True)
    type_user = models.CharField(max_length=50, null=True)
    phonenum = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.name if self.name else ''
#Hàm tự động thay đổi email ở User_authen sau khi nhập ở customer
@receiver(post_save, sender=Customer)
def update_user_email(sender, instance, created, **kwargs):
    if instance.user:
        if instance.email != instance.user.email:
            instance.user.email = instance.email
            instance.user.save()
        elif instance.email is None:
            instance.user.email = ""
            instance.user.save()


class Adress(models.Model):
    adress = models.CharField(max_length=50)
    def __str__(self):
        return self.adress

class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    price = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    def clean(self):
        super().clean()
        if self.name and not self.name.isupper():
            raise ValidationError("Tên sản phẩm phải viết hoa.")
    def __str__(self):
        return self.name
    
    
    @property
    def IMG_URL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    # Create your models here.


class market(models.Model): 
    marketName = models.CharField(max_length=200, null=False)
    marketPlant = models.CharField(max_length=200, null=False)
    marketUser = models.ForeignKey(User, on_delete=models.CASCADE)
    marketFee = models.CharField(max_length=200, null=False)
    marketDetail = models.CharField(max_length=1000, null=False)
    def clean(self):
        super().clean()
        if self.marketName and not self.marketName.isupper():
            raise ValidationError("Tên thị trường phải viết hoa.")
        if self.marketPlant and not self.marketPlant.isupper():
            raise ValidationError("Tên cây trồng phải viết hoa.")
    def __str__(self):
        return self.marketName


# class notifyCusjoin(models.Model):
     


class notify_market(models.Model):
    maker = models.ForeignKey(market, on_delete=models.CASCADE, related_name="maker")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    makerAuth = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="makerAuth")
    timejoin = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=0)
    link = models.CharField(max_length=250)
    



class Contact(models.Model):
    hoten = models.CharField(max_length=255)
    email = models.CharField(max_length=250)
    loinhan = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.hoten

