# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import KindContactManager,PeriodManager

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
    
    @models.permalink
    def get_absolute_url(self):
		return ('core:speaker_detail', (), {'slug': self.slug})

class Contact(models.Model):
    
    KINDS = (
    	('P', _('Telefone')),
    	('E', _('Email')),
    	('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker',verbose_name=_('Palestrantes'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=50)
    
    objects = models.Manager()
    
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes  = KindContactManager('F')

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __unicode__(self):
        return self.value


class Talk(models.Model):
    title  = models.CharField(_(u'Título'), max_length=200)
    description = models.TextField(_(u'Descrição'), max_length=255)
    start_time = models.TimeField(_(u'Horário'), blank=True)
    
    speakers = models.ManyToManyField('Speaker', verbose_name=_('Palestrantes'))
    
    objects = PeriodManager()

    class Meta:
        verbose_name = _('Palestra')
        verbose_name_plural = _('Palestras')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
		return ('core:talk_detail', (), {'pk': self.pk})

    @property
    def slides(self):
		return self.media_set.filter(kind='SL')

    @property
    def videos(self):
		return self.media_set.filter(kind='YT')

class Course(Talk):
	slots = models.IntegerField(_('vagas'))
	notes = models.TextField(_(u'Observações'))

	objects = PeriodManager()

class Media(models.Model):

	MEDIAS = (
		('YT', _('Youtube')),
		('SL', _('SlideShare'))
	)

	talk = models.ForeignKey('Talk', verbose_name=_('palestras'))
	kind = models.CharField(_('tipo'), max_length=2, choices=MEDIAS)
	title = models.CharField(_('título'), max_length=255)
	media_id= models.CharField(_('ref'),max_length=255)

	def __unicode__(self):
		return u'%s - %s' % (self.talk.title, self.title)
