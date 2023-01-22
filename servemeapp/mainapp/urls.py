from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('diner/', views.diner, name="diner"),
    path('manager/', views.manager, name="manager"),
    path('diner/register/', views.dinerregister, name="dinerregister"),
    path('diner/login/', views.dinerlogin, name="dinerlogin"),
    path('diner/scan/', views.scan, name="dinerscan"),
    path('manager/register/', views.managerregister, name="managerregister"),
    path('manager/login/', views.managerlogin, name="managerlogin"),
    path('<managername>/profile/', views.managerprofile, name="managerprofile"),
    path('<managername>/profile/createfloor/', views.createfloor, name="createfloor"),
    path('<managername>/profile/layouts/', views.layouts, name="layouts"),
    path('<managername>/profile/menu/', views.menu, name="menu"),
    path('<managername>/profile/createmenu/', views.createmenu, name="createmenu"),
]