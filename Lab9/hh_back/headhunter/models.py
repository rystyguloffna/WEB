from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название')
    description = models.TextField(verbose_name='Description')
    city = models.CharField(max_length=200,verbose_name="City")
    address = models.TextField(verbose_name='Address')

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
    
    def __str__(self):
        return f"{self.name}"


class Vacancy(models.Model):
    company = models.ForeignKey(Company,related_name="vacancies",on_delete=models.CASCADE)
    name = models.CharField(max_length=200,verbose_name="Название")
    salary = models.FloatField(verbose_name="Salary")
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }