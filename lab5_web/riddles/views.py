from .models import Riddle, Option, Message
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
import json


def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]

    return render(
        request,
        "index.html",
        {
            "latest_riddles":
                Riddle.objects.order_by('-pub_date')[:5],
            "message": message
        })


def detail(request, riddle_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    
    return render(
        request,
        "answer.html",
        {
            "riddle": get_object_or_404(Riddle, pk=riddle_id),
            "error_message": error_message,
            "latest_messages": Message.objects.filter(chat_id=riddle_id).order_by('-pub_date')[:5]
        }
    )


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk = riddle_id)
    try:
        option = riddle.option_set.get(pk = request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return redirect(
            '/riddles' + str(riddle_id) +
            '?error_message=Option does not exist',
        )
    else:
        if option.correct:
            return redirect("/riddles/?message=Nice! Choose another one!")
        else:
            return redirect(
                '/riddles/' + str(riddle_id) +
                '?error_message=Wrong Answer!',
            )


def post(request, riddle_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(Riddle, pk=riddle_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url+str(riddle_id))


def msg_list(request, riddle_id):
    res = list(Message.objects.filter(chat_id=riddle_id).order_by('-pub_date')[:5].values('author__username','pub_date','message'))
    for r in res:
        r['pub_date'] = r['pub_date'].strftime('%d.%m.%Y %H:%M:%S')
    return JsonResponse(json.dumps(res), safe=False)


app_url = "/riddles/"
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
