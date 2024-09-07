from django.db import models
import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    remark=models.CharField(default='',max_length=128)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
def rename_image(instance, filename):
    upload_to = 'pics/'
    ext = filename.split('.')[-1]
    # timestamp = datetime.now().strftime('%y%m%d%H%M%S')
    # randomstr=''.join(random.choices(string.ascii_letters, k=1))
    if instance.pk:
        filename = f"staff_{instance.pk}.{ext}"
    else:
        filename = f"photo.{ext}"
    return os.path.join(upload_to, filename)

class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    designation = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    posting_place = models.CharField(max_length=64)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=64)
    remark = models.CharField(max_length=150, blank=True)
    photo=models.ImageField(upload_to=rename_image, blank=True, null=True)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
@receiver(pre_save, sender=Employee)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_image = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False
    new_image = instance.photo
    if old_image and old_image != new_image and os.path.isfile(old_image.path):
        os.remove(old_image.path)

@receiver(post_delete, sender=Employee)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

