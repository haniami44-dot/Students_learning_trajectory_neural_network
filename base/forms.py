from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class PredictionForm(forms.Form):
    study_hours = forms.FloatField(label="Liczba godzin nauki", validators=[MinValueValidator(0.0)])
    sleep_hours = forms.FloatField(label="Liczba godzin snu", validators=[MinValueValidator(0.0)])
    stress_level = forms.FloatField(label="Poziom stresu (0-10)", validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    attendance_rate = forms.FloatField(label="Frekwencja (0-1)", validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    caffeine_intake = forms.IntegerField(label="Spożycie kofeiny (w filiżankach)", validators=[MinValueValidator(0)])