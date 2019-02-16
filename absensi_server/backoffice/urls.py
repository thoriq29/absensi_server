from django.urls import path, include
from . import views


app_name = 'backoffice'

urlpatterns = [
    path('', include('absensi_server.backoffice.students.urls', namespace='index')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('students/', include('absensi_server.backoffice.students.urls', namespace='students')),
]