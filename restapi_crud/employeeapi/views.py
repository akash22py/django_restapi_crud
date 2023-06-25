import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import employee

# CREATE
@csrf_exempt
def create(request):
    if request.method == 'POST':
        try :
            data = json.loads(request.body)
            new_employee = employee.objects.create(emp_id = data.get('emp_id'), name = data.get('name'), department = data.get('department'))
            return JsonResponse({'emp_id': new_employee.emp_id, 'name': new_employee.name, 'department': new_employee.department}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
# READ ALL DATA
@csrf_exempt
def read_all(request):
    if request.method == 'GET':
        all_employee = employee.objects.all()
        data = [{'id' : employees.id, 'emp_id': employees.emp_id, 'name': employees.name, 'department': employees.department} for employees in all_employee]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

# READ
@csrf_exempt
def read(request, id):
    if request.method == 'GET':
        emp = employee.objects.filter(id=id).values('id','emp_id','name','department').first()
        if not emp:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        return JsonResponse(emp, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

# UPDATE
@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            update_emp = employee.objects.filter(id=id).first()
            if not update_emp:
                return JsonResponse({'error': 'Employee not found'}, status=404)
            update_emp.emp_id = data.get('emp_id', update_emp.emp_id)
            update_emp.name = data.get('name', update_emp.name)
            update_emp.department = data.get('department', update_emp.department)
            update_emp.save()
            return JsonResponse ({'emp_id': update_emp.emp_id, 'name': update_emp.name, 'department': update_emp.department})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


# DELETE
@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        emp_data = employee.objects.filter(id=id).first()
        if not emp_data:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        emp_data.delete()
        return JsonResponse({'message': 'Employee deleted successfully!'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)