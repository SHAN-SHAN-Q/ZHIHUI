"""
用户账户相关功能：注册、短信、登陆、注销
"""
from django.shortcuts import render,HttpResponse, redirect
from web.forms.account import RegisterModelForm, SendSmsForm, LoginSMSForm, LoginForm
from django.http import JsonResponse
from web import models
from web.models import Distinguish
    # ,Focustatistics
from utils.image_code import check_code
from io import BytesIO
from django.db.models import Q

# 登陆注册
def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})
    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        # 验证通过，写入数据库（密码要是密文）
        instance = form.save()

        return JsonResponse({'status': True, 'data': '/login/'})
    else:
        print(form.errors)

    return JsonResponse({'status': False, 'error': form.errors})


def send_sms(request):
    """ 发送短信 """
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号：不能为空、格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})


def login_sms(request):
    """ 短信登录 """
    if request.method == 'GET':
        form = LoginSMSForm()
        return render(request, 'login_sms.html', {'form': form})
    form = LoginSMSForm(request.POST)
    if form.is_valid():
        # 用户输入正确，登录成功
        mobile_phone = form.cleaned_data['mobile_phone']

        # 把用户名写入到session中
        user_object = models.UserInfo.objects.filter(mobile_phone=mobile_phone).first()
        request.session['user_id'] = user_object.id
        request.session.set_expiry(60 * 60 * 24 * 14)

        return JsonResponse({"status": True, 'data': "/index/"})

    return JsonResponse({"status": False, 'error': form.errors})


def login(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm(request)
        return render(request, 'login.html', {'form': form})
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        #  (手机=username and pwd=pwd) or (邮箱=username and pwd=pwd)

        user_object = models.UserInfo.objects.filter(Q(email=username) | Q(mobile_phone=username)).filter(
            password=password).first()
        if user_object:
            # 登录成功为止1
            request.session['user_id'] = user_object.id
            request.session.set_expiry(60 * 60 * 24 * 14)

            return redirect('index')

        form.add_error('username', '用户名或密码错误')

    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 生成图片验证码 """

    image_object, code = check_code()

    request.session['image_code'] = code
    request.session.set_expiry(60)  # 主动修改session的过期时间为60s

    stream = BytesIO()
    image_object.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.flush()
    return redirect('index')


# 界面一
def concentration(request):
    datas = Distinguish.objects.all()
    # focus = Focustatistics.objects.all()
    # environment = {"focus":focus}
    context = {
                    "datas": datas,
               }
    # , environment = environment

    return render(request, 'concentration.html', context=context)


def issues_chart(request):
    """ 在概览页面生成highcharts所需的数据 """

    data_list = models.Eachclass.objects.values()
    data_data = []
    for item in data_list:
         data_data.append(item['Focusvalue'])

    return JsonResponse({'status': True, 'data': data_data})


def issues_priority(request):
    data_list=[
         {
            "name": '睡觉',
            "y": 10
        }, {
            "name": '没睡觉',
            "y": 90
        }
    ]
    return JsonResponse({'status':True,'data':data_list})


def issues_barchart(request):
    data_list=[

        ['第一节', 24],
        ['第二节', 23],
        ['第三节', 21],
        ['第四节', 16],
        ['第五节', 16],
        ['第六节', 15],
        ['第七节', 14],

    ]
    return JsonResponse({'status': True, 'data': data_list})


# 界面二
def administration0(request):
    num = "0"
    context = {"num": num}
    return render(request,'administration.html',context=context)


def administration1(request):
    num="1"
    context = {"num": num}
    return render(request,'administration.html',context=context)


def administration2(request):
    num="2"
    context = {"num": num}
    return render(request,'administration.html',context=context)

