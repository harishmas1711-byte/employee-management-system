from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee


def login_view(request):

    if request.user.is_authenticated:
        return redirect('employee_list')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('employee_list')

        else:

            return render(
                request,
                'login.html',
                {
                    'error': 'Invalid username or password'
                }
            )

    return render(request, 'login.html')


@login_required
def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def home(request):

    return render(request, 'home.html')


@login_required
def add_employee(request):

    if request.method == 'POST':

        name = request.POST['name']
        department = request.POST['department']
        salary = request.POST['salary']

        employee = Employee(
            name=name,
            department=department,
            salary=salary
        )

        employee.save()

        return redirect('employee_list')

    return render(request, 'add_employee.html')


@login_required
def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employee_list.html',
        {
            'employees': employees
        }
    )


@login_required
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        employee.name = request.POST['name']
        employee.department = request.POST['department']
        employee.salary = request.POST['salary']

        employee.save()

        return redirect('employee_list')

    return render(
        request,
        'edit_employee.html',
        {
            'employee': employee
        }
    )


@login_required
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('employee_list')