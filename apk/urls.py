from django.urls import path
from .views import *

urlpatterns = [

    path('',home,name ="home_link"),
    path('user_stock',stock,name ="stock_link"),
    path('user_view/<int:id>',view,name="view_link"),
    path('user_update/<int:id>',update,name ="update_link"),
    path('user_delete/<int:id>',user_delete,name ="delete_link")

    
]