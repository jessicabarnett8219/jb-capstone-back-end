from django.conf.urls import url
from django.urls import path

from . import views

app_name = "goalfish"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    path('students/', views.list_students, name='all_students'),
    path('add-student/', views.display_student_form, name='add_student_form'),
    path('student-added/', views.add_student, name='add_student'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('new-evaluation/<int:student_id>/', views.display_eval_form, name='new_eval'),
    path('eval-added/<int:student_id>/', views.add_evaluation, name='eval_added'),
    path('eval-detail/<int:eval_id>/', views.eval_detail, name='eval_detail'),
    path('grade-filter', views.grade_filter, name='grade_filter'),
    path('progress-landing/<int:student_id>/', views.progress_form, name='progress_form'),
    path('weekly-progress-results/<int:student_id>/', views.weekly_progress_results, name='weekly_progress_results'),
    path('range-progress-results/<int:student_id>/', views.range_progress_results, name='range_progress_results'),
    path('delete-eval/<int:eval_id>/', views.delete_eval, name='delete_eval'),
    path('edit-student-form/<int:student_id>/', views.edit_student_form, name='edit_student_form'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('student-search-results', views.student_search, name='student_search')
]
