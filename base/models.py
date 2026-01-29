from django.db import models

# Create your models here.

class Prediction(models.Model):
    study_hours = models.FloatField()
    sleep_hours = models.FloatField()
    stress_level = models.FloatField()
    attendance_rate = models.FloatField()
    caffeine_intake = models.IntegerField()

    def __str__(self):
        return f"Predykcja {self.id} ({self.study_hours}, {self.sleep_hours}, {self.stress_level}, {self.attendance_rate}, {self.caffeine_intake})"