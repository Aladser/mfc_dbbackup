from django.views.generic import ListView

from backup.models import BackupRecord


# LIST
class BackupRecordListView(ListView):
    extra_context = {
        'header': 'Список записей',
    }

    model = BackupRecord
    template_name = "index.html"
