from .models import Student, Option, Message, UserRiddle, Mark
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.db.models import Avg
import json


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]

    return render(
        request,
        "index.html",
        {
            "all_students":
                Student.objects.order_by('-pub_date')[:5],
            "message": message
        })


def detail(request, student_id):
    error_message = None
    riddle = get_object_or_404(Student, pk = student_id)
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    
    return render(
        request,
        "answer.html",
        {
            "riddle": riddle,
            "error_message": error_message,
            "latest_messages": Message.objects.filter(chat_id=student_id).order_by('-pub_date')[:5],
            #"already_rated_by_user": Mark.objects.filter(author_id=request.user.id).count(),
            "user_rating": Mark.objects.filter(author_id=request.user.id).filter(student_id=student_id).aggregate(Avg('mark'))["mark__avg"],
            "avg_mark": Mark.objects.filter(student_id=student_id).aggregate(Avg('mark'))["mark__avg"],
            "already_rated_by_user": Mark.objects.filter(author_id = request.user.id).filter(student_id = student_id).count()
        }
    )


def answer(request, student_id):
    riddle = get_object_or_404(Student, pk = student_id)
    try:
        option = riddle.option_set.get(pk = request.POST['option'])
        #time_spent = request.GET['time_spent']
    except (KeyError, Option.DoesNotExist):
        return redirect(
            '/students' + str(student_id) +
            '?error_message=Option does not exist'
        )
    else:
        if option.correct:
            return redirect("/students/?message=Nice! Choose another one!")
        else:
            return redirect(
                '/students/' + str(student_id) +
                '?error_message=Wrong Answer!',
            )


def post(request, student_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(Student, pk=student_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(student_id))


def msg_list(request, student_id):
    res = list(Message.objects.filter(chat_id=student_id).order_by('-pub_date')[:5].values('author__username','pub_date','message'))
    for r in res:
        r['pub_date'] = r['pub_date'].strftime('%d.%m.%Y %H:%M:%S')
    return JsonResponse(json.dumps(res), safe=False)


def record_time(request, student_id):
    if "time_spent" in request.GET:
        riddle = get_object_or_404(Student, pk = student_id)
        time_spent = int(request.GET["time_spent"])
        user_attempt = UserRiddle()
        user_attempt.user = request.user
        user_attempt.attempt = 1
        user_attempt.riddle = riddle
        user_attempt.time_spent = time_spent
        user_attempt.save()


def post_mark(request, student_id):
    msg = Mark()
    msg.author = request.user
    msg.riddle = get_object_or_404(Student, pk=student_id)
    msg.mark = request.POST['mark']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(student_id))


def get_mark(request, student_id):
    res = Mark.objects\
            .filter(student_id=student_id)\
            .aggregate(Avg('mark'))

    return JsonResponse(json.dumps(res), safe=False)


app_url = "/students/"
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login/"
    template_name = "reg/register.html"


    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    success_url = app_url + 'login/'
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)
