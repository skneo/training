from django.db import models

class Training(models.Model):
    id = models.AutoField(primary_key=True)
    subject=models.CharField(max_length=128)
    start_date=models.DateField()
    days=models.IntegerField()
    remark=models.CharField(default='',max_length=128)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    employee=models.ForeignKey('employees.Employee',on_delete=models.CASCADE)
    training=models.ForeignKey('training.Training',on_delete=models.CASCADE)
    remark=models.CharField(max_length=128)