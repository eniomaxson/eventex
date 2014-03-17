from django.test import TestCase
from django.contrib.auth import  get_user_model
from eventex.myauth.backends import EmailBackend
from django.test.utils import override_settings
from unittest import skip

@skip
class EmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user(username='enio', email='enio@gmail.com',password='123456')
		self.backend = EmailBackend()

	def test_autenticate_with_email(self):
		user = self.backend.authenticate(email='enio@gmail.com',password='123456')
		self.assertIsNotNone(user)

	def test_wrong_password(self):
		user = self.backend.authenticate(email='enio@gmail.com',password='wrong')
		self.assertIsNone(user)

	def test_unknown_user(self):
		user = 	self.backend.authenticate(email='unknown@mail.com',password='abracadabra')
		self.assertIsNone(user)

	def test_get_user(self):
		self.assertIsNotNone(self.backend.get_user(1))

@skip
@override_settings(AUTHENTICATION_BACKENDS=('eventex.myauth.backends.EmailBackend',))
class FunctionalEmailBackendTest(TestCase):
	def setUp(self):
		UserModel = get_user_model()
		UserModel.objects.create_user( username='enio', email='enio@gmail.com', password='123456')

	def test_login_with_email(self):
		result = self.client.login(email='enio@gmail.com',password='123456')
		self.assertTrue(result)

	def test_login_with_username(self):
		result = self.client.login(username='enio@gmail.com',password='123456')
		self.assertTrue(result)