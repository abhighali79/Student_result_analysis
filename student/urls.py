from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    # path('download/', views.download, name='download'),
    path('display_table/', views.display_table, name='display_table'),
    path('logout/',views.logout_view,name='student_logout'),
]
