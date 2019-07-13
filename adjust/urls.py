"""adjust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from adjust_api import views as api_views

urlpatterns = [
    path('', api_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('import_to_db/', api_views.import_csv),
    path('api/v1/records/', api_views.RecordViewSet.as_view(), name="records")

]

# /api/v1/tasks/?offset=0&status=O&limit=100&university=1&ordering=-created&created__lt=2015-09-22 17:39:01.184681&tag=sport
