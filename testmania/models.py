from django.db import models

class Student(models.Model):
    Elem_Category = (
        ('행당', '행당'),
        ('성수', '성수'),
    )
    elem = []
    for k in Elem_Category:
        elem.append(k[0])

    name = models.CharField(max_length=20)
    elementary = models.CharField(max_length=20, null=False, choices=Elem_Category)

    def __str__(self):
        return self.name

    def is_real_elementary(self):
        return self.elementary in self.elem
# Create your models here.
