#encoding=utf-8
from django.shortcuts import render,HttpResponse
import json
# Create your views here.
import os
import logging
def index(request):
    lst = ['yuanbao','xiaotaozi']
    result = json.dumps(lst)
    return HttpResponse(result)
from core.config import settings
from django.views import View
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.decorators import method_decorator
#from django.conf import settings
logger = logging.getLogger('monkey.views')

#mybaseview 作为一个基类，在每个请求前后都做一些事情，
class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        #这个super不是简单的找自己的父类，也会去找self 继承体系中的类
        #super() 只能找到当前类的父类
        func = super(MyBaseView,self).dispatch(request, *args, **kwargs) #
        print('After')
        return func

class TeacherView(MyBaseView,View):

    def get(self,request,*args,**kwargs):
        return HttpResponse("Get")

    @method_decorator(csrf_exempt)
    def post(self,request,*args,**kwargs):
        return HttpResponse("post,this is my post")
    def put(self,request,*args,**kwargs):
        return HttpResponse("put")
    def delete(self,request,*args,**kwargs):
        return HttpResponse("delete")

#方法二：在类上面加上decorator
@method_decorator(csrf_exempt,name='dispatch')
class StudentsView(View):

    #类视图就是 通过调一个dispatch的方法去分发【post,put get....】等http请求
    #如果StudentView 重写了父类的这个方法，有请求过来直接使用本类的dispatch方法

    #操作过程是通过反射拿到 http请求的方式
    """
            if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed) 拿到了http请求的方式
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)  执行http请求的方法 对应的 post get ////

    """
    #不管你的请求方式是什么我直接返回一个httpresponse
    # def dispatch(self, request, *args, **kwargs):
    #     return HttpResponse("hello 我是 dispatcher!")

    #通过reflection 执行get方法
    # def dispatch(self, request, *args, **kwargs):# 这个self是指StudentView 这个类
    #     func = getattr(self,request.method.lower())# 获得get方法
    #     return func(request, *args, **kwargs)    #执行get方法

    #使用父类的dispatch方法，就是通过反射 相当于什么都没做，当时可以吧这个方法从源码中拿出来
    #可以加一下自己的操作
    #方法一： 直接在dispatch上面加上
    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print('before')
        func = super(StudentsView,self).dispatch(request, *args, **kwargs) #super的dispatch之后已经是执行了get方法
        print('After')
        return func


    def get(self,request,*args,**kwargs):
        return HttpResponse("Get")

    @method_decorator(csrf_exempt)
    def post(self,request,*args,**kwargs):
        return HttpResponse("post,this is my post")

    def put(self,request,*args,**kwargs):
        return HttpResponse("put")

    def delete(self,request,*args,**kwargs):
        return HttpResponse("delete")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
###################################################################3
"""
restful
"""


def global_settings(request):
    return {"herman":settings.Herman,
            #"SITE_DESC":settings.SITE_DESC,
            }


#pre restful
def get_order(request):
    logger.log(level=10,msg="today is your day!")
    logger.info("info logging")
    #logger.warning('warning')
    logger.warning("warning logger")
    logger.debug("debug  logger")
    logger.error("ffffffffffffffffffff")

    try:
        a = open('xxerere.txt','r')
    except Exception as e:
        logger.error(e)

    return HttpResponse("ddd")
def update_order():
    pass
def delete_order():
    pass
def post_order(request):

    return HttpResponse("hello world")

#restful with fbv
def order(request):
    if request.method == 'GET':
        return HttpResponse("获取订单")
    elif request.method == 'POST':
        return HttpResponse("新增订单")
    elif request.method == 'PUT':
        return HttpResponse("更新订单")
    elif request.method == 'DELETE':
        return HttpResponse("删除订单")

@method_decorator(csrf_exempt,name='dispatch')
class OrderView(View):
    def get(self,request,*args,**kwargs):
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name)
        herman = {'name':str(name),age:age}
        j1 = json.dumps(herman,ensure_ascii=False)
        print(j1)
        #print(settings.Herman)
        return HttpResponse(j1,status=201,content_type='application/json',charset='utf-8')
        #return HttpResponse("hello i am %s %s "%(name,age))

    def post(self,request,*args,**kwargs):
        print('i am ------------------------post ')
        name = request.POST.get('name')
        age = request.POST.get('baobei')
        with open(os.path.join(BASE_DIR,'static/yuan.txt'),'a') as f:
            f.write(name)
        print(name)
        return HttpResponse("hello i am %s %s "%(name,age))


    def put(self,request,*args,**kwargs):
        return HttpResponse("get order")
    def delete(self,request,*args,**kwargs):
        return HttpResponse("get order")
    def put(self,request,*args,**kwargs):
        return HttpResponse("get order")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@csrf_exempt
def pic(request):
    print("pic===================================")
    file = request.FILES.get('pic',None)
    f = open(os.path.join(BASE_DIR,'static'),'wb+')
    #for chunk in file.chunks():
    f.write(file)
    f.close()
#-----------------------------------------------------------------------------------
from rest_framework import exceptions
from rest_framework.views import APIView
"""
1.cbv 都是url找的View，view里面调用dispatch，dispatch分发到各个方法

2.

"""
class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed("authenticate failed 认证失败！")
        return ('alex',None)#这个是应该去数据库校验，放入登陆者的信息
    def authenticate_header(self,user):
        pass

from rest_framework.authentication import BaseAuthentication
class MonkeyView(APIView):
    """
    restframework 的授权
        def get_authenticators(self):
        Instantiates and returns the list of authenticators that this view can use.
        return [auth() for auth in self.authentication_classes]
    """

    #authentication_classes = [MyAuthentication,]


    def get(self,request,*args,**kwargs):
        name = request.GET.get('name')
        age = request.GET.get('age')
        print(name)
        herman = {'name':str(name),age:age}
        j1 = json.dumps(herman,ensure_ascii=False)
        print(j1)
        print(request.user)
        #print(settings.Herman)
        #return HttpResponse(j1,status=201,content_type='application/json',charset='utf-8')
        return HttpResponse("hello i am %s %s "%('康康','12'))

    def post(self,request,*args,**kwargs):
        print('i am ------------------------post ')
        with open(os.path.join(BASE_DIR,'static/yuan.txt'),'a') as f:
            f.write("aiyuanbo")
        return HttpResponse("hello i am %s %s "%('yuanbo','12'))

    def put(self,request,*args,**kwargs):
        return HttpResponse("get order")
    def delete(self,request,*args,**kwargs):
        return HttpResponse("get order")
    def put(self,request,*args,**kwargs):
        return HttpResponse("get order")


