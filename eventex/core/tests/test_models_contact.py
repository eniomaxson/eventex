# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker,Contact
from django.core.exceptions import ValidationError

class ContactModelTest(TestCase):

	def setUp(self):
		self.speaker = Speaker.objects.create(name='Henrique Bastos',slug='henrique-bastos', description='Passionate software developer!')

	def test_email(self):
		contact = Contact.objects.create(speaker= self.speaker, kind='E', value='henrique@bastos.net')
		
		self.assertEqual(1,len(Contact.objects.all()))

	def test_phone(self):
		contact = Contact.objects.create(speaker= self.speaker, kind='P', value='21996186180')

		self.assertEqual(1,len(Contact.objects.all()))

	def test_fax(self):
		contact = Contact.objects.create(speaker= self.speaker, kind='F', value='2199188298')
		
		self.assertEqual(1,len(Contact.objects.all()))

	def test_kind(self):
		'Contact should be limited to E,P or F'
		contact = Contact.objects.create(speaker= self.speaker, kind='A', value='2199188298')

		self.assertRaises(ValidationError, contact.full_clean)

	def test_unicode(self):
		'Contact string representation should be value'
		contact = Contact.objects.create(speaker= self.speaker, kind='E', value='enio.maxson@gmail.com')

		self.assertEqual(u'enio.maxson@gmail.com', unicode(contact))
			