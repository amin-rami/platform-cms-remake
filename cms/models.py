from django.db import models



class ProtectionLevel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title


class TrendQuery(models.Model):
    id = models.AutoField(primary_key=True)
    protection_level = models.ForeignKey(to=ProtectionLevel, on_delete=models.PROTECT)
    query = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.query

