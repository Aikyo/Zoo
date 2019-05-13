"""Zoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monkey import views
import elephent.views as vi

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r'index/', views.index),
    path(r'user/',views.StudentsView.as_view()),
    path(r'teacher/',views.TeacherView.as_view()),

    #fbv
    #pre restful
    path(r'get_order',views.get_order),
    path(r'update_order',views.update_order),
    path(r'post_order',views.post_order),
    path(r'delete_order',views.delete_order),

    #restful with fbv
    #path(r'order',views.order),
    # restful with fbv
    path(r'order', views.OrderView.as_view()),
    path(r'pic',views.pic),
    path(r'monkey',views.MonkeyView.as_view()),


    ##########################

    path(r'api/v1/auth',vi.AuthView.as_view()),
    path(r'api/v1/order',vi.OrderView.as_view()),


]


