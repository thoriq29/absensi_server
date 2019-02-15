from django.urls import path, include

urlpatterns = [
    path('students/', include('absensi_server.backoffices.students.urls'))
]