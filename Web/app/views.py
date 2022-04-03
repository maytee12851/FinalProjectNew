from multiprocessing import context
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# calendar
import calendar
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
from .utils import Calendar
from .forms import EventForm
from django.urls import reverse

def index(request):
    return render(request, 'app/index.html')

def indexTutor(request):
    return render(request, 'app/index-tutor.html')

def registerStudent(request):

    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=username):
            messages.warning(request, 'Username นี้ถูกใช้ไปแล้ว')
            return redirect('/register-student/')
        else:
            newUser = User()
            newUser.username = username
            newUser.email = email
            newUser.set_password(password)
            newUser.save()

            profile = Profile()
            profile.user = User.objects.get(username=username)
            profile.username = username
            profile.email = email
            profile.userType = 'student'
            profile.save()
            return redirect('login') 
                              
        user = authenticate(username=username, password=password)
        login(request, user)

    return render(request, 'app/register-student.html')

def registerTutor(request):

    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(username=username):
            messages.warning(request, 'Username นี้ถูกใช้ไปแล้ว')
            return redirect('/register-tutor/')
        else:
            newUser = User()
            newUser.username = username
            newUser.email = email
            newUser.set_password(password)
            newUser.save()

            profile = Profile()
            profile.user = User.objects.get(username=username)
            profile.username = username
            profile.email = email
            profile.userType = 'teacher'
            profile.save()

            EducationTutor = ProfileEducationTutor()
            EducationTutor.user = Profile.objects.get(username=username)
            EducationTutor.save()

            yourself = YourselfTutor()
            yourself.user = Profile.objects.get(username=username)
            yourself.save()
            return redirect('login')
                      
        user = authenticate(username=username, password=password)
        login(request, user)
     
    return render(request, 'app/register-tutor.html')

def tutorForm1(request):
    return render(request, 'app/tutor-form1.html')

def tutorForm2(request):
    return render(request, 'app/tutor-form2.html')

def tutorForm3(request):
    return render(request, 'app/tutor-form3.html')

def tutorForm4(request):
    return render(request, 'app/tutor-form4.html')

def tutorForm5(request):
    return render(request, 'app/tutor-form5.html')

