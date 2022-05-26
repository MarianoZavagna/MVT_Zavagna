from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from app1.models import Family

# Create your views here.


def post_family(request, name: str, dni: int, nacdate: str):
    family = Family(name=name, dni=dni, nacdate=nacdate)
    family.save() # guardo en base de datos

    context_dict = {
        'family': family
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app1/post_family.html"
    )


def get_family(request, id: int):
    family = Family.objects.get(pk=id)

    context_dict = {
        'family': family
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app1/get_family.html",
    )


def all_family(request):
    family = Family.objects.all()

    context_dict = {
        'family': family
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app1/all_family.html"
    )
