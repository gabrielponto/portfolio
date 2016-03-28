# -*- coding: utf-8 -*-
from django.db import models
from Portfolio.settings import MEDIA_URL
from autoslug.fields import AutoSlugField
from redactor.fields import RedactorField


class Block(models.Model):
    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    text = models.TextField(verbose_name=u'Texto')
    position = models.IntegerField(verbose_name=u'Posição')
    background = models.ImageField(verbose_name=u'Plano de Fundo', blank=True, upload_to='img/block')
    background_color = models.CharField(max_length=7, verbose_name='Cor')
    
    @property
    def backgroundurl(self):
        return "{0}/{1}".format(MEDIA_URL, self.background.__str__())
    
class Case(models.Model):
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=100, verbose_name=u'Título')
    content = RedactorField(verbose_name=u'Conteúdo')
    slug = AutoSlugField(verbose_name=u'Slug', populate_from='title', unique=False, blank=True)
    
class BlockCase(Block):
    case = models.ForeignKey(Case)
    logo = models.ImageField(verbose_name='Logo', upload_to='img/blockcase')
    
    @property
    def logourl(self):
        return "{0}/{1}".format(MEDIA_URL, self.logo.__str__())
    
class Skill(models.Model):
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-rating']
    name = models.CharField(max_length=100, verbose_name=u'Nome')
    rating = models.IntegerField(verbose_name=u'Nota')
    color = models.CharField(max_length=7, verbose_name=u'Cor')
    
class Badge(models.Model):
    def __unicode__(self):
        return self.name
    
    name = models.CharField(max_length=100, verbose_name=u'Nome')
    badge = models.ImageField(verbose_name=u'Badge')
    url = models.URLField(verbose_name=u'Link')
    