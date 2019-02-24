from django.contrib import admin
from absensi_server.apps.students.models import Students


class StudentAdmin(admin.ModelAdmin):
    list_display = ('NIS', 'name')


admin.site.register(Students, StudentAdmin)