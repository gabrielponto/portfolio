from django.shortcuts import render
from .models import Block, Case, BlockCase, Skill

def index(request):
    blocks = Block.objects.order_by('position')
    skills = Skill.objects.order_by('-rating')
    context = {'blocks': blocks, 'skills': skills}
    return render(request, 'main/index.html', context)

def case(request, name):
    case = Case.objects.get(slug=name)
    context = {'case': case}
    return render(request, 'main/case.ajax.html', context)
