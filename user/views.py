from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import *   

@csrf_exempt    
def register(request):  
    if request.method == 'POST':  
        username = request.POST.get('username') 
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        if password_1 != password_2:   
            return JsonResponse({'errno': 250, 'msg': r"两次输入的密码不同"})
        if User.objects.filter(username=username).exists():  
            return JsonResponse({'errno': 251, 'msg': r"用户名已存在"})
        user = User.objects.create(username=username, password=password_1,email=email)
        user.save()
        return JsonResponse({'errno': 200, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 255, 'msg': r"请求方式错误"})
