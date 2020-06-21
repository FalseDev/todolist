from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('' , views.index , name='index'),
    path('add/<str:name>/<str:text>/<str:color_code>/<str:prior_code>/' , views.add , name='add'),
    path('delete/<int:q_id>/', views.delete , name='delete'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('signup/' , views.signup , name='signup'),
    path('edit/<int:q_id>/<str:name>/<str:text>/<str:color_code>/<str:prior_code>/' ,
         views.edit ,
         name='edit'),
]
