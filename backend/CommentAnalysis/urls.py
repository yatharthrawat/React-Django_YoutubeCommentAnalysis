from django.urls import path

from . import views

urlpatterns = [
    path('',views.CommentAnalysis.as_view()),
    path('<slug:video_id>/',views.Analysis.as_view()),
]
