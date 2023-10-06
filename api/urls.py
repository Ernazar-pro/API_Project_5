from django.urls import path, include
from .views import teacher, teacher_detail, student, student_detail, study_center, study_center_detail

urlpatterns = [
    path('teacher/', teacher),
    path('teacher/<int:pk>/', teacher_detail),
    path('student/', student),
    path('student/<int:pk>/', student_detail),
    path('study_center/', study_center),
    path('study_center/<int:pk>/', study_center_detail),
    path('auth/', include('dj_rest_auth.urls')),
]