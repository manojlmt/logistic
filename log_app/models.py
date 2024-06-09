from django.db import models

class Zone(models.Model):
    zone_name = models.CharField(max_length=10)

    def __str__(self):
        return self.zone_name

class City(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Rate(models.Model):
    from_zone = models.ForeignKey(Zone, related_name='rates_from', on_delete=models.CASCADE)
    to_zone = models.ForeignKey(Zone, related_name='rates_to', on_delete=models.CASCADE,null = True)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"Rate from {self.from_zone} to {self.to_zone}: {self.value}"