from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from datetime import datetime
from app1.models import Family


def post_family(self, name: str, dni: int):
    template = loader.get_template('post_family.html')

    family = Family(name=name, dni=dni)
    family.save() # guardo en base de datos

    context_dict = {
        'family': family
    }

    render = template.render(context_dict)
    return HttpResponse(render)


def get_family(self, id: int):

    template = loader.get_template('get_family.html')

    family = Family.objects.get(pk=id)

    context_dict = {
        'family': family
    }

    render = template.render(context_dict)
    return HttpResponse(render)


def all_family(self):
    template = loader.get_template('all_family.html')

    family = Family.objects.all()

    context_dict = {
        'family': family
    }

    render = template.render(context_dict)
    return HttpResponse(render)

