from django.test import TestCase

def home(request):
	return render(request, 'main.html',{})