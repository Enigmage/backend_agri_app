from django.db import models

class Data(models.Model):
    created_on = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=50, decimal_places=5, default="")
    season = models.CharField(max_length=50)
    crop_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state



