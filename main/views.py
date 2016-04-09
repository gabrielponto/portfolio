from django.shortcuts import render
from .models import Block, Case, BlockCase, Skill
from django.core.mail import EmailMessage

def index(request, contact=False):
    blocks = Block.objects.order_by('position')
    skills = Skill.objects.order_by('-rating')
    context = {'blocks': blocks, 'skills': skills, 'contact': False}
    if contact:
        context['contact'] = True
    return render(request, 'main/index.html', context)

def case(request, name):
    case = Case.objects.get(slug=name)
    context = {'case': case}
    return render(request, 'main/case.ajax.html', context)

def contact(request):
    post = request.POST
    if post:
        message = u'<p>' + post.get('name') + u' (' + post.get('email') + u') enviou a seguinte mensagem: </p>'
        message += u'<p>' + post.get('message') + u'</p>'
        email = EmailMessage('Contato Recebido pelo Form do Site', message, to=['gabriellucianooliveira@gmail.com'])
        email.send()
        ctx = True
    else:
        ctx = False
    return index(request, ctx)
