from mongoapp.models import PollModel, ChoiceModel
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import logging


def index(request):
    data = {}
    p = PollModel.objects.all()
    data["polls"] = p
    return render(request,"mongoapp/index.html",data)


def create(request):
    choice1 = ChoiceModel(choice_text="option a", votes=20)
    choice2 = ChoiceModel(choice_text="option a", votes=12)
    choice3 = ChoiceModel(choice_text="option a", votes=9)
    choice4 = ChoiceModel(choice_text="option a", votes=21)

    choices = [choice1, choice2, choice3, choice4]

    poll = PollModel(question="This is a sample question", pub_date=datetime.datetime.now(), choices=choices)
    poll.save()

    poll = PollModel(question="This is another sample question with same choices", pub_date=datetime.datetime.now(),
                     choices=choices)
    poll.save()

    return HttpResponseRedirect(reverse("mongoapp:show"))


def show(request):
    data = {}
    p = PollModel.objects.all()
    data["polls"] = p
    return render(request, "mongoapp/show.html", data)


def delete(request, document_id):
    PollModel.objects.filter(id=document_id).delete()
    return HttpResponseRedirect(reverse("mongoapp:show"))
