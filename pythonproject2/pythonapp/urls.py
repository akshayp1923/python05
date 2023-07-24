from.import views
from django.urls import path



urlpatterns = [

    path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition')
    #path('contact/',views.contact,name='abc'),
    #path('details/',views.details,name='hello'),
    #path('thanks/',views.thanks,name='hai'),
]