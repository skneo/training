from django.shortcuts import render,redirect
from .forms import EmployeeModelForm
from django.contrib import messages
from .models import Employee

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

def edit_employee(request):
    employee = Employee.objects.get(id=request.GET['emp_id'])
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, request.FILES, instance=employee)
        photo = request.FILES.get('photo')
        if photo and photo.size > 100 * 1024:  # 100KB
            messages.error(request,f"Error! Photo size should be less than 100 kb")
            return redirect('/employee/edit_employee/?emp_id='+str(employee.id))
        if form.is_valid():
            form.save()
            messages.success(request, "employee updated successfully")
            return redirect('/employees')
    else:
        form = EmployeeModelForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})