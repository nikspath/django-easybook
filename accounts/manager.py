from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

	def create_user(self,phone_number,password = None,**extra_field):
		if not phone_number:
			raise ValueError("Please enter phone number")
		extra_field['email']=self.normalize_email(extra_field['email'])
		user=self.model(phone_number=phone_number,**extra_field)
		user.set_password(password)
		user.save(using=self.db)

	def create_superuser(self,phone_number,password,**extra_field):
		extra_field.setdefault('is_staff',True)
		extra_field.setdefault('is_active',True)
		extra_field.setdefault('is_superuser',True)

		return self.create_user(phone_number,password,**extra_field)		




