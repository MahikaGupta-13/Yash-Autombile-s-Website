from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('',views.index, name="serviceBook"),
    path('messages', views.showMessage, name="Messageurl"),
    path('bookings', views.bookServices,name="bookSer"),
    path('table', views.displayTable, name="showTables"),
    path('display/<id>', views.details, name="showDetails"),
    path('discussion', views.question_list, name='dicussion'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('ask_auestion', views.post_question, name='ask_question'),
    path('post_answer/<int:question_id>', views.post_answer, name="post_answer"),
]