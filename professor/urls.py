from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('professor-dashboard/', views.professor_dashboard, name='professor_dashboard'),
    path('batch/<int:branch_id>/', views.batch, name='batch'),
    path('sem/<int:branch_id>/<int:batch_id>',views.sem,name='sem'),
    path('download/<int:branch_id>/<int:batch_id>/<int:sem>', views.download_report, name='download'),
     path('preview/<int:branch_id>/<int:batch_id>/<int:sem>', views.download_and_display, name='preview'),
     path('logout/',views.logout_view,name='professor_logout'),

]