from django.contrib import admin
from backup.models import BackupRecord


@admin.register(BackupRecord)
class BackupRecordAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'content', 'size', 'storage_number', 'storage_location', 'responsible_person')

