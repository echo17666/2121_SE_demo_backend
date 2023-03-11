from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import User   

@csrf_exempt    
def register(request):  
    if request.method == 'POST':  
        username = request.POST.get('username') 
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:   
            return JsonResponse({'errno': 250, 'msg': "两次输入的密码不同"})
        else:
            if User.objects.filter(username=username).exists():  
                return JsonResponse({'errno': 251, 'msg': "用户名已存在"})
            else:
                # 新建 Author 对象，赋值用户名和密码并保存
                new_author = User(username=username, password=password_1)
                new_author.save()   # 一定要save才能保存到数据库中
                return JsonResponse({'errno': 200, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 252, 'msg': "请求方式错误"})
