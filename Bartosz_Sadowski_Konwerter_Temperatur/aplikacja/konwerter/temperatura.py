# temperatura.py – Moduł do konwersji temperatur

def celsius_na_fahrenheit(c):
    """
    Zamienia temperaturę z Celsjusza na Fahrenheita.
    """
    return (c * 9/5) + 32

def fahrenheit_na_celsius(f):
    """
    Zamienia temperaturę z Fahrenheita na Celsjusza.
    """
    return (f - 32) * 5/9
