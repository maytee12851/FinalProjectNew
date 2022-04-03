from django import views
from django.urls import path,include
from .views import *
from . import views
from django.conf.urls import url

# app_name = 'app'
urlpatterns = [
    path('', index, name='index'),
    path('index-tutor/', indexTutor, name='index-tutor'),
    path('register-student/', registerStudent, name='register-student'),
    path('register-tutor/', registerTutor, name='register-tutor'),
    # path('login/', login, name='login'),
    path('tutor-form1/', tutorForm1, name='tutor-form1'),
    path('tutor-form2/', tutorForm2, name='tutor-form2'),
    path('tutor-form3/', tutorForm3, name='tutor-form3'),
    path('tutor-form4/', tutorForm4, name='tutor-form4'),
    path('tutor-form5/', tutorForm5, name='tutor-form5'),
    path('finding-tutor/', findingTutor, name='finding-tutor'),
    path('tutor-data/<int:id>', tutorData, name='tutor-data'),
    path('chat/', chat, name='chat'),
    path('study/', study, name='study'),
    path('teaching/', teaching, name='teaching'),
    path('profile-student/', profileStudent, name='profile-student'),
    path('profile/', profile, name='profile'),
    path('profile-tutor/', profileTutor, name='profile-tutor'),
    path('edit-profile/', editProfile, name='edit-profile'),
    path('edit-profile-tutor/', editProfileTutor, name='edit-profile-tutor'),
    path('profile-education-tutor/', profileEducationTutor, name='profile-education-tutor'),
    path('edit-profile-education-tutor/', editProfileEducationTutor, name='edit-profile-education-tutor'),
    path('yourself-tutor/', yourselfTutor, name='yourself-tutor'),
    path('edit-yourself-tutor/', editYourselfTutor, name='edit-yourself-tutor'),
    path('course-tutor/', courseTutor, name='course-tutor'),
    path('deleteCourse/<int:id>', deleteCourse, name='deleteCourse'),

    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('deleteEvent/<int:event_id>', deleteEvent, name='deleteEvent'),
]