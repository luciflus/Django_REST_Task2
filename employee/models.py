from django.db import models

class Position(models.Model):
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.position}'

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, related_name='employees', on_delete=models.CASCADE)
    salary = models.FloatField()

    def __str__(self):
        return f'{self.fullname} - {self.position} - {self.salary}'

