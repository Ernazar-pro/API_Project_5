from django.db import models

class StudyCenter(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Учебного Центра'
        verbose_name_plural = 'Учебные Центры'
    
class Teacher(models.Model):
    fullname = models.CharField(max_length=256)
    about = models.CharField(blank=True, null=True, max_length=256)
    experience = models.PositiveIntegerField(blank=True, null=True)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:
        verbose_name = 'Учителья'
        verbose_name_plural = 'Учители'

class Student(models.Model):
    fullname = models.CharField(max_length=256)
    about = models.CharField(blank=True, null=True, max_length=256)
    phone_number = models.CharField(max_length=256)
    study_center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:
        verbose_name = 'Студента'
        verbose_name_plural = 'Студенты'
        