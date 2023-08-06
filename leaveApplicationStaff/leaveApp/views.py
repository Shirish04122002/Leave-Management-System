from django.shortcuts import render,redirect
from .models import Staff, Employee_Manager, Employees
from django.contrib.auth import logout

# Create your views here.

def apply(request):
    if request.method == 'POST':
        employeeId = request.POST.get('employeeId')
        name = request.POST.get('name')
        leave_type = request.POST.get('leave')
        caddress = request.POST.get('caddress')
        approver = request.POST.get('approver')
        from_date = request.POST.get('from_date')
        till_date = request.POST.get('till_date')
        reason = request.POST.get('reason')
        approverId = request.POST.get('approverId')

        staff = Staff.objects.create(
            employeeId=employeeId,
            name=name,
            leave_type=leave_type,
            address=caddress,
            approver=approver,
            approverId=approverId,
            from_date= from_date,
            till_date=till_date,
            reason=reason
        )

        employee = Employees.objects.get(userid=staff.employeeId)
        employee_manager = Employee_Manager.objects.create(
            id=f"{employeeId}_{approverId}",
            managerId=approverId,
            employee=employee
        )
        return redirect('leaveApp:success', employeeId=employeeId)
    return render(request, 'leaveApp/apply.html')

def applystaff(request):
    if request.method == 'POST':
        employeeId = request.POST.get('employeeId')
        name = request.POST.get('name')
        leave_type = request.POST.get('leave')
        caddress = request.POST.get('caddress')
        approver = request.POST.get('approver')
        from_date = request.POST.get('from_date')
        till_date = request.POST.get('till_date')
        reason = request.POST.get('reason')
        approverId = request.POST.get('approverId')

        staff = Staff.objects.create(
            employeeId=employeeId,
            name=name,
            leave_type=leave_type,
            address=caddress,
            approver=approver,
            approverId=approverId,
            from_date= from_date,
            till_date=till_date,
            reason=reason
        )

        employee = Employees.objects.get(userid=staff.employeeId)
        employee_manager = Employee_Manager.objects.create(
            id=f"{employeeId}_{approverId}",
            managerId=approverId,
            employee=employee
        )
        return redirect('leaveApp:success', employeeId=employeeId)
    return render(request, 'leaveApp/applystaff.html')

def success(request, employeeId):
    staff_data = Staff.objects.filter(employeeId=employeeId)
    return render(request, 'leaveApp/success.html', context={'staff_data': staff_data})

def approve(request):
    if request.user.is_authenticated:
        managerId = request.user.username 
        print(managerId) 
        staff_data = Staff.objects.filter(approverId=managerId, leave_id='Pending')
        print(staff_data)
        return render(request, 'leaveApp/approve.html', context={'managerId': managerId, 'staff_data': staff_data})
    else:
        return redirect('login')  

def approve_action(request, employeeId):
    staff = Staff.objects.get(employeeId=employeeId)
    print(staff)
    if request.method == 'POST':
        action = request.POST.get('action')
        print(action)
        if action == 'approve':
            staff.leave_id = 'approved'
        elif action == 'reject':
            staff.leave_id = 'rejected'

        staff.save()

    return redirect('leaveApp:approve')
