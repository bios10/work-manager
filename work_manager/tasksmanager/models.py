from django.db import models
from django.contrib.auth.models import User

error_name = {
    'required': 'You must type a name!',
    'invalid': 'Wrong format.'
}


class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True, default=None, blank=True)
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)

    def __str__(self):
        return self.user_auth.username


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=100, verbose_name="Client name")


class Supervisor(UserProfile):
    specialization = models.CharField(max_length=50, verbose_name="Specialization")


class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name="Supervisor")


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time", null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)
    app_user = models.ForeignKey(Developer, verbose_name="Developer")