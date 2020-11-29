from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    firstName = models.CharField(max_length = 150)
    lastName = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.IntegerField()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return str(self.pk) + " " +self.firstName +" " + self.lastName

