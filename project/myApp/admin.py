from django.contrib import admin
from .models import *

# Register your models here.

def ProfessorEvaluate(Professor):
    a = 0
    for professor in Professor:
        a += professor[2] * (professor[1] * professor[1] - professor[0] * professor[0])

    b = 0
    for professor in Professor:
        b += professor[2] * (professor[1] - professor[0])

    Q_ = a/(2 * b)

    a = 0
    for professor in Professor:
        a += (professor[1] - Q_) * (professor[1] - Q_) * (professor[1] - Q_) - (professor[0] - Q_) * (professor[0] - Q_) * (professor[0] - Q_)

    g = a/(3 * b)