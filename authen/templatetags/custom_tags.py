import os

from django import template

from config.settings import APP_NAME, BASE_DIR

register = template.Library()


@register.filter()
def site_name_prefix(value):
    return f"{APP_NAME} - {value}" if value != '' else APP_NAME

@register.filter()
def custom_label(value, required_fields):
    if value in required_fields:
        return f"<label class='fw-bolder text-theme' title='обязательно для заполнения'>{value}:*</label>"
    else:
        return f"<label class='text-theme'>{value}:</label>"
