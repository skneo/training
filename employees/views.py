from django.shortcuts import render,redirect
from .forms import EmployeeModelForm
from django.contrib import messages
from .models import Employee
from training.models import Trainee
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def all_employees(request):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    all_employee_list = Employee.objects.all().order_by('emp_no')
    total_emp_nos=len(all_employee_list)
    employees_per_page = 100
    paginator = Paginator(all_employee_list, employees_per_page)
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)
    context = {'employees': employees,'total_emp_nos':total_emp_nos}
    return render(request, 'employees/all_employees.html', context)
@login_required(login_url='/login')
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully")
            return redirect('/employees')
    else:
        form = EmployeeModelForm()
    return render(request, 'employees/add_employee.html', {'form': form})
@login_required(login_url='/login')
def view_employee(request):
    try:
        employee = Employee.objects.get(emp_no=int(request.GET['emp_no']))
        trainings=Trainee.objects.filter(employee__emp_no=request.GET['emp_no'])
        return render(request, 'employees/view_employee.html', {'employee':employee,'trainings':trainings})
    except Exception as e:
        print(e)
        messages.error(
            request, f"Error! No Employee found with employee no {request.GET['emp_no']}")
    return redirect('/employees')
@login_required(login_url='/login')
def edit_employee(request):
    employee = Employee.objects.get(emp_no=request.GET['emp_no'])
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, request.FILES, instance=employee)
        photo = request.FILES.get('photo')
        if photo and photo.size > 100 * 1024:  # 100KB
            messages.error(request,f"Error! Photo size should be less than 100 kb")
            return redirect('/employee/edit_employee/?emp_no='+str(employee.id))
        if form.is_valid():
            form.save()
            messages.success(request, "employee updated successfully")
            return redirect('/employees')
    else:
        form = EmployeeModelForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})