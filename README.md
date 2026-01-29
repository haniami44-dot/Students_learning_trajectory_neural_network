# AURORZY
Gabriela Przybysz s218611
Hanna Milewska s223384

# Przegląd Projektu

Jest to aplikacja webowa oparta na Pythonie, zbudowana przy użyciu frameworka Django. Aplikacja wykorzystuje dwie sieci neuronowe (model podstawowy i zaawansowany) do przewidywania wyników studentów na podstawie danych dotyczących stylu życia i nauki studenta.

Frontend jet stylizowany za pomocą Bootstrapa.

**Aktulanie zaimplementowane funkcje:**

### **System predykcji z wykorzystaniem AI**
- Formularz umożliwiający wprowadzenie danych:
  - liczba godzin nauki (`study_hours`)
  - liczba godzin snu (`sleep_hours`)
  - poziom stresu (`stress_level`)
  - frekwencja (`attendance_rate`)
  - spożycie kofeiny (`caffeine_intake`)
- Predykcja wyniku studenta przez:
  - model podstawowy (prosta architektura sieci)
  - model zaawansowany (głębsza sieć z regularizacją i Batch Normalization)
- Wyświetlanie wyników obu modeli na stronie.

### **Porównanie modeli**
- Możliwość otwarcia raportu PDF porównującego modele (MAE, MSE, architektura sieci, krzywe uczenia).

### **System uwierzytelniania**
- Rejestracja użytkowników
- Logowanie i wylogowanie
- Obsługa superusera (panel admina Django)

---

# Budowanie i uruchamianie

## Wymagania

- Python 3.10  
- pip (menedżer pakietów Pythona)

---
## Instrukcje uruchomienia aplikacji

### UWAGA: Wszystkie poniższe instrukcje należy wykonywać w katalogu Application/ProjektPython (tam znajduje się plik manage.py).

## Instrukcje dla systemów Linux/macOS

### **1. Przejdź do katalogu projektu Django**

```bash
cd ProjektPythonowski
```

### **2. Utwórz i aktywuj wirtualne środowisko**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Zainstaluj zależności**

pip install -r requirements.txt

### **4. Uruchom aplikację**

python manage.py runserver

Aplikacja będzie dostępna pod adresem:
http://127.0.0.1:8000

## Instrukcje dla systemów Windows

### **1. Przejdź do katalogu projektu Django**

cd ProjektPythonowski

### **2. Utwórz i aktywuj wirtualne środowisko**

python -m venv venv
venv\Scripts\activate

### **3. Zainstaluj zależności**

pip install -r requirements.txt

### **4. Uruchom aplikację**

python manage.py runserver

Aplikacja będzie dostępna pod adresem:
http://127.0.0.1:8000