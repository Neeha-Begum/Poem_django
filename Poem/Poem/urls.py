from django.urls import path
from Poem import views
urlpatterns=[
    path('<str:name1>/<str:name2>',views.func1)
]