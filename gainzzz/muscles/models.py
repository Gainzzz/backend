from django.db import models


class Muscle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    muscle = models.ForeignKey(Muscle)

    def __str__(self):
        return self.name
