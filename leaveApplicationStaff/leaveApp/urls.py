from django.urls import path
from . import views

app_name = 'leaveApp'

urlpatterns=[
    path('',views.apply,name='apply'),
    path('success/<str:employeeId>/', views.success, name='success'),
    path('approve_action/<str:employeeId>/', views.approve_action, name='approve_action'),
    path('approve/',views.approve,name='approve')
]