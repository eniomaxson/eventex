# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, cpf, name=None, password=None):
		user = self.model(cpf=cpf, name=name)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, **credentials):
		return self.create_user(**credentials)

class User(AbstractBaseUser):
	cpf  = models.CharField(unique=True, max_length=11,db_index=True)
	name = models.CharField(null=True, max_length=50)

	USERNAME_FIELD = 'cpf'

	objects = UserManager()

	def __unicode__(self):
		return self.name

	@property
	def is_staff(self):
		return True
	
	def has_module_perms(self, app_label):
		return True
	
	def has_perm(self, perm, obj=None):
		return True

	def get_short_name(self):
		return self.name
	
	def get_full_name(self):
		return self.name