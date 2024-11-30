from django.db import models

class ExcelData(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    pending_tasks = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.city} - {self.year}"
    
    