from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shanks/', views.shanks_view, name="shanks"),
    path('shanks/shanksInfo', views.shanks_info, name="shanksInfo"),
    path('luffy/', views.luffy_view, name="luffy"),
    path('luffy/luffyInfo', views.luffy_info, name="luffyInfo"),
    path('teach/', views.teach_view, name="teach"),
    path('teach/teachInfo', views.teach_info, name="teachInfo"),
    path('buggy/', views.buggy_view, name="buggy"),
    path('buggy/buggyInfo', views.buggy_info, name="buggyInfo")
]