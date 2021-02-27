from django.urls import include, path
from app.views import name_med_2, login_user, do_logout, register, name_med_5, \
    name_med_6, name_med_8, name_med_9, name_med_10, name_med_11, name_med_12, \
    name_med_13, name_med_14

urlpatterns = [
    # path('main_page', name_med),
    path('', name_med_2),
    path('login', login_user),
    path('logout', do_logout),
    path('registration', register),
    path('registr', name_med_5),
    path('patient', name_med_6),
    path('patient_1', name_med_8),
    path('doctor', name_med_9),
    path('farm', name_med_10),
    path('doctor_1', name_med_11),
    path('farm_1', name_med_12),
    path('about_us', name_med_13),
    path('know', name_med_14),
    # path('', name_med_3),
    # path('inf', name_med_4),
]
