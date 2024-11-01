from django.core.management import BaseCommand

from authen.models import User, WorkPosition
from libs.seeding import Seeding

# должности
position_obj_list = [
    {'name': 'инженер-программист 1 категории'},
    {'name': 'ведущий программист'},
]

# пользователи
user_params_obj_list = [
    {
        'email': 'admin@test.ru',
        'first_name': 'Админ',
        'last_name': 'Админов',
        'patronym': 'Админович',
        'is_superuser': True,
        'is_staff': True
    },
    {
        'email': 'user1@test.ru',
        'first_name': 'Иванов',
        'last_name': 'Иван',
        'patronym': 'Иванович',
    },
    {
        'email': 'user2@test.ru',
        'first_name': 'Александров',
        'last_name': 'Александр',
        'patronym': 'Александрович',
    },
    {
        'email': 'user3@test.ru',
        'first_name': 'Сергеев',
        'last_name': 'Сергей',
        'patronym': 'Сергеевич',
    }
]
password = '_strongpassword_'


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # пользователи
        User.truncate()
        Seeding.seed_table(WorkPosition, position_obj_list)
        programmer = WorkPosition.objects.get(name="инженер-программист 1 категории")
        leading_programmer = WorkPosition.objects.get(name="ведущий программист")

        for i in range(1, len(user_params_obj_list)):
            user_params_obj_list[i]['worker_position'] = programmer
        user_params_obj_list[0]['worker_position'] = leading_programmer

        Seeding.seed_users(User, user_params_obj_list, password)
