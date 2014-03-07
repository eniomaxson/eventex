# coding: utf-8
from django.test import TestCase
from eventex.core.models import Course
from eventex.core.managers import PeriodManager


class CourseModelTest(TestCase):
	def setUp(self):
		
		self.course = Course.objects.create(
				title=u'Tutorial Django',
				description=u'Descrição do curso.',
				start_time='10:00', slots=20)
	
	def test_create(self):
		self.assertEqual(1, Course.objects.count())

	def test_unicode(self):
		self.assertEqual(u'Tutorial Django', unicode(self.course))

	def test_speakers(self):
		'Course has many Speakers and vice-versa.'
		
		self.course.speakers.create(
			name='Henrique Bastos',
			slug='henrique-bastos',
			url='http://henriquebastos.net')
		
		self.assertEqual(1, self.course.speakers.count())
	
	def test_period_manager(self):
		'Course default manager must be instance of PeriodManager.'
		self.assertIsInstance(Course.objects, PeriodManager)