def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required
def findingTutor(request):

    course = Course.objects.all()
    language = request.GET.get('language')

    if is_valid_queryparam(language):
        course = course.filter(language=language)
    
    context = {'course' : course}
    
    if request.user.profile.userType == 'student':
    
        if request.user.profile.email == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile/')

        if request.user.profile.name == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile/')

        if request.user.profile.surname == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile/')

        if request.user.profile.nickname == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            
        
        if request.user.profile.tel == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile/')

        if request.user.profile.sex == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile/')

    if request.user.profile.userType == 'teacher':
    
        if request.user.profile.email == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')

        if request.user.profile.name == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')

        if request.user.profile.surname == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')

        if request.user.profile.nickname == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')
        
        if request.user.profile.tel == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')

        if request.user.profile.sex == '':
            messages.warning(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return redirect('/edit-profile-tutor/')

    return render(request, 'app/finding-tutor.html', context)

def tutorData(request, id):

    course = Course.objects.filter(id=id)
   
    context = {'course' : course}

    return render(request, 'app/tutor-data.html', context)

def chat(request):
    return render(request, 'app/chat.html')

def study(request):
    return render(request, 'app/study.html')

def teaching(request):
    return render(request, 'app/teaching.html')

def profileStudent(request):
    return render(request, 'app/profile-student.html')

def profile(request):
    return render(request, 'app/profile.html')

def profileTutor(request):
    return render(request, 'app/profile-tutor.html')

def editProfile(request):

    username = request.user.username
    user = User.objects.get(username=username)

    if request.method == 'POST':
        data = request.POST.copy()  
        name = data.get('name')
        surname = data.get('surname')
        nickname = data.get('nickname')
        tel = data.get('tel')
        email = data.get('email')
        sex = data.get('sex')

        editUser = User.objects.get(username = user)
        editUser.email = email
        editUser.save()

        profile = Profile()
        newProfile = Profile.objects.get(user=user)
        newProfile.email = email
        newProfile.name = name
        newProfile.surname = surname
        newProfile.nickname = nickname
        newProfile.tel = tel
        newProfile.sex = sex
        newProfile.save()

        if "photo" in request.FILES:
            new_photo = request.FILES["photo"]
            newProfile.photo = new_photo
            newProfile.save()

        return redirect('/profile/')

    profile = Profile.objects.filter(user=user)

    context = {'profile' : profile}

    return render(request, 'app/edit-profile.html',context)

def editProfileTutor(request):

    username = request.user.username
    user = User.objects.get(username=username)

    if request.method == 'POST':
        data = request.POST.copy()  
        name = data.get('name')
        surname = data.get('surname')
        nickname = data.get('nickname')
        tel = data.get('tel')
        email = data.get('email')
        sex = data.get('sex')

        editUser = User.objects.get(username = user)
        editUser.email = email
        editUser.save()

        profile = Profile()
        newProfile = Profile.objects.get(user=user)
        newProfile.email = email
        newProfile.name = name
        newProfile.surname = surname
        newProfile.nickname = nickname
        newProfile.tel = tel
        newProfile.sex = sex
        newProfile.save()

        if "photo" in request.FILES:
            new_photo = request.FILES["photo"]
            newProfile.photo = new_photo
            newProfile.save()

        if "idcard" in request.FILES:
            new_idcard = request.FILES["idcard"]
            newProfile.idcard = new_idcard
            newProfile.save()

        return redirect('/profile-tutor/')

    profile = Profile.objects.filter(user=user)

    context = {'profile' : profile}

    return render(request, 'app/edit-profile-tutor.html',context)

def profileEducationTutor(request):

    username = request.user.profile.username
    user = Profile.objects.get(username=username)
    Education = ProfileEducationTutor.objects.filter(user=user)

    context = {'Education' : Education}

    return render(request, 'app/profile-education-tutor.html', context)

def editProfileEducationTutor(request):

    username = request.user.username
    user = Profile.objects.get(username=username) # get (username ที่มีอยู่ในโมเดล profile ในวงเล็บซ้าย = ชื่อที่จะตั้ง)

    if request.method == 'POST':
        data = request.POST.copy()
        school = data.get('school')
        schoolProgram = data.get('schoolProgram')
        schoolYear = data.get('schoolYear')
        university = data.get('university')
        degree = data.get('degree')
        faculty = data.get('faculty')
        major = data.get('major')
        universityYear = data.get('universityYear')

        Education = ProfileEducationTutor()
        newEducation = ProfileEducationTutor.objects.get(user=user)
        newEducation.user = user
        newEducation.school = school
        newEducation.schoolProgram = schoolProgram
        newEducation.schoolYear = schoolYear
        newEducation.university = university
        newEducation.degree = degree
        newEducation.faculty = faculty
        newEducation.major = major
        newEducation.universityYear = universityYear
        newEducation.save()

        return redirect('/profile-education-tutor/')

    Education = ProfileEducationTutor.objects.filter(user=user)

    context = {'Education' : Education}

    return render(request, 'app/edit-profile-education-tutor.html', context)

def yourselfTutor(request):

    username = request.user.profile.username
    user = Profile.objects.get(username=username)
    yourself = YourselfTutor.objects.filter(user=user)

    context = {'yourself' : yourself}

    return render(request, 'app/yourself-tutor.html', context)

def editYourselfTutor(request):

    username = request.user.username
    user = Profile.objects.get(username=username)

    if request.method == 'POST':
        data = request.POST.copy()
        introduce = data.get('introduce')

        yourself = YourselfTutor()
        newYourself = YourselfTutor.objects.get(user=user)
        newYourself.user = user
        newYourself.introduce = introduce
        newYourself.save()

        if request.FILES['video'] if 'video' in request.FILES else None:
            new_video = request.FILES["video"]
            newYourself.video = new_video
            newYourself.save()

        return redirect('/yourself-tutor/')

    yourself = YourselfTutor.objects.filter(user=user)

    context = {'yourself' : yourself}
    
    return render(request, 'app/edit-yourself-tutor.html', context)

def courseTutor(request):
   
    username = request.user.username
    user = Profile.objects.get(username=username)
    introduceTutor = YourselfTutor.objects.get(user=user)
    education = ProfileEducationTutor.objects.get(user=user)

    if request.method == 'POST':
        data = request.POST.copy()
        language = data.get('language')
        courseTitle = data.get('courseTitle')
        courseDesc = data.get('courseDesc')
        courseHours = data.get('courseHours')
        courseDay = data.get('courseDay')
        courseTime = data.get('courseTime')
        coursePrice = data.get('coursePrice')

        addCourse = Course()
        addCourse.user = user
        addCourse.introduceTutor = introduceTutor
        addCourse.education = education
        addCourse.language = language
        addCourse.courseTitle = courseTitle
        addCourse.courseDesc = courseDesc
        addCourse.courseHours = courseHours
        addCourse.courseDay = courseDay
        addCourse.courseTime = courseTime
        addCourse.coursePrice = coursePrice
        addCourse.save()

        return redirect('/course-tutor/')

    username = request.user.profile.username
    user = Profile.objects.get(username=username)
    myCourse = Course.objects.filter(user=user)

    context = {'myCourse' : myCourse}

    return render(request, 'app/course-tutor.html',context)

def deleteCourse(request, id):

    course = Course.objects.get(id=id)
    course.delete()

    return redirect ('/course-tutor/')

# calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True, user=self.request.user.profile)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@login_required
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    username = request.user.username
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form = form.save(commit=False)
        form.user = Profile.objects.get(username=username)
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'app/event.html', {'form': form,'event_id' : event_id})

def deleteEvent(request, event_id):
   
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect ('/calendar/')