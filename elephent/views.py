from django.shortcuts import render

# Create your views here.

from django.views import View
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from elephent import models
import time
import hashlib
import json
import logging
from django.core import serializers
logger = logging.getLogger('elephent.views')

def md5(name):
    ctime = str(time.time())
    m = hashlib.md5(bytes(name,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()



class AuthView(APIView):

    def post(self,request,*args,**kwargs):
        result = {'code':'100','msg':'success'}

        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                result['code'] = 101
                result['msg'] = '用户名密码错误！'
            #create token
            token = md5(user)
            result['token'] = token
            print(token)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})

        except Exception as e:
            logger.error(e)
            result['code'] = 102
            result['msg'] = '请求异常！'
        return JsonResponse(result)



class OrderView(APIView):

    def get(self,request):
        try:
            orders = models.Order.objects.all()
            orders = serializers.serialize('json',orders,ensure_ascii=False)
            print(orders)
        except Exception as e:
            logger.error(e)
        ret = {'code': 200 }
        ret['data'] = orders

 #fffff
        #today is your day
        #return JsonResponse(orders,safe=False)
        return HttpResponse(orders)





