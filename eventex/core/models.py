# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    url = models.URLField(_('Url'))
    description = models.CharField(_('Descrição'), max_length=50)
    slug = models.SlugField(_('Slug'))

    class Meta:
		verbose_name = _('Speaker')
		verbose_name_plural = _('Speakers')

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    
    speaker = models.ForeignKey('Speaker',verbose_name=_('Palestrantes'))
    kind = models.CharField(_('Tipo'), max_length=1)
    value = models.CharField(_('Valor'), max_length=50)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        pass
    