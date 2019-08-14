from .models import Riddle, Option
from django.shortcuts import get_object_or_404, render, redirect

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
            "riddle": get_object_or_404(Riddle, pk = riddle_id),
            "error_message": error_message
        })


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