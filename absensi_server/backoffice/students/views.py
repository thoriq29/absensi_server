"""
urutan import yang pythonic :
    1. Python standard library
    2. Django Library
    3. Third party libraries
    4. Project Library
harus sesuai alfabet
"""

from django.shortcuts import render

from absensi_server.apps.students.models import Students
from absensi_server.core.decorators import user_staff_required


@user_staff_required
def index(request):
    students = Students.objects.all()
    q = request.GET.get('q')
    if q:
        students = students.filter(name__istartswith=q)

    context_data = {
        'students': students,
        'q': q
    }
    return render(request, 'backoffice/students/index.html', context_data)