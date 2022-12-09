from datetime import datetime

from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField()

    def get_age(self):
        return f'{self.name}-{datetime.today().year - self.birth_date.year}'

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=20)
    salary = models.IntegerField()
    work_experience = models.DateField()

    def __str__(self):
        return f'{self.name}-{self.salary}-{self.position}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.name} в должности {self.position} успешно сохранен!')


class Passport(models.Model):
    name = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='passports')
    inn = models.CharField(max_length=14)
    id_card = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.name.name} ID:{self.id_card}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        return print(f'{self.name} с паспортом {self.id_card} успешно сохранен!')

    def get_gender(self):
        if self.inn[0] == '1':
            return 'Женский пол'
        elif self.inn[0] == '2':
            return 'Мужской пол'
        else:
            'Ты не человек!'


class WorkProject(models.Model):
    participants = models.ManyToManyField(Employee, related_name='employees', through='Membership')
    project_name = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.participants} учасвтующие в {self.project_name} успешно сохранены!')


class Membership(models.Model):
    person = models.ForeignKey(Employee, on_delete=models.CASCADE)
    group = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.person}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.person} в проекте {self.group} успешно сохранен!')


class Client(AbstractPerson):
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'Клиент {self.name} успешно сохранен!')


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def __str__(self):
        return f'{self.name} имеет вип статус'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.name} с донатом в {self.donation_amount} успешно сохранен!')
