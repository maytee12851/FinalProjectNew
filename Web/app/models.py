from calendar import Calendar, calendar
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT
from django.urls import reverse
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    tel = models.CharField(max_length=10)
    sex = models.CharField(max_length=100, choices=[('ชาย', 'ชาย'), ('หญิง', 'หญิง'), ('เพศทางเลือก', 'เพศทางเลือก')])
    photo = models.ImageField(upload_to="profilePic/", null=True, blank=True, default='profilePic/avatarPic_pekm5b.jpg')
    idcard = models.ImageField(upload_to="idCard/", null=True, blank=True, default='idCard/idcard_midixi.jpg')
    userType = models.CharField(max_length=100, choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')])
    approve = models.BooleanField('Approve', default=False)

    def __str__(self):
        return '%s %s' % (self.name,self.surname)

class ProfileEducationTutor(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True)
    school = models.CharField(max_length=100, blank=True)
    schoolProgram = models.CharField(max_length=100, blank=True)
    schoolYear = models.CharField(max_length=4, blank=True)
    university = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)
    universityYear = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return '%s' % (self.user)

class YourselfTutor(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True, null=True)
    video = models.FileField(upload_to='Video/', null=True, blank=True, default='#.mp4', storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    introduce = models.TextField()
    line = models.CharField(max_length=10, blank=True)
    facebook = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return '%s' % (self.user)

class Course(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True, null=True)
    introduceTutor = models.ForeignKey(YourselfTutor, on_delete=CASCADE, blank=True, null=True)
    education = models.ForeignKey(ProfileEducationTutor, on_delete=CASCADE, blank=True, null=True)
    language = models.CharField(max_length=100, choices=[('ภาษาอังกฤษ', 'ภาษาอังกฤษ'), ('ภาษาเกาหลี', 'ภาษาเกาหลี'), ('ภาษาจีน', 'ภาษาจีน'), ('ภาษาญี่ปุ่น', 'ภาษาญี่ปุ่น'), ('ภาษาเยอรมัน', 'ภาษาเยอรมัน')])
    courseTitle = models.CharField(max_length=100)
    courseDesc = models.TextField()
    courseHours = models.CharField(max_length=2, blank=True, null=True)
    courseDay = models.CharField(max_length=20, blank=True, null=True)
    courseTime = models.TimeField(max_length=30, blank=True, null=True)
    coursePrice = models.IntegerField(default=0, blank=True, null=True)
    courseRating = models.DecimalField(default=0, max_digits=5, decimal_places=1,null=True, blank=True)
    courseCount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.user)

class MyCourseStudent (models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=CASCADE)
    courseId = models.IntegerField(null=True)
    finish = models.BooleanField(default=False)
    star = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user)

class Rating (models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True, null=True)
    tutor = models.ForeignKey(Course, on_delete=CASCADE, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, default='1', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    MycourseId = models.ForeignKey(MyCourseStudent, on_delete=CASCADE, blank=True, null=True)
    star = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.user)

# calendar
class Event(models.Model):
    user = models.ForeignKey(Profile, on_delete=CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return '%s' % (self.user)

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'