from django.db import models

from authen.models import User


class BackupRecord(models.Model):
    created_at = models.DateField(verbose_name="Дата создания копии")
    content = models.CharField(max_length=255, verbose_name="Содержание копии")
    size = models.PositiveIntegerField(verbose_name="Размер резервной копии (Мб)")
    storage_number = models.CharField(max_length=255, verbose_name="Учетный номер носителя")
    storage_location = models.CharField(max_length=255, verbose_name="Место хранения носителя")
    responsible_person = models.ForeignKey(
        to=User,
        verbose_name="ФИО",
        on_delete=models.CASCADE,
        related_name='backup_records',
    )

    class Meta:
        verbose_name = 'Запись бэкапа'
        verbose_name_plural = 'Записи бэкапа'

    def __str__(self):
        return f"{self.created_at}, {self.content}, {self.size}, {self.responsible_person}"
