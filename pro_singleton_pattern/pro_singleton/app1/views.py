from django.shortcuts import render,redirect
from django.views import View

# Create your views here.

class EmployeeInfo(View):
    def get(self,request):
        
        template_name = 'app1/index.html'
        context={}
        return render(request,template_name,context)
    
    
