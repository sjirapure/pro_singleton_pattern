from .models import Employee
def settings(request):
    return {'settings':Employee.load()}