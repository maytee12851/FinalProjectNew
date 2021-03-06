from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username','name','surname','nickname','sex','userType','approve','id']
    list_filter = ['userType','approve']

admin.site.register(Profile,ProfileAdmin)

class EducationTutor(admin.ModelAdmin):
    list_display = ['user','id']

admin.site.register(ProfileEducationTutor,EducationTutor)

class introduceYourselfTutor(admin.ModelAdmin):
    list_display = ['user','id']

admin.site.register(YourselfTutor,introduceYourselfTutor)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['user','language','courseTitle','courseRating','id']
    list_filter = ['user','language']

admin.site.register(Course,CourseAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['user','title']

admin.site.register(Event,EventAdmin)

class MyCourseStudentAdmin(admin.ModelAdmin):
    list_display = ['user','course','finish','star','id']

admin.site.register(MyCourseStudent,MyCourseStudentAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user','tutor','rating','star','id']

admin.site.register(Rating,RatingAdmin)