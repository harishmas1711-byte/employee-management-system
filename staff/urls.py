from django.urls import path
from . import views


urlpatterns = [

    path('', views.login_view, name='login'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('home/', views.home, name='home'),

    path('add/', views.add_employee, name='add_employee'),

    path(
        'employees/',
        views.employee_list,
        name='employee_list'
    ),

    path(
        'edit/<int:id>/',
        views.edit_employee,
        name='edit'
    ),

    path(
        'delete/<int:id>/',
        views.delete_employee,
        name='delete'
    ),
]