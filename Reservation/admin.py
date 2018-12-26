from django.contrib import admin
from django.utils import timezone
import moment


class Import(admin.ModelAdmin):
    change_form_template =  'Reservations/templates/admin/change_form.html'

