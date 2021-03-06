from django.db import models


class Muscle(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle = models.ForeignKey(Muscle)
    image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Stretches(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle = models.ForeignKey(Muscle)
    image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Injuries(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    muscle = models.ForeignKey(Muscle)
    image = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
