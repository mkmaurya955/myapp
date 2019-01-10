"""myapp URL Configuration

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
from django.conf.urls import url,include
from reglogpage import views
# from reglogpage.views import HomeView,get_data,ChartData
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'registration/', views.registration,name='registration'),
    url(r'^$', views.login,name='home'),
    url(r'logout/',views.logout,name='logout'),
    # url(r'^charts/$',HomeView.as_view(),name='charts'),
    # url(r'^api/data/$',get_data,name='api-data'),
    # url(r'^api/chart/data/$',ChartData.as_view()),
    url(r'index/',views.index,name='index'),
    url(r'useraccount/',views.useraccount,name='useraccount'),
    url(r'report/',views.report,name='report'),
    url(r'calibration/',views.calibration,name='calibration'),
    url(r'user/',views.user,name='user'),
    url(r'submit/',views.submit,name='submit'),
]   