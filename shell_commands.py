from app.models import *
from django.db.models import Q, Subquery

# emp1 = Employee.objects.create(name='Iman', birth_date='2003-06-01', position='Backend dev',
#                                salary=100000, work_experience='2019-05-04')
# emp2 = Employee.objects.create(name='Akim', birth_date='2003-06-26', position='Frontend dev',
#                                salary=5000, work_experience='2015-08-12')
# emp3 = Employee.objects.create(name='Aiym', birth_date='2003-11-24', position='FullStack dev',
#                                salary=100000, work_experience='2020-01-03')
# emp4 = Employee.objects.create(name='Tima', birth_date='2003-12-11', position='PM',
#                                salary=5566, work_experience='2009-07-11')

#
# inn1 = Passport.objects.create(name=emp1, inn='1234567890123', id_card='1234567')
# inn2 = Passport.objects.create(name=emp2, inn='1234567890123', id_card='1234567')
# inn3 = Passport.objects.create(name=emp3, inn='1234567890123', id_card='1234567')
# inn4 = Passport.objects.create(name=emp4, inn='1234567890123', id_card='1234567')


# empl_delete1 = Employee.objects.all().order_by('-name')
# empl_delete1[0].delete()

# name1 = Employee.objects.all()[0]
# name2 = Employee.objects.all()[1]
# name3 = Employee.objects.all()[2]

# iman = Employee.objects.create(name='Iman', birth_date='2003-06-01', position='Backend dev',
#                                salary=990000, work_experience='2019-05-04')


# wp = WorkProject.objects.create(project_name='SomeProject')
# wp1 = WorkProject.objects.create(project_name='SomeSite')
# wp1.participants.set([iman, name2])

# wp_delete = Membership.objects.all()[2]
# wp_delete.delete()


# emp5 = Employee.objects.create(name='Artur', birth_date='2002-01-11', position='Security',
#                                salary=12345, work_experience='2010-11-05')

# wp_1 = WorkProject.objects.all()[0]
# wp_1.participants.set([emp5])


# client1 = Client.objects.create(name='Temir', birth_date='2001-02-14', address='Isanova')
# client2 = Client.objects.create(name='Bakyt', birth_date='1999-07-07', address='Moskovskaya')
# client3 = Client.objects.create(name='Chyngiz', birth_date='2012-05-09', address='Sovetskaya')
#
#
# vip_person = VIPClient.objects.create(name='Vasilii', birth_date='1999-10-14',
#                                       address='Isanova', phone_number='+996509335757', vip_status_start='2012-09-18',
#                                       donation_amount=20000)
# cli_delete = Client.objects.all()[0]
# cli_delete.delete()



print(f'Ёто все сотрудники-{Employee.objects.all()}')
employee_with_id = Passport.objects.filter(
    Q(id_card__contains='1') |
    Q(id_card__contains='2') |
    Q(id_card__contains='3') |
    Q(id_card__contains='4') |
    Q(id_card__contains='5') |
    Q(id_card__contains='6') |
    Q(id_card__contains='7') |
    Q(id_card__contains='8') |
    Q(id_card__contains='9') |
    Q(id_card__contains='0')
)
print(f'это все сотрудники с паспортом{employee_with_id}')
print(f'это все проекты{WorkProject.objects.all()}')
print(f"это проекты в которых участвую €{WorkProject.objects.filter(participants__name__startswith='I')}")
print(f'это все клиенты{Client.objects.all()}')
print(f'¬се вип клиенты-{VIPClient.objects.all()}')

# ѕроверка get_gender
employee_1 = Passport.objects.all()[2]
print(Passport.get_gender(employee_1))

# ѕроверка get_age

name = Employee.objects.all().first()
print(Employee.get_age(name))



