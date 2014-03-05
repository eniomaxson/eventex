from django.contrib import admin
from eventex.core.models import Speaker


class SpeakerAdmin(admin.ModelAdmin):
	pass		

admin.site.register(Speaker,SpeakerAdmin)