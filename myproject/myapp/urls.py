from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('doctor',views.doctor,name='doctor'),
    path('appoint',views.appoint,name='appoint'),
    path('final',views.final,name='final'),
    path('doc1',views.doc1,name="doc1"),
    path('blood',views.blood,name='blood'),
    path('Book',views.Book,name='Book'),
    path('final1',views.final1,name='final1'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('login1',views.login1,name='login1'),
    path('register1',views.register1,name='register1'),
    path('final2',views.final2,name='final2'),
    path('final3',views.final3,name='final3'),
    path('navbar',views.navbar,name='navbar'),

]