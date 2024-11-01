from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from authen.models import User
from backup.models import BackupRecord
from libs.seeding import Seeding


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if User.objects.all().count() == 0:
            print("Нет созданных пользователей")
            return

        workers_list = [
            User.objects.get(id=1),
            User.objects.get(id=2),
            User.objects.get(id=3),
            User.objects.get(id=4)
        ]
        worker_index = 0
        backup_records_obj_list = []
        created_at = timezone.now()

        for i in range(1, 5):
            record_obj = {
                "created_at": created_at,
                "content": "Содержание " + str(i),
                "size": i * 10,
                "storage_number": "NAC" + str(4),
                "storage_location": "Город " + str(i),
                "responsible_person": workers_list[worker_index]
            }
            worker_index = worker_index + 1 if worker_index != 3 else 0
            backup_records_obj_list.append(record_obj)
            created_at += timedelta(days=1)

        Seeding.seed_table(BackupRecord, backup_records_obj_list)
