from django.shortcuts import render
from absensi_server.core.decorators import user_staff_required


@user_staff_required
def index(request):
    return render(request, 'backoffice/students/index.html')