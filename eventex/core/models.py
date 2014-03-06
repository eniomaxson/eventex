# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    url = models.URLField(_('Url'))
    description = models.CharField(_(u'Descrição'), max_length=50)
    slug = models.SlugField(_('Slug'))

    class Meta:
		verbose_name = _('Palestrante')
		verbose_name_plural = _('Palestrantes')

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    
    KINDS = (
    	('P', _('Telefone')),
    	('E', _('Email')),
    	('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker',verbose_name=_('Palestrantes'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=50)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return self.value
    