from django.db import models
#makemigrations
#migrate
# Create your models here.
class airport(models.Model):
    city=models.CharField(max_length=50)
    code=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}"


class flight(models.Model):
    source=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrival")
    durations=models.IntegerField()

    def __str__(self):
        return f"({self.source} - {self.destination})"
       # return f"{self.source} - {self.destination}"


