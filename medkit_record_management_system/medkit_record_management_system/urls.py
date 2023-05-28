"""medkit_record_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from medkit import views
app_name = 'medkit'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="homepage"),
    path("createpage", views.create, name="createpage"),
    path("loginpage", views.signin, name="loginpage"),
    path("addmedkits/", views.addMedkit, name="addmedkits"),
    path("displaydata/", views.display_data, name="displaydata"),
    path("<int:id>/", views.update_data, name="updatedata"),
    path("saledata/<int:id>/", views.salepage, name="saledata"),
    path("adddata/<int:id>/", views.addpage, name="adddata"),
    path("deletedata/<int:id>/", views.delete_data, name="deletedata"),
    path("logout/", views.logout_view, name="logout"),
    path("expirypage/", views.expiring_medkits, name="expirypage"),
]
