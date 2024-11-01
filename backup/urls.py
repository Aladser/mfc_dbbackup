from django.urls import path

from backup.apps import BackupConfig
from backup.views import BackupRecordListView

app_name = BackupConfig.name

urlpatterns = [
    path('', BackupRecordListView.as_view(), name="list"),
]
