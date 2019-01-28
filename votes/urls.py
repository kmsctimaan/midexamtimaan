from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    #path('help/', views.help, name='help'),
    path('<int:votes_id>/', views.candidate_detail, name ='detail'),
    path('candidate_create/', views.candidate_create, name='candidate_create'),
    path('<int:votes_id>/update', views.candidate_update, name = 'update'),
    path('create/', views.position_create, name='create'),
    # path('vote/', views.vote, name='vite'),
    # path('comment/', views.comment, name='comment'),
]
