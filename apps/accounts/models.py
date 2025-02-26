from django.db import models
from django.contrib.auth.models import  AbstractUser,BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле email должно быть заполнено')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Супер пользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Супер пользователь должен иметь is_superuser=True')

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Почта',unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatar/',blank=True,null=True)
    phone = models.IntegerField('Номер телефона',blank=True,null=True)
    profession = models.CharField('Профессия', max_length=50, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ползователь'
        verbose_name_plural = 'Ползователи